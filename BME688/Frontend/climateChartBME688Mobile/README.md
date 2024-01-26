## Climate Chart BME688 Mobile

This frontend can be used when the BME688 collects the data. Frontend contains three charts: temperature, celsius and pressure

## How to use

- open the /public/index.html file and check the sheet ID in loadData()
- run the server with ```node /server/index.js```
- probably the following error shows up: ```/usr/bin/node: /usr/lib/arm-linux-gnueabihf/libstdc++.so.6: version `GLIBCXX_3.4.26' not found (required by /usr/bin/node)```
- as a solution, downgrading node to an older version like v8.0.0 helped.
- finally type ```crontab -e``` to add a cron job. Add the command to run index.js as a cron job
