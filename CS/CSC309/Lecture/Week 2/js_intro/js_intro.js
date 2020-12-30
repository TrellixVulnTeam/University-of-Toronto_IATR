/* JS Intro */
"use strict";

console.log('JS Intro');

// We can declare and define a variable value
var a = 3;
console.log(a)

// variable never declared, we get an error
// console.log(b)

console.log(c) // undefined, not error
var c = 12;

console.log(c)

function f1() {
	var a = 4;
	console.log(a)
}

f1();


var g = 5;
f2(); // function called before definition still works.
function f2() {
	var g = 4;
	console.log(g)
}

function f3() {
	var r = 4;
	console.log(r)
}

f3();
// console.log('Outside f3', r)   // error

// code below won't work with 'use strict' at the top.
// comment out 'use strict' first before running.
/*
function f4() {
	k = 37 // no var
	console.log(k)
}

f4()
console.log('Outside f4', k)


function f5() {
	console.log('In f5', k)
}

f5() // we still get k
*/

// for loop with var
var i = 8;
function forFunc() {
	for (var i = 0; i < 5; i++) {
		console.log(i)
	}
	console.log(i)
}

forFunc()
console.log(i)

// for loop with let
const num = 100;
function logNum() {

	for (let j = 0; j < 4; j++) {
		console.log(num);
	}

}

logNum()
console.log(j)
