#!/usr/bin/node
let x;
console.log(x = require('./100-data').list);
console.log(x.map((value, index) => value * index));
