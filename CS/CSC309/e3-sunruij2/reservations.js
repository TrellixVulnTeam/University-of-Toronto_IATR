/* Reservations.js */
'use strict';

const log = console.log
const fs = require('fs');
const datetime = require('date-and-time')
require('date-and-time/plugin/meridiem')
datetime.plugin('meridiem')

const startSystem = () => {

	let status = {};

	try {
		status = getSystemStatus();
	} catch(e) {
		status = {
			numRestaurants: 0,
			totalReservations: 0,
			currentBusiestRestaurantName: null,
			systemStartTime: new Date(),
		}

		fs.writeFileSync('status.json', JSON.stringify(status))
	}

	return status;
}

/*********/


// You may edit getSystemStatus below.  You will need to call updateSystemStatus() here, which will write to the json file
const getSystemStatus = () => {
	//update status json file
	updateSystemStatus();

	const status = fs.readFileSync('status.json')

	return JSON.parse(status)
}

/* Helper functions to save JSON */
// You can add arguments to updateSystemStatus if you want.
const updateSystemStatus = () => {
	const status = {}

	/* Add your code below */
	// Step 1 read restaurant json then update status
	const restaurants = JSON.parse(fs.readFileSync('restaurants.json'))
	status["numRestaurants"] = restaurants.length;

	// Step 2 read reservation json then update status
	const reservations = JSON.parse(fs.readFileSync('reservations.json'))
	status["totalReservations"] = reservations.length;

	// Step 3 find the busiest restaurant name then update status
	let busy_name = null;
	let max = 0;
	for (let index=0; index < restaurants.length; index++){
		if (restaurants[index]['numReservations'] > max){
			max = restaurants[index]['numReservations']
			busy_name = restaurants[index]['name']


		}
	}
	status["currentBusiestRestaurantName"] = busy_name;

	// Step 4 Update system time
	status['systemStartTime'] = new Date();

	fs.writeFileSync('status.json', JSON.stringify(status))
}

const saveRestaurantsToJSONFile = (restaurants) => {
	/* Add your code below */
	fs.writeFileSync('restaurants.json', JSON.stringify(restaurants))
};

const saveReservationsToJSONFile = (reservations) => {
	/* Add your code below */
	fs.writeFileSync('reservations.json', JSON.stringify(reservations))
};

/*********/

// Should return an array of length 0 or 1.
const addRestaurant = (name, description) => {
	// Check for duplicate names

	let restaurants = null;
	// get restaurants
	try {
		restaurants = JSON.parse(fs.readFileSync('restaurants.json'));

	} catch(e) {
		restaurants = [];
	}

	let if_dup = false;

	for (let index=0; index < restaurants.length; index++){
		if (restaurants[index]['name'] == name){
			if_dup = true;
		}
	}

	if (if_dup){
		return [];
	}
	else{
		// if no duplicate names:
		restaurants.push({"name":name, "description":description, "numReservations":0})
		saveRestaurantsToJSONFile(restaurants)

		const restaurant = name; // remove null and assign it to proper value

		return [restaurant];
	}



}

// should return the added reservation object
const addReservation = (restaurant, time, people) => {

	/* Add your code below */
	const restaurants = JSON.parse(fs.readFileSync('restaurants.json'))

	let reservations = null;

	try {
		reservations = JSON.parse(fs.readFileSync('reservations.json'))
	} catch(e) {
		reservations = [];
	}

	reservations.push({"restaurant":restaurant, "time":time, "people":people})
	saveReservationsToJSONFile(reservations)

	// update restaurants json
	for (let index=0; index < restaurants.length; index++){
		if (restaurants[index]['name'] == restaurant){
			restaurants[index]['numReservations'] +=1;
		}
	}
	saveRestaurantsToJSONFile(restaurants)


	const reservation = `${restaurant} on ${time} for ${people} people.`; // remove null and assign it to proper value
	return reservation;

}


/// Getters - use functional array methods when possible! ///

