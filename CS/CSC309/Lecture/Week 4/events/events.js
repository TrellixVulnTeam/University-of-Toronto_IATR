/* events js */
'use strict'
const log = console.log;
console.log('Events')

let right = false;
function moveCircle(e) {
	const circle = e.target;

	if (!right) {
		circle.style.left = '650px';
		right = true	
	} else {
		circle.style.left = '40px';
		right = false	
	}
}

/// Below makes an event listener in JS if not using HTML onmouseover attribute
//const circle = document.querySelector('#circle')
//circle.addEventListener('mouseover', moveCircle)  // 'mouseover' vs 'onmouseover'



//// Non-blocking code

setTimeout(function () {
	log('0 seconds')
}, 0)

setTimeout(function () {
	log('2 seconds')
}, 2000)

log('After setTimeout')


setTimeout(function () {
	log('3 seconds')
}, 3000)

log('After setTimeout 2')



