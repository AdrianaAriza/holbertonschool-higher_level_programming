#!/usr/bin/node
class Rentangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    } else {
      ;
    }
  }
}
module.exports = Rentangle;
