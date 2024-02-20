#!/usr/bin/node
// script reads and prints the content of a file.

const fs = require('fs');
const path = process.argv[2];
const content = fs.readFileSync(path, 'utf-8');
console.log(content);
