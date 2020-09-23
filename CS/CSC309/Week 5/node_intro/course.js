/* Course selection module */
console.log('Course selection module')

// module.exports =  { courseName: 'csc309' }

// require() will provide our app with the 
// object that is referenced by module.exports:
module.exports = {
	addCourse: function(courseList, course) {
		courseList.push(course)
	},

	removeCourse: function(courseList, course) {
		const i = courseList.indexOf(course)
		courseList.splice(i, 1)
	}
}

