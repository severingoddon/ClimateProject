const express = require('express');
const app = express();
const PORT = 3001;


const path = require('path')
app.use(express.static('/home/pi/Desktop/PythonScripts/ClimateBME688/climateChatBME688Mobile/public'));

app.listen(PORT, () => console.log(`Server listening on port: ${PORT}`));
