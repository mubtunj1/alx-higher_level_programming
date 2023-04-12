#!/usr/bin/node
const args = process.argv.slice(2);
const arg1 = args[0];
console.log(arg1 || 'No argument');
