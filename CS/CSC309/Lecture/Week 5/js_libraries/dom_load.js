/* dom content loaded */
"use strict";
const log = console.log
log('Loading DOM Content')

function logId(element) {
	log(element.id)
}

/// The DOM isn't loaded yet, can't find the element
// const myElement = document.querySelector('#myId')
// logId(myElement)

document.addEventListener('DOMContentLoaded', function() {
	const myElement = document.querySelector('#myId')
	logId(myElement)

	/// How can we take a function from within this scope to the global scope?

	// won't be able to see logId2 outside of this scope...
	const logId2 = function(element) {
		log(element.id)
	}

	// ..but can attach to global window object
	window.logId3 = function(element) {
		log(element.id)
	}

})


