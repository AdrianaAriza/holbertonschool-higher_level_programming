#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (res) {
    fs.writeFile(process.argv[3], body, 'utf-8', err => {
      if (err) {
        console.log(err);
      }
    }
    );
  } else {
    console.log(err);
  }
});
