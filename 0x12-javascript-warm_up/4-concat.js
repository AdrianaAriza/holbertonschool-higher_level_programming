#!/usr/bin/node
const x = ' is ';
if (!process.argv[2]) {
  process.argv[2] = 'undefined';
}
if (!process.argv[3]) {
  process.argv[3] = 'undefined';
}
console.log(process.argv[2] + x + process.argv[3]);
