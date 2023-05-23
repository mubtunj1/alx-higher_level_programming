#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${data.statusCode}`);
  }
});
