#!/usr/bin/node
let f = 1;
let n = parseInt(process.argv[2]);
function fact (n, f) {
  return f * n;
}
while (n > 0) {
  f = fact(n, f);
  n--;
}
console.log(f);
