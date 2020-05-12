#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let i = list.length; i > 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
