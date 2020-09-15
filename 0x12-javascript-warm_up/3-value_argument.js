#!/usr/bin/node
const count = process.argv.length;
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
