#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (res) {
    const title = JSON.parse(body);
    console.log(title.title);
    return;
  }
  console.log(err);
});
