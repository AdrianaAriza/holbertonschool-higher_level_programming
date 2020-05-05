#!/usr/bin/node
const arr = [];
const len = process.argv.length;
let i = 0;
if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (i = 2; process.argv[i]; i++) {
    arr.push(process.argv[i]);
  }
  arr.sort().reverse();
  i = 0;
  while (arr[i] === arr[i + 1]) {
    i++;
  }
  console.log(arr[i + 1]);
}
