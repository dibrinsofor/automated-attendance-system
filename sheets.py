import gspread
import time
from pprint import pprint
# from sendmail import send_email
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Attendance").sheet1

def attendance():
    sheet.update_cell(2,3, "Present")
    time.sleep(10)

def rest():
    i = 3 
    while sheet.cell(i,3).value != "":
        sheet.update_cell(i,3, "Absent")
        i += 1
        if i == 15:
            break
    send_email()

attendance()
rest()
# lecturerName = "Dr. Nsofor"
# print(f"Sending Attendance to {lecturerName}")
# time.sleep(5)
# print("Done!")

# data = sheet.get_all_records()
# pprint(data)