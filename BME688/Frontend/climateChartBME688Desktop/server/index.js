const express = require('express');
const app = express();
const PORT = 3000;


const path = require('path')
app.use(express.static('/home/pi/Desktop/PythonScripts/ClimateBME688/climateChartBME688Desktop/public'));

app.listen(PORT, () => console.log(`Server listening on port: ${PORT}`));
