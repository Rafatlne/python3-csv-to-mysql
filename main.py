from ReadJsonClass import ReadJsonClass
from ReadSchoolClass import ReadSchoolClass

def main():
  readjson_obj = ReadJsonClass("district")
  district_json = readjson_obj.readJson()

  readjson_obj = ReadJsonClass("division")
  division_json = readjson_obj.readJson()

  readjson_obj = ReadJsonClass("upzilla")
  upzilla_json = readjson_obj.readJson()

  readschool_obj = ReadSchoolClass(division_json, district_json, upzilla_json)

if __name__== "__main__":
  main()