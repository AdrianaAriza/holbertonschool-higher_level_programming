#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    [this.width, this.height] = [w, h];
    this.print = function () {
      for (let x = 0; x < h; x++) {
        console.log('X'.repeat(w));
      }
    };
  }
}
module.exports = Rectangle;