// Should return an array - check to make sure restaurants.json exists
const getAllRestaurants = () => {
	/* Add your code below */
	// get restaurants

	try {
		const restaurants = JSON.parse(fs.readFileSync('restaurants.json'));

		const all_rest_info = restaurants.map(rest => rest['name'] + ': ' + rest['description'] + ' - ' + rest['numReservations'] + ' active reservations')
		return all_rest_info;
	} catch(e) {
		log('restaurants.json does not exist')
	}

};

// Should return the restaurant object if found, or an empty object if the restaurant is not found.
const getRestaurantByName = (name) => {
	/* Add your code below */

	try {
		const restaurants = JSON.parse(fs.readFileSync('restaurants.json'));

		for (let index=0; index < restaurants.length; index++){

			if (restaurants[index]['name'] == name){
				return restaurants[index]
			}
		}
		return {};

	} catch(e) {
		log('restaurants.json does not exist')
	}
};

// Should return an array - check to make sure reservations.json exists
const getAllReservations = () => {
  /* Add your code below */
	try {
		const reservations = JSON.parse(fs.readFileSync('reservations.json'));
		return reservations;

	} catch(e) {
		log('reservations.json does not exist')
	}
};

// Should return an array
const getAllReservationsForRestaurant = (name) => {
	/* Add your code below */
	const reservations = getAllReservations();
	const reservations_for_rest = reservations.filter(r => r['restaurant'] == name);
	const res = reservations_for_rest.sort((a,b) => new Date(a.time) - new Date(b.time));
	return res
};


// Should return an array
const getReservationsForHour = (time) => {
	/* Add your code below */
const reservations = getAllReservations();
const goal_time = new Date(time)
const hour = goal_time.getHours();
goal_time.setHours(hour+1);

const reservations_for_hour = reservations.filter(r => new Date(r['time']) >= new Date(time) && new Date(r['time']) <= goal_time );
const res = reservations_for_hour.sort((a,b) => new Date(a.time) - new Date(b.time));
return res

}

// should return a reservation object
const checkOffEarliestReservation = (restaurantName) => {
	const to_delete = getAllReservationsForRestaurant(restaurantName)[0];

	const reservations = getAllReservations();
	const	after_check_off_reservations = reservations.filter(r =>
		(r['restaurant'] != restaurantName) ||
		(new Date(r['time']).getTime() != new Date(to_delete['time']).getTime()) ||
		(r['people'] != to_delete['people']));

	saveReservationsToJSONFile(after_check_off_reservations)

	try {
		const restaurants = JSON.parse(fs.readFileSync('restaurants.json'));

		for (let index=0; index < restaurants.length; index++){
			if (restaurants[index]['name'] == restaurantName){
				restaurants[index]['numReservations'] -=1;
			}
		}
		saveRestaurantsToJSONFile(restaurants)
	} catch(e) {
		log('no resturants file')
	}

	const checkedOffReservation = to_delete; // remove null and assign it to proper value
 	return checkedOffReservation;
}


const addDelayToReservations = (restaurant, minutes) => {
	// Hint: try to use a functional array method
	const reservations = getAllReservations();

	const update_reservation = reservations.map(rest => {
		if (rest['restaurant'] == restaurant){
			const goal_time = new Date(rest['time'])
			const min = goal_time.getMinutes();
			goal_time.setMinutes(min+minutes);

			return {"restaurant":rest['restaurant'] ,"time": goal_time.toString(), "people":rest['people']};
		}else{
			return rest;
		}
	})

	saveReservationsToJSONFile(update_reservation);
	return getAllReservationsForRestaurant(restaurant);
}

startSystem(); // start the system to create status.json (should not be called in app.js)

// May not need all of these in app.js..but they're here.
module.exports = {
	addRestaurant,
	getSystemStatus,
	getRestaurantByName,
	getAllRestaurants,
	getAllReservations,
	getAllReservationsForRestaurant,
	addReservation,
	checkOffEarliestReservation,
	getReservationsForHour,
	addDelayToReservations
}
