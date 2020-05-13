#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let cont = 0;

request(url, function (err, res, body) {
  if (res) {
    const title = JSON.parse(body);
    const list = title.results.map(ele => ele.characters);
    list.forEach(e => e.includes('https://swapi-api.hbtn.io/api/people/18/') ||
    e.includes('http://swapi.co/api/people/18/') ? cont++ : '');
    console.log(cont);
    return;
  }
  console.log(err);
});
