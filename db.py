import mysql.connector
from mysql.connector import Error
str =""
def fetchTopFiveorder():
  print("inside fetchTop10order method")
  str = "SELECT * FROM world.order limit 5"
  curser =callDB(str)
  return curser

def fetchAllOrder():
  print("inside fetchAllOrder method")
  str = "SELECT * FROM world.order"
  curser = callDB(str)
  return curser

def callDB(query):

    myList=[]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="world"
        )
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print("\nPrinting each record")

        #   print("Id = ", row[0], )
        #    print("Name = ", row[1])
        #    print("qty  = ", row[2])
        #    print("location = ", row[3], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
    return records