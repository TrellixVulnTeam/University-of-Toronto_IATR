/* E3 app.js */
'use strict';

const log = console.log
const yargs = require('yargs').option('addRest', {
    type: 'array' // Allows you to have an array of arguments for particular command
  }).option('addResv', {
    type: 'array'
  }).option('addDelay', {
    type: 'array'
  })

const reservations = require('./reservations');

// datetime available if needed
const datetime = require('date-and-time')
require('date-and-time/plugin/meridiem')
datetime.plugin('meridiem')


const yargs_argv = yargs.argv
//log(yargs_argv) // uncomment to see what is in the argument array

if ('addRest' in yargs_argv) {
	const args = yargs_argv['addRest']
	const rest = reservations.addRestaurant(args[0], args[1]); //args[0] is name, args[1] is description
	if (rest.length > 0) {
		/* complete */
		log('Added restaurant' + args[0] + '.')
	} else {
		/* complete */
		log('Duplicate restaurant not added.')
	}
}

if ('addResv' in yargs_argv) {
	const args = yargs_argv['addResv']
	const resv = reservations.addReservation(args[0], args[1], args[2]);

	// Produce output below
	log("Added reservation at " + resv)
}

if ('allRest' in yargs_argv) {
	const restaurants = reservations.getAllRestaurants(); // get the array

	// Produce output below
	restaurants.map(info => log(info));
}

if ('restInfo' in yargs_argv) {
	const restaurants = reservations.getRestaurantByName(yargs_argv['restInfo']);

	// Produce output below
	if (restaurants != {}){
		log(restaurants['name'] + ': ' + restaurants['description'] + ' - ' + restaurants['numReservations'] + ' active reservations')
	}else{
		log('there is no such restaurant')
	}
}

if ('allResv' in yargs_argv) {
	const restaurantName = yargs_argv['allResv']
	const reservationsForRestaurant = reservations.getAllReservationsForRestaurant(restaurantName); // get the arary

	// Produce output below
	reservationsForRestaurant.map(item => log(`${item['time']}, table for ${item['people']}`))
}

if ('hourResv' in yargs_argv) {
	const time = yargs_argv['hourResv']
	const reservationsForRestaurant = reservations.getReservationsForHour(time); // get the arary

	// Produce output below
	reservationsForRestaurant.map(item => log(`${item['restaurant']}: ${item['time']}, table for ${item['people']}`))
}

if ('checkOff' in yargs_argv) {
	const restaurantName = yargs_argv['checkOff']
	const earliestReservation = reservations.checkOffEarliestReservation(restaurantName);

	// Produce output below
	log(`Checked off reservation on ${earliestReservation['time']}, table for ${earliestReservation['people']}`)
}

if ('addDelay' in yargs_argv) {
	const args = yargs_argv['addDelay']
	const resv = reservations.addDelayToReservations(args[0], args[1]);

	// Produce output below
	resv.map(item => log(`${item['time']}, table for ${item['people']}`))
}

if ('status' in yargs_argv) {
	const status = reservations.getSystemStatus()

	// Produce output below
	log(`Number of restaurants: ${status['numRestaurants']}`);
	log(`Number of total reservations: ${status['totalReservations']}`);
	log(`Busiest restaurant: ${status['currentBusiestRestaurantName']}`);
	log(`System started at: ${status['systemStartTime']}`)

}
