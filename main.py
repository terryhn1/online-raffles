from __future__ import print_function
import pickle
import os.path
import random
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from Raffle import Raffle,RaffleBag, RaffleListing

#For documentation on the Google Sheets API, visit https://developers.google.com/sheets/api
#Visit https://developers.google.com/sheets/api/quickstart/python and look at Step 1/2 to set up the environment to run this code.

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# ---------------------------------- FILL IN PORTION ------------------------------------------------

#Fill ORIGINAL_SPREADSHEET with the filled out raffle form and RESULTS_SPREADSHEET with an empty form.
# To find the id,  find the value between '/d/' and '/edit' in the URL
# MAKE SURE THAT LINK AUTHORIZATION FOR FORM IS SET TO 'ALL CAN VIEW'
ORIGINAL_SPREADSHEET = "COPY PASTE ID HERE. EXAMPLE LOOKS LIKE 1ry7ovBwLqLBFqv0v3GM687TRMO_K0TJgpGCLuoMCk30"
RESULTS_SPREADSHEET = "COPY PASTE ID HERE"


#FILL IN. A sample for format has been given.
#Below, the list given requires Named Ranges. Named Ranges can be found by selecting a column or row of data on Google Sheets, right clicking and go to "Define Named Range".
#In the list below, "B1:F" is given. "F" corresponds to the last column for which you have a prize while B1 corresponds to the first email of the column.
#Only change "F" depending on how many prizes you have. If you have 2 prizes, change "F" to "F". If you have 3 prizes, change "F" to "G". This continues on. 
ranges = ["\'Form Responses 1\'!B1:F"]

#FILL IN. Sample has been given for two prizes has been given.
#Same as ranges, this list uses Named Ranges in order to select which areas to write data to the new spreadsheet.
#Here, we have "Sheet1!A2:B". "A2" refers to the first name in a certain raffle pool. Do not change this. "B" refers to the last column for how many prizes you have.
#If you have 1 prize, change "B" to "A". If 3 prizes, change "B" to "C". This continues on. The same methodology is used with the second item, "Sheet1!A1:B1".
#However, do not change the number. Example: If you have 5 prizes, change "B1" to "E1".
prizes = ["Sheet1!A2:B", "Sheet1!A1:B1"]

# ---------------------------------- FILL IN PORTION ------------------------------------------------


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    print("Creating a Sheets object", flush = True)
    sheet = service.spreadsheets()
    result = sheet.values().batchGet(spreadsheetId=ORIGINAL_SPREADSHEET,
                                ranges=ranges, majorDimension = 'ROWS').execute()
    data = result.get('valueRanges', [])[0]

    #Prize names will be Index 3 and forth
    index = 3
    listing = RaffleListing()
    #set up the Listing
    while True:
        #If it is the last index
        if index == len(data['values'][0]) -1:
            bag = RaffleBag(data['values'][0][index])
            listing.add_bag(bag)
            break
        else:
            bag = RaffleBag(data['values'][0][index])
            listing.add_bag(bag)
            index += 1
    
    #Iterate participant to participant
    respondent_index = 1
    while (respondent_index != len(data['values'])):
        
        respondent = data['values'][respondent_index]
        prize_index = 0
        while (prize_index +3 != len(respondent)):
            bag = listing.get_bag(prize_index)
            bag.add_raffles(respondent[1], respondent[0], int(respondent[prize_index +3]))
            prize_index += 1
        
        respondent_index += 1

    #Write to the results sheet
    results = list()
    results.append({
        'range':prizes[0],
        'values': [prize.stringify() for prize in listing.get_listing()],
        'majorDimension': 'COLUMNS'
    })
    
    results.append({
        'range': prizes[1],
        'values': [[data['values'][0][x] for x in range(len(data['values'][0])) if x >= 3]],
        'majorDimension': 'ROWS'
    })

    body = {
        'valueInputOption': 'RAW',
        'data': results
    }

    resultant_sheets = service.spreadsheets()
    results = resultant_sheets.values().batchUpdate(spreadsheetId = RESULTS_SPREADSHEET,
                                                    body = body).execute()


        

if __name__ == '__main__':
    main()
