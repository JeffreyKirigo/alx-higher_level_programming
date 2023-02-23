#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      let space = '';
      for (let j = 1; j <= this.width; j++) {
        space += '#';
      }
      console.log(space);
    }
  }
}

module.exports = Rectangle;
