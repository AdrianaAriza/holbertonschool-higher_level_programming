#!/usr/bin/node
const fs = require('fs');
try {
  const fileA = fs.readFileSync(process.argv[2], 'utf8');
  console.log(fileA);
} catch (err) {
  console.error(err);
}
