#!/usr/bin/node
/**
 * function that imports an array and computes a new array
 */
const importlist = require('./100-data').list;
const newlist = importlist.map((x, i) => x * i);
console.log(importlist);
console.log(newlist);
