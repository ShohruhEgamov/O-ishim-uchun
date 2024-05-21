// const tasodifiy = [40, 100, 1, 5, 25, 10, 42, 15, 18, 54, 95, 13]

// document.getElementById("demo").innerHTML = tasodifiy;

// function myFunction() {
// 	for (let i = tasodifiy.length - 1; i > 0; i--) {
// 		let j = Math.floor(Math.random() * (i + 1));
// 		let k = tasodifiy[i];
// 		tasodifiy[i] = tasodifiy[j];
// 		tasodifiy[j] = k;
// 	}
// 	document.getElementById("demo").innerHTML = tasodifiy;
// }


const cars = [
	{ type: "Volvo", year: 2016 },
	{ type: "Saab", year: 2001 },
	{ type: "BMW", year: 2010 }
];

displayCars();

function myFunction() {
	cars.sort(function (a, b) {
		let x = a.type.toLowerCase();
		let y = b.type.toLowerCase();
		if (x < y) { return -1; }
		if (x > y) { return 1; }
		return 0;
	});
	displayCars();
}

function displayCars() {
	document.getElementById("demo").innerHTML =
		cars[0].type + " " + cars[0].year + "<br>" +
		cars[1].type + " " + cars[1].year + "<br>" +
		cars[2].type + " " + cars[2].year;
}