#!/usr/bin/node
exports.addmeMaybe = function (number, theFunction) {
  theFunction(++number);
};
