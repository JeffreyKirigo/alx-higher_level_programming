#!/usr/bin/node
const Square = require('./5-Square.js');

class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint(c){
    
  }

}

module.exports = Square;
