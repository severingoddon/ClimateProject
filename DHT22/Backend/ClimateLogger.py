
import json
import sys
import time
import datetime

import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Type of sensor
DHT_TYPE = Adafruit_DHT.DHT22

# GPIO 4
DHT_PIN  = 4

# auth file for google docs
GDOCS_OAUTH_JSON       = '/home/pi/Desktop/PythonScripts/climate-logger-main/google-auth.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'climate-table'

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 600


def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    MAX_ATTEMPTS = 5
    for attempt in range(MAX_ATTEMPTS):
        try:
            scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
            gc = gspread.authorize(credentials)
            worksheet = gc.open(spreadsheet).sheet1
            return worksheet
        except Exception as ex:
            print('Attempt', attempt, 'failed to login and get spreadsheet. Waiting 10 seconds before retrying...')
            time.sleep(10)
    print('Failed to login after', MAX_ATTEMPTS, 'attempts. Exiting.')
    sys.exit(1)



print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = None

index = 0

while True:
    
    # Login if necessary.
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    # Attempt to get sensor reading.
    humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)

    # Skip to the next reading if a valid measurement couldn't be taken.

    if humidity is None or temp is None:
        time.sleep(2)
        continue

    try:
        # Append the data in the spreadsheet, including a timestamp
        worksheet.insert_row((datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%H:%M'), temp, humidity),2)
    except:

        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue

    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))

    time.sleep(FREQUENCY_SECONDS)
