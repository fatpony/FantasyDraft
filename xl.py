import xlwings as xw

wb = xw.Book('C:\Users\Joseph\Google Drive (fatpony@gmail.com)\sheets_example.gsheet')
sheet1 = wb.sheets('Sheet1')
sheet1.range('B2').value = 46
