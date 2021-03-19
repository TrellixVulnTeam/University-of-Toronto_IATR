/* Node app.js */
const log = console.log
log('Node intro');

// require() is a built-in function that 'imports'
// modules into a variable
const util = require('util')

const s = util.format('%s %s', 'csc', '309')
log(s)

// built-in file system module
const fs = require('fs')
fs.appendFileSync('node.txt', 'appending to file\n')

/// Creting our own module (the module design pattern)
// require() returns module.exports of the module
const course = require('./course')

const courseList = ['csc309', 'csc343']

course.addCourse(courseList, 'csc301')
course.removeCourse(courseList, 'csc343')
log(courseList)

// object destructuring: an easy way to pick off 
// the object properties you specifically want
const { addCourse, removeCourse } = course;
addCourse(courseList, 'csc108')
removeCourse(courseList, 'csc301')
log(courseList)


// a 3rd-party module installed by npm:
const chalk = require('chalk')
log(chalk.blue('Feelin blue'))
log(chalk.blue.bgRed.bold('Hello world'))

////////////////////
/// Arrow functions
// A different way to create function expressions.

// normally:
const square = function(x) {
	return x * x
}

/// arrow function:
// const squareA = (x) => { return x * x }
// const squareA = (x) => x * x 
const squareA = x => x * x 
log(squareA(5))

// no arguments
const noArgs = () => 6
log(noArgs())

// multiple arguments
const multipleArgs = (a, b) => a + b
log(multipleArgs(1, 2))

  
// Be careful: with arrow function, you cannot bind 'this' to objects 
// the way we did before.
const student = {
	name: 'Jimmy',
	sayName: () => log(this.name)
}

student.sayName()  // undefined 
// Functional programming in conflict with Object oriented approach
   // they also can’t be used as a constructor.


// one-line if statements
const a = 0
const b = a ? a : 309
/// same as:
// if (a) {
// 	const b = a;
// } else {
// 	const b = 309;
// }

log(b) // 309






