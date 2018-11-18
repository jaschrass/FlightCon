'''
Python outputs to spreadsheet demo
pip install gspread oauth2client
docs for client.json:
    https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
    Youtube vid:
    https://www.youtube.com/watch?v=vISRn5qFrkM
'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Legislators 2017').sheet1

legislators = sheet.get_all_records()
print(legislators)
