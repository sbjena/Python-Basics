from db import fetchTopFiveorder,fetchAllOrder
from ExportToExcel import generateEXcelfile
print("**** REPORT GENERATION **** ")
print("1: To fetch top 5 last orders ")
print("2: To fetch all order")
print("3: To exit")

def generateReport(myList):
    y = int(input("4: To generate excel report"))
    if y == 4:
        print("--GENERATING REPORT--")
        generateEXcelfile(myList)
1

x = int(input("Enter your choice"))
print(":you have entered ", x)

if x == 1:
    myList = fetchTopFiveorder()
    for row in myList:
        print("id: %s name: %s qty: %s location: %s" %(row[0],row[1],row[2],row[3]))
    if myList.__len__() >0:
        generateReport(myList)
if x == 2:
    myList = fetchAllOrder()
    for row in myList:
        print("id: %s name: %s qty: %s location: %s" % (row[0], row[1], row[2], row[3]))
    if myList.__len__() >0:
        generateReport(myList)