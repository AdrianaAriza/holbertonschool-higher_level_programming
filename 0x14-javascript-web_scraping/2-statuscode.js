#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res) {
  if (err) {
    console.log('code: ' + err.statusCode);
    return;
  }
  console.log('code: ' + res.statusCode);
});