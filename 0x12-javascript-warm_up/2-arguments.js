#!/usr/bin/node

let args = process.argv.length;
if (args > 2) {
	console.log('Arguments found');
}else if (args === 2) {
	console.log('Argument found');
}else {
	console.log('No argument');
}