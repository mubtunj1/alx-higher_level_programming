#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasks[todo.userId]) {
        tasks[todo.userId] = 1;
      } else {
        tasks[todo.userId] += 1;
      }
    }
  });
  console.log(tasks);
});
