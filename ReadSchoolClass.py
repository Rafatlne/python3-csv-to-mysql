import csv
import json
import csvtomysql

# ReadSchoolCsv class
class ReadSchoolClass:
    def __init__(self, division, district, upzilla):
        self.division = division
        self.district =  district
        self.upzilla = upzilla
        self.readSchoolCsv()

    def readSchoolCsv(self):
        csv_list = ["EBTEDAYEE_LIST"]
        for csv_name in csv_list:
            with open('files/' + csv_name + '.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                division_id = self.compareDivision('lol')
                i = 0
                for row in csv_reader:
                    if(i > 0):
                        division_id = self.compareDivision(row[0].upper())
                        district_id = self.compareDistrict(row[1].upper())
                        upzilla_id = self.compareUpzilla(row[2].upper())
                        row.append(division_id)
                        row.append(district_id)
                        row.append(upzilla_id)
                        self.writeToExistingCsv(row)
                    i = 1
        
        csvtomysql.convertCsvToMysql()

    def compareDivision(self, division_name):
        for value in self.division:
            if(division_name == value['name'].upper()):
                return value['id']
        return 0

    def compareDistrict(self, district_name):
        for value in self.district:
            if(district_name == value['name'].upper()):
                return value['id']
        return 0

    def compareUpzilla(self, upzilla_name):
        for value in self.upzilla:
            if(upzilla_name == value['name'].upper()):
                return value['id']
        return 0
            

    def writeToExistingCsv(self, row):
        with open('files/madrasah.csv',  'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            f.close()
