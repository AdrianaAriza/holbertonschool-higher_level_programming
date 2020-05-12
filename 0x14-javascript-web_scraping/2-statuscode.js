#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (res) {
  console.log('code: ' + res.statusCode);
});
