#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('No arguments');
} else if (argv.length == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
