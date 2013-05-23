#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys,argparse
# add Sources to the PYTHONPATH
sys.path.append(os.path.join("Sources"))
from yocto_api import *
from yocto_datalogger import *
from datetime import *

import time

parser = argparse.ArgumentParser( description="Take and fetch measures from a Yocto-X usb device. Exports the data in csv" )
parser.add_argument( "-s", "--serial", dest="serial", nargs='?', required=True, help="the Yocto-Watt serial to use. If no argument is specified, print all available devices.")
parser.add_argument ("-f", "--flush", dest="flush", action="store_true", help="delete all the runs and logs on the device's memory. Is executed before anything else." )
parser.add_argument( "-o", "--output", dest="output_file", nargs=1, help="output file for the data. If none specified, a default name is used for --duration and --dump-last." )
parser.add_argument( "-c", "--chart-output", dest="chart_output", action='store_true', help="Exports in a csv file ready for charts. Need --dump-last or --duration." )
group = parser.add_mutually_exclusive_group()
group.add_argument( "-m", "--measure-duration", dest="duration", type=int, help="duration of the measure in seconds." )
group.add_argument( "-d", "--dump-last", dest="dump_last", action="store_true", help="dump the last data stream." )
args = parser.parse_args()

if len(sys.argv) == 1 :
	parser.print_help()
	sys.exit(1)

errmsg = YRefParam()
# Setup the API to use local USB devices
if YAPI.RegisterHub( "usb", errmsg ) != YAPI.SUCCESS :
	sys.exit( "[-] Failed register hub : " + errmsg.value )

#################
### Functions ###
#################

# List yocto-* usb devices with a datalogger module.
# Print their serial number and logical name.
# If no device is found, the script exits with error code 1.
def list_devices() :
	logger = YDataLogger.FirstDataLogger()

	if logger == None :
		sys.stderr.write( "[-] No devices with datalogger module available (check your USB cable and your udev rules).\n" )
		sys.exit( 1 )

	while logger != None :
		serial = logger.get_module().get_serialNumber()
		if serial != None :
			print "\tSerial available : " + str( serial ),
			name = logger.get_logicalName()
			if name != YDataLogger.LOGICALNAME_INVALID :
				print "\t|\tSerial's name : " + str( name )

		logger = logger.nextDataLogger()
# end of list_devices()

# Write the supplied data stream in the filename.
# std_csv = { True | False }
#	If true "time elapsed" column is add to the log file.
def write_stream( stream, filename, std_csv = True ) :
	nrows = stream.get_rowCount()
	log_file = open( filename, 'w' )

	default_names = stream.get_columnNames()

	# let's remove values we don't use
	exclude_log_names = ['currentAC','voltageAC','currentDC','voltageDC']
	exclude_log_offsets = []
	column_names = []
	i = 0
	for name in default_names :
		if name in exclude_log_names :
			exclude_log_offsets.append( i )
		else :
			column_names.append( name )
		i += 1

	# We write the columns name
	if std_csv :
		log_file.write( 'time elapsed;' )

	for name in column_names :
		log_file.write( str( name ) + ';' )
	log_file.write( '\n' )
	
	if std_csv :
		i = 1
		row_interval = stream.get_dataSamplesInterval()
	
	table = stream.get_dataRows()
	table.pop( 0 ) # remove the initial measure (actual value when the measure start)
	for row in table :
		if std_csv :
			log_file.write( str( i ) + ';' )

		for pos in range(len(row)) :
			if not pos in exclude_log_offsets :
				log_file.write( str( row[pos] ) + ';' )
		log_file.write( '\n' )

		if std_csv :
			i += row_interval

	log_file.close()
	print "[+] '" + filename + "' log wrote"
# end of write_stream()

# "Proxy" for write_stream.
# Set the filenames (for regular csv and chart csv) and the last data stream.
def dump() :
	dataStreams = YRefParam()
	if logger.get_dataStreams( dataStreams ) != YAPI.SUCCESS :
		sys.stderr.write( "[-] Fetch of data streams (get_dataStreams) failed, exiting...\n" )
		sys.exit( 1 )
	offset_last_stream = len(dataStreams.value) -1
	if offset_last_stream <= 0 :
		sys.stderr.write( "[-] No data stream available, exiting...\n" )
		sys.exit( 1 )
	last_stream = dataStreams.value[offset_last_stream]

	filename = args.output_file
	if filename == None :
		# making default filename
		filename = "log_stream_" + str( offset_last_stream ) + ".csv"

	write_stream( last_stream, filename, True )

	if args.chart_output != None :
		# making default filename
		chart_filename = "chart_" + filename
		write_stream( last_stream, chart_filename, False )
# end of dump()

#####################
### End Functions ###
#####################


# Handling the 'serial' option
if args.serial != None :
	logger = YDataLogger.FindDataLogger( args.serial )
	if not logger.isOnline() :
		sys.stderr.write( "[-] The device can't be found, check your serial parameter or your USB cable." )
		sys.exit( 1 )
	else :
		print "[+] Device " + args.serial + " found."
		if args.flush == False and args.dump_last == False and args.duration == None :
			sys.stderr.write( "[-] You have to select an action {--flush | --dump-last | --measure-duration}.\n\tSee " + sys.argv[0] + " for details.\n" )
			sys.exit( 1 )
else :
	print "[*] List all currently available devices :"
	list_devices()
	sys.exit( 0 )

# Handling the 'flush' option
if args.flush :
	if logger.forgetAllDataStreams() != YAPI.SUCCESS :
		sys.stderr.write( "[-] Undefined error while flushing runs & logs, exiting...\n" )
		sys.exit( 1 )
	else :
		print "[+] Flushing of runs & logs done."

# Handling the 'duration' option
if args.duration != None and args.duration <= 0 :
	sys.stderr.write( "[-] Invalid log/measure duration.\n" )
elif args.duration != None :
	# in case automatic log is enable, we stop the recording
	if logger.get_autoStart() == YDataLogger.AUTOSTART_ON :
		logger.set_recording( YDataLogger.RECORDING_OFF )
	
	if logger.set_recording( YDataLogger.RECORDING_ON ) != YAPI.SUCCESS :
		sys.stderr.write( "[-] The logger can't be started, exiting...\n" )
		sys.exit( 1 )

	print "\n[+] Start logger at " + datetime.fromtimestamp(logger.get_timeUTC()).strftime('%H:%M:%S') + " (device time)",
	print "for " + str( args.duration ) + " seconds."
	time.sleep( args.duration )
	if logger.set_recording( YDataLogger.RECORDING_OFF ) != YAPI.SUCCESS :
		sys.stderr.write( "[-] The logger can't be stopped, exiting..." )
		sys.exit( 1 )
	print "[+] Stop logger at " + datetime.fromtimestamp(logger.get_timeUTC()).strftime('%H:%M:%S') + " (device time)"

	print "\n[*] Writting the results to disk..."
	dump()

# Handling the 'dump_last' option
if args.dump_last :
	print "\n[*] Dumping last data stream..."
	dump()
