import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("../secrets/Kindle Notes-7420d3fa2c18.json", scope)

client = gspread.authorize(creds)

sheet = client.open('Kindle Notes').sheet1
telemedicine = sheet.get_all_records()
print(telemedicine)

pp = pprint.PrettyPrinter()
employees = sheet.get_all_records()
pp.pprint(employees)

#"/secrets/Kindle Notes-7420d3fa2c18.json"