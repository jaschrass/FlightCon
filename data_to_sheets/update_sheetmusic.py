from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1eCCDVIlr9TSuf_XEd07YGtiAFY22--dnr8dvLocctr8'
RANGE_NAME = 'Sheet1!A2:C'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Latitude, Noise (PLdB):')
        for row in values:
            if row != []:
                # Print columns A and C, which correspond to indices 0 and 2.
                print('%s, %s' % (row[0], row[2]))

    requests = []
    title = 'SheetMusicSplice'
    # Change the spreadsheet's title.
    requests.append({
        'updateSpreadsheetProperties': {
            'properties': {
                'title': title
            },
            'fields': 'title'
        }
    })

    # Find and replace text
    find = 'C2'
    replacement = '80.03504098'
    requests.append({
        'findReplace': {
            'find': find,
            'replacement': replacement,
            'allSheets': True
        }
    })

    # Update Cells
    requests.append({
        'updateCells': {
            'range': {
                'endRowIndex': 2,
                'endColumnIndex': 2,
                'startColumnIndex': 1,
                'startRowIndex': 1,
            },
            'rows': [{
                'values': [{
                    'userEnteredValue': {
                        'numberValue': 5
                    }
                }]
            }],
            'fields': '*'
        }
    })

    # Add additional requests (operations) ...

    body = {
        'requests': requests
    }
    response = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=body).execute()
    find_replace_response = response.get('replies')[1].get('findReplace')
    print('{0} replacements made.'.format(
        find_replace_response.get('occurrencesChanged')))


if __name__ == '__main__':
    main()
