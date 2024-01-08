#!/usr/bin/node
const args = process.argv;

add(args[2], args[3]);

function add(a, b) {
    console.log(parseInt(a) + parseInt(b));
}
