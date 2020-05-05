#!/usr/bin/node
const arr = 'C is fun';
let i = 0;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
}
else {
  for (i; i < parseInt(process.argv[2]); i++) {
    console.log(arr);
  }
}
