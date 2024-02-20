#!/usr/bin/node
// script that writes a string to a file

const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];
fs.writeFileSync(path, content, 'utf-8');
