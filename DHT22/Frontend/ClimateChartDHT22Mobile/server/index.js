const express = require('express');
const app = express();
const PORT = 3001;


const path = require('path')
app.use(express.static('/home/pi/Desktop/PythonScripts/climate-logger-chart-mobile/public'));

app.listen(PORT, () => console.log(`Server listening on port: ${PORT}`));
