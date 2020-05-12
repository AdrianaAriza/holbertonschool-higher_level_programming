#!/usr/bin/node
exports.esrever = function (list) {
  const x = list.length;
  const list_n = [];
  for (let i = x; i > 0; i--) {
    list_n.push(list[i]);
  }
  return list_n;
};
