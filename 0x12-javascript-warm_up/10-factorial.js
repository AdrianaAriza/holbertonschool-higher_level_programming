#!/usr/bin/node
let f = 1;
let n = parseInt(process.argv[2]);
while (n > 0) {
  f = f * n;
  n--;
}
console.log(f);
