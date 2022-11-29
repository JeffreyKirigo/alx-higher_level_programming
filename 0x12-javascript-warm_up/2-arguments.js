#!/usr/bin/node
const len = process.argv.length;
if (len < 3) {
  console.log('No argument');
}
if (len == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
