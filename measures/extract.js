/*
 * This script is used to parse HTML output of the datalogger.php example present in Yocto-watt php library.
 * It computes the average power for a session and transform the HTML table in a csv file (that you can use to obtain charts).
 */
var rows = document.getElementsByTagName( "tr" ); // On charge toutes les lignes

var line = "time;power (watt)<br />";
var sumSession = 0;
// For each line, we extract the time and the power (average) of the row.
// We also make the sum of each power in order to obtain an average value for power.
for( var i = 2 ; i < rows.length ; i++ ) {
	var time = rows.item(i).cells.item(0).innerHTML;
	var avgPower = rows.item(i).cells.item(2).innerHTML;
	sumSession += parseFloat( avgPower ); 
	// We build the line to print
	line += time.toString() + ";" + avgPower.toString() + "<br />";
}
document.write( line.toString() );

document.write( "<br /><br />;Average Power : " );
var avgSession = sumSession / rows.length; // The average calculation
document.write( avgSession );
