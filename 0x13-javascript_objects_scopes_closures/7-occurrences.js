#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  function checkAdult (age) {
    return age === searchElement;
  }

  return list.filter(checkAdult).length;
};
