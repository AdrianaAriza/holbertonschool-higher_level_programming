#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18';

request(url, function (_err, _res, body) {
  const title = JSON.parse(body);
  console.log(title.films.length);
});
