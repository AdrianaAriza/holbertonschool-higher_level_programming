#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (res) {
    const title = body.split(':')[1].split(',')[0].split('"')[1];
    console.log(title);
    return;
  }
  console.log(err);
});
