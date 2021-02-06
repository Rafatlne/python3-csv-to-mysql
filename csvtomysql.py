import csv
import mysql.connector
from mysql.connector import errorcode

def convertCsvToMysql():
    connection = mysql.connector.connect(user='root', password='', host='localhost')
    mycursor = connection.cursor()

    mycursor.execute("USE laravel_api")

    with open('files/madrasah.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        i = 1
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO nsp_institutions_madrasah(division_name, \
            district_name, upzila_name, eiin, institute_name, institute_type, division_id,district_id, upzila_id) \
            VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7], row[8])
            print(i)
            i +=  1
            try:
                # Execute the SQL command
                mycursor.execute(sql)
                # Commit your changes in the database
                connection.commit()
            except:
                # Rollback in case there is any error
                connection.rollback()
if __name__ == "__main__":
    convertCsvToMysql()