#!/usr/bin/node
let arr = 'X';
let i;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < parseInt(process.argv[2]) - 1; i++) {
    arr = arr + 'X';
  }
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(arr);
  }
}
