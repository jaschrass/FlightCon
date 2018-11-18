/**
 * AppsScript script to run in a Google Spreadsheet that synchronizes its
 * contents with a Fusion Table by replacing all rows.
 * Explination Link:
 * https://www.youtube.com/watch?v=1wzmRzeLZM4

 */

// Replace with your Fusion Table's ID (from File > About this table)
var TABLE_ID = 'YOUR TABLE ID';

// First row that has data, as opposed to header information
var FIRST_DATA_ROW = 2;

// True means the spreadsheet and table must have the same column count
var REQUIRE_SAME_COLUMNS = true;

/**
 * Replaces all rows in the Fusion Table identified by TABLE_ID with the
 * current sheet's data, starting at FIRST_DATA_ROW.
 */
function sync() {
  var tasks = FusionTables.Task.list(TABLE_ID);
  // Only run if there are no outstanding deletions or schema changes.
  if (tasks.totalItems == 0) {
    var sheet = SpreadsheetApp.getActiveSheet();
    var wholeSheet = sheet.getRange(1, 1, sheet.getLastRow(),
        sheet.getLastColumn());
    var values = wholeSheet.getValues();
    if (values.length > 1) {
      var csvBlob = Utilities.newBlob(convertToCsv_(values),
          'application/octet-stream');
      FusionTables.Table.replaceRows(TABLE_ID, csvBlob,
         { isStrict: REQUIRE_SAME_COLUMNS, startLine: FIRST_DATA_ROW - 1 });
      Logger.log('Replaced ' + values.length + ' rows');
    }
  } else {
    Logger.log('Skipping row replacement because of ' + tasks.totalItems +
        ' active background task(s)');
  }
}
