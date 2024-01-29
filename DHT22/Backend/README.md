## DHT22 backend

This backend can be utilized for data collection with the DHT22. Begin by connecting the wiring and then proceed to run the Python file.
The directory also contains the necessary code to display measurements on an lcd display. 

### Google cloud platform

The code stores date, time, temperature and humidity every 10 minutes in a google spreadsheet. To access the sheet from the raspberry pi, a "Dienstkonto" is needed.

- go to google cloud console
- create a new project (if not already done)
- go to "IAM"
- go to "Dienstkonten"
- create a new service account "Dienstkonto" if not already done
- go to "schlüssel" and hit "schlüssel hinzufügen"
- the result is a json file that is being downloaded.
- ClimateLogger.py uses it here: ```GDOCS_OAUTH_JSON = 'google-auth.json'```so make sure, that the file has the name ```google-auth.json```and is in the same directory.
- adjust the spreadsheet name if a different spreadsheet should be used. Important: that spreadsheet needs to give permission to the service account

### Cron job

To automatically launch the python script at boot, hit ```crontab -e```and add the skript call to the file. 
The command in crontab -e file may look like that: ```@reboot sleep 20 && /usr/bin/python /home/pi/Desktop/PythonScripts/climate-logger-main/ClimateLogger.py```
Note: sleep 20 is important as the raspberry isn't connected to the wifi yet but the script has already been launched. With a sleep 20s, the script won't crash. 
