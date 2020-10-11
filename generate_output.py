import algo.py
import xlsxwriter

#open algo.py and export data
f = open("algo.py", "r")

#creates an excel file
workbook = xlsxwriter.Workbook('Stocks.xlsx')
spreadsheet = workbook.add_worksheet()

Get_Stock()
#Stock patterns organized into columns
patterns = (
[ticker]
['Beta', beta]
['Previous Close']
['Open', Open]
['Bid', bid]
['Days Range', ]
['52 Week Range', ]
['Volume', volume]
)


# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, value in (patterns):
    spreadsheet.write(row, col,     item)
    spreadsheet.write(row, col + 1, value)
    row += 1

#Update stocks
Sub AutoRefresh()

 ActiveWorkbook.RefreshAll

 'Auto-Refresh in 0 hours, 1 minute, 0 seconds

 NextTime = Time + TimeSerial(0, 1, 0)

 Application.OnTime NextTime, &amp;amp;amp;amp;amp;quot;AutoRefresh&amp;amp;amp;amp;amp;quot;

End Sub

#Close the file once it's executed
workbook.close()
f.close()
