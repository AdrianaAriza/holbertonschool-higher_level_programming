#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let cont = 0;
let x = /18/;

request(url, function (err, res, body) {
  if (res) {
    const title = JSON.parse(body);
    const list = title.results.map(ele => ele.characters);
    list.forEach(e => x.test(e) ? cont++ : '');
    console.log(cont);
    return;
  }
  console.log(err);
});
