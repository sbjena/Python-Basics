# import xlsxwriter module 
import xlsxwriter

def generateEXcelfile(myList):
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook('hello.xlsx')

    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()

    # Use the worksheet object to write
    # data via the write() method.
    scores = (
        ['ankit', 1000],
        ['rahul', 100],
        ['priya', 300],
        ['harshita', 50],
    )
    row = 0
    col = 0
    for name, score in (scores):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, score)
        row += 1
#worksheet.write('A1', item[0])
#worksheet.write('B1', item[1])
#worksheet.write('C1', item[2])
#worksheet.write('D1', item[3])
#    worksheet.write('A1', 'Hello..')
#    worksheet.write('B1', 'Geeks')
#    worksheet.write('C1', 'For')
#    worksheet.write('D1', 'Geeks')

    # Finally, close the Excel file
    # via the close() method.
    workbook.close()