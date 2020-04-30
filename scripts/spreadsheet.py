import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("../secrets/Kindle Notes-7420d3fa2c18.json", scope)

client = gspread.authorize(creds)

sheet = client.open('Kindle Notes').sheet1
notes = sheet.get_all_records()
#print(notes)

pp = pprint.PrettyPrinter()
#employees = sheet.get_all_records()
pp.pprint(notes)

Book = "Book 2"
Author = "Author 2"
Type = "Type 2"
Location = "Location 2"
Word = "Word 2"
Sentance = "Sen 2"







def insertValues(row):
    index = 2
    sheet.insert_row(row,index)


