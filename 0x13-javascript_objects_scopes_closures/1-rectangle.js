#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    [this.width, this.height] = [w, h];
    Rectangle.print = function () {
      for (x = 0; x < h; x++){
        console.log('X'* w);
      }
    }
  }
}
module.exports = Rectangle;
