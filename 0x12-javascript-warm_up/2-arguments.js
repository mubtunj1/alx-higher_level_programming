#!/usr/bin/node

const args = process.argv.length;
if (args > 2) {
	console.log('Argument found');
}else {
	console.log('No argument');
}
