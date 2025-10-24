const express = require('express');
const app = express();
const port = 8080;

app.get('/', (req, res) => {
  res.send('Hello World from Google Cloud!');
});

app.listen(port, () => {
  console.log(`Hello World app listening at http://localhost:${port}`);
});