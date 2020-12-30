/* JS Functions & Objects */
"use strict";
console.log('JS Functions & Objects')
const log = console.log;

// Two ways to define a function:
function func() {
	log('func');
}

// Since a function is an object, can also be assigned to variable:
const func2 = function () {
	log('func2');
}


// Closure example
function createCounter() {
	let count = 0;
	return function () {
		count += 1;
		return count;
	}
}

const myCounter = createCounter();
// myCounter();  // this will return an incremented count every time it's called


// setTimeout closure
// Using the function setTimeout(f, interval)

// let's start with var
/*
for (var i = 1; i <= 5; i++) {
	setTimeout(function () {
		log(i);
	}, i * 1000);
}
*/

// Wrapping in an IFFE

for (var i = 1; i <= 5; i++) {
	(function () {
		var j = i; // j is function scoped in the anonymous function
		setTimeout(function () {
			log(j);
		}, i * 1000);
	})();
}


// Using let and block scope

for (let i = 1; i <= 5; i++) {
	// i is block scoped, a new scope is made for each iteration of the for loop
	setTimeout(function () {
		log(i);
	}, i * 1000);
}


//// Objects

const student = {
	name: 'Jimmy',
	year: 2,
	sayName: function() {
		log('My name is ' + this.name + '.')
		// Q: what is the context of this?
		// A: we don't know, until we call it
	}
}

student.sayName();
let mySayName = student.sayName;
//mySayName(); // undefined

// we can get this to work without having
// to explicitly call student.sayName()
// Binding
mySayName = student.sayName;
const boundSayName = mySayName.bind(student)
boundSayName();

// A function can be outside of the object.
// It doesn't matter, since binding only happens at the call-site.
const whatYearAmI = function() {
	log(this.year)
}

const student2 = {
	name: 'Saul',
	year: 3,
	myYear: whatYearAmI,
	nested: {
		name: 'Jane',
		year: 7,
		myYear: whatYearAmI
	}
}

student2.myYear();

const student3 = {
	name: 'Jane',
	year: 7,
	myYear: student2.myYear
}

// What is the binding for the calls below?
student3.myYear()
student3.myYear.bind(student2)();
student3.myYear.call(student2)

student2.nested.myYear();
