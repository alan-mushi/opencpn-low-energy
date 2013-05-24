/*
 * This script is used to parse HTML output of the datalogger.php example present in Yocto-watt php library.
 * It transforms the HTML table in a csv file (that you can use to obtain charts).
 */
var rows = document.getElementsByTagName( "tr" ); // On charge toutes les lignes

var line = "time;power (watt)<br />";
// For each line, we extract the time and the power (average) of the row.
for( var i = 2 ; i < rows.length ; i++ ) {
	var time = rows.item(i).cells.item(0).innerHTML;
	var avgPower = rows.item(i).cells.item(2).innerHTML;
	// We build the line to print
	line += time.toString() + ";" + avgPower.toString() + "<br />";
}
document.write( line.toString() );