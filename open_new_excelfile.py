import win32com
import win32com.client
excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.Workbooks.Add()
ws=wb.Worksheets("sheet1")
ws.Cells(1,1).Value="Hellow,Excel!"
wb.SaveAs(r"D:\Book1")
wb.Close()
excel.Quit()