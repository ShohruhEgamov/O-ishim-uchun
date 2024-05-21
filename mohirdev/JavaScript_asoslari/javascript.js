'use strict';
function Salomlashish() {
	document.getElementById("salom").innerHTML = "Salom bu yerda nima qilayapsan"
}

function Alikolish() {
	document.getElementById("salom").style.display = 'none'
}

// window.alert(5 + 6)
// alert(5 + 10)

{
	let x, y, z;
	x = 6;
	y = 6;
	z = x + y;
	document.getElementById("bayonot").innerHTML = "The value of z is " + z + ".";
}

function yana_Ismla() {
	document.getElementById("demo1").innerHTML = "Salom Shohruh!";
	document.getElementById("demo2").innerHTML = "Yaxshimisiz";
}

document.getElementById("raqam").innerHTML = 10.50;
document.getElementById("son").innerHTML = (5 + 6) * 10;

/* The code below will change
the heading with id = "myH"
and the paragraph with id = "myP"
in my web page:*/


{
	x = 10;
	y = 6;
	z = x + y;
	document.getElementById('ozgaruvchi').innerHTML = "Bu yerdan ozgaruvchi: " + z;
}


{
	var x = 2;
	// Here x is 2
	var x = 10;
	// Here x is 10

	// Here x is 2
	document.getElementById("elon").innerHTML = x;
}

//                                                                JavaScript Const

{
	const cars = [" Saab", " Volvo ", " BMW"];
	cars[1] = " Tayotta";
	cars.push(" Lasetti");
	document.getElementById("moshina").innerHTML = cars;


	const car = { type: "Lasetti", model: "500", color: "white" }
	// car.color = "black";
	car.owner = "Johnson";
	document.getElementById("ranglar").innerHTML = "Bu o'zgargan " + car.color;
}


//                                                                JavaScript operatorlari

{
	let harf = 5;
	let harf2 = 8;
	let natija = harf > harf2;
	let harf4 = "G";
	let harf3 = "J";
	let natija2 = harf < harf2;
	document.getElementById("operator").innerHTML = "Bu yerda A harf B dan katta " + natija;
	document.getElementById("harflar").innerHTML = "Bu yer'da A harf B dan katta " + natija2;
}


//                                                                 JavaScript arifmetikasi

{

	x = 11;
	document.getElementById("arifmet").innerHTML = x ** 2;
	x = 5;
	document.getElementById("arifmet1").innerHTML = Math.pow(x, 2);
}


//                                                                 JavaScript Data Types
let b = BigInt("123456789012345678901234567890");
document.getElementById("bigint").innerHTML = b;

const cars = ["Saab", "Volvo", "BMW"];

document.getElementById("massiv").innerHTML = cars[1];

const person = {
	firstName: "Shohruh",
	lastName: "Egamov",
	yosh: 23,
	kozRangi: "black"
};

document.getElementById("objekt").innerHTML = person.firstName + " u " + person.yosh +
	" yoshga kirdi. Familyasi " + person.lastName;

// document.getElementById("taypeof").innerHTML =
// 	typeof "" +
// 	typeof "Shoh" +
// 	typeof "Egamov";

document.getElementById("taypeof").innerHTML =
	typeof "" + "<br>" +
	typeof "John" + "<br>" +
	typeof "John Doe" + "<br>" +
	typeof 0 + "<br>" +
	typeof 314 + "<br>" +
	typeof 3.14 + "<br>" +
	typeof (3) + "<br>" +
	typeof (3 + 4);

let car;
document.getElementById("undefn").innerHTML = typeof car;

//                                                                 JavaScript Functions

// function name(parameter1, parameter2, parameter3) {
// 	// code to be executed
//   }

function myFunction(p1, p2) {
	return p1 ** p2;
}

let natija = myFunction(4, 5);
document.getElementById("function").innerHTML = natija;

function buCelsius(f) {
	return (f - 32) * 5 / 9;
}


let lakal = "Malumot: " + typeof masNomi;
document.getElementById("lokal").innerHTML = lakal;

function mashinaNomi() {
	let masNomi = "Lasetti";
	let lakal = "Ichidagi: " + typeof masNomi + " " + masNomi;
	document.getElementById("lokal1").innerHTML = lakal.length;
	document.getElementById("lokal1").innerHTML = lakal;
}
mashinaNomi();


//                                                                 JavaScript ob'ektlari

const shaxs = {
	ism: "Shohruh",
	familya: "Egamov",
	id: 1221,
	toliqIsm: function () {
		return this.ism + " " + this.familya;
	}
}

document.getElementById("thisUsuli").innerHTML = shaxs.toliqIsm() + " Bu odam " +
	shaxs.ism + " Uning Familyasi " + shaxs.familya + " ID raqami " + shaxs.id;
document.getElementById("thisUsuli1").innerHTML = "Bu odam " + shaxs.ism;


//                                                                 JavaScript Events

let s = "John";
let c = new String("John");

document.getElementById("stri").innerHTML = typeof s + "<br>" + typeof c;


//                                                                 JavaScript string usullari

// var stringj = "HELLO WORD";
// document.getElementById("strd").innerHTML = stringj.charAt(1);

// var textar = "HELLO WORLD";
// document.getElementById("strd").innerHTML = textar.charAt(0);

// let codee = "SHOHRUH";
// document.getElementById("strd1").innerHTML = textar.charCodeAt(0);

// const codee = "SHOHRUH";
// let leter = codee.at(2);
// document.getElementById("strd1").innerHTML = leter;

// const text = "salom dunyo";
// let salom = text.at(6);
// document.getElementById("header").innerHTML = salom;
// console.log(text)

// let text = "salom dunyo";
// document.getElementById("header").innerHTML = text[1];
// console.log(text)

// let text = "olma, banan, anor";
// let part = text.slice(6,12);
// document.getElementById("header").innerHTML = part;               //slice()satrning bir qismini chiqaradi va chiqarilgan qismini yangi qatorga qaytaradi.
// console.log(text)

// let str = "Apple, Banana, Kiwi";
// document.getElementById("header").innerHTML = str.substring(7,13);
// console.log(text)

// let str = "Apple, Banana, Kiwi";
// document.getElementById("header").innerHTML = str.substr(7,7);
// console.log(text)

// function myFunction() {
// 	let text = document.getElementById("header").innerHTML;
//   document.getElementById("header").innerHTML = text.toUpperCase();
//   }
//   console.log(text)

// function myFunction() {
// 	let text = document.getElementById("header").innerHTML;
// 	document.getElementById("header").innerHTML = text.toLowerCase();
//   }
//   console.log(text)

// let text1 = "Shoxrux";
// let text2 = "Egamov";
// let text3 = "Shuxraat o'g'li";
// let text4 = text1.concat(" ",text2," ",text3)
// document.getElementById("header").innerHTML = text4;

// console.log(text)


// let text1 = "    Shoxrux    ";
// let text2 = text1.trim();

// document.getElementById("header").innerHTML = "Boshlangiz uzunlik: " +
// text1.length + "<br>Keyingi uzunlik: " + text2.length;

// console.log(text)

// let text = "1236";
// text = text.padStart(4,"X")
// document.getElementById("header").innerHTML = text;

// console.log(text)

// let num = 5;
// let text = num.toString();
// document.getElementById("header").innerHTML = text.padStart(4,"x");
// document.getElementById("header").innerHTML = text.padEnd(4,"x");

// console.log(text)

// let text = "SALOM ";
// let natija = text.repeat(2);

// document.getElementById("header").innerHTML = natija;

// console.log(text)

// function myFunction() {
// 	let text = document.getElementById("demo").innerHTML;
// 	document.getElementById("demo").innerHTML =
// 	text.replace(/Microsoft/g,"W3Schools");
//   }

// function myFunction() {
// 	let text = document.getElementById("demo").innerHTML;
// 	document.getElementById("demo").innerHTML =
// 	text.replace(/MICROSOFT/i,"W3Schools");
//   }

// let text = "I love cats. Cats are very easy to love. Cats are very popular."
// text = text.replaceAll("Cats","Dogs");
// text = text.replaceAll("cats","dogs");
// document.getElementById("demo").innerHTML = text;
// console.log(text)


// let text = "a,b,s,d,e,f";
// const menHaq = text.split("s");

// document.getElementById("demo").innerHTML = menHaq[0];
// console.log(text)


//                                                                 JavaScript string qidiruvi

// let text = "Salom shohruh men dasturchiman";
// let index = text.indexOf("dasturchiman");

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "Salom shohruh men dasturchiman men";
// let index = text.lastIndexOf("men");

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "Please locate where 'locate' occurs!";
// let index = text.lastIndexOf("locate", 15);

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "Please locate where 'locate' occurs!";
// let index = text.search("where");

// document.getElementById('header').innerHTML = index;
// console.log(text)

// let text = "The rain in SPAIN stays mainly in the plain";
// const myArr = text.match("in");

// document.getElementById('header').innerHTML = myArr.length + " " + myArr;
// console.log(text)

// let text = "The rain in  stays mainly in the plain";
// const myArr = text.match(/ain/gi);

// document.getElementById('header').innerHTML = myArr.length + " " + myArr;
// console.log(text)

// let text = "I love cats. Cats are very easy to love. Cats are very";
// const iterator = text.matchAll("Cats");

// document.getElementById('header').innerHTML = Array.from(iterator);
// console.log(text)

// let text = "I love cats. Cats are very easy to love. Catsd are very popular.";
// const iterator = text.matchAll(/Cats/gi);

// document.getElementById('header').innerHTML = Array.from(iterator);
// console.log(text)

// let text = "Hello world, welcome to the universe.";
// document.getElementById('header').innerHTML = text.includes("welcom");
// console.log(text)

// let text = "Hello world, welcome to the universe.";
// document.getElementById('header').innerHTML = text.startsWith("Hello");
// console.log(text)

// let text = "Hello world, welcome to the universe.";
// document.getElementById('header').innerHTML = text.endsWith("universe.");
// console.log(text)

//                                                                 JavaScript shablon satrlari

// let ism = "Shohruh";
// let familya = "Egamov";

// let text = `Salom ${ism} ${familya} yaxshimisiz.`
// document.getElementById('header').innerHTML = text.endsWith(".");
// console.log(text)

// let son = 10;
// let kurs = 0.25;

// let text = `Summa ${(son * (1 + kurs)).toFixed(2)}`
// document.getElementById('header').innerHTML = text.endsWith(".");
// console.log(text)


// let header = "Shohruhbek";
// let tags = ["Birinchi", "Ikkinchi", "Uchinchi"];

// let html = `<h2>${header}<h2><ul>`;
// for (const x of tags) {
// 	html += `<<li>${x}</li>`
// }

// html += `</ul>`;
// document.getElementById('header').innerHTML = html;
// console.log(text)

// let myNumber = 2;
// let txt = "";
// while (myNumber != Infinity) {
//    myNumber = myNumber * myNumber;
//    txt = txt + myNumber + "<br>";
// }
// document.getElementById("header").innerHTML = txt;
// console.log(header)


//                                                                 JavaScript BigInt

// let x = Number.MIN_SAFE_INTEGER;

// document.getElementById('header').innerHTML = x


// console.log(header)


// document.getElementById('header').innerHTML = Number.isInteger(10) + "<br>" + Number.isInteger(10.5)


// console.log(header)


//                                                                 JavaScript raqamlari usullari

// let x = 123;
// document.getElementById("header").innerHTML =
// 	x.toPrecision() + "<br>" +
// 	(123).toString() + "<br>" +
// 	(100 + 23).toString();

// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.toExponential() + "<br>" +
// 	x.toExponential(2) + "<br>" +
// 	x.toExponential(6);

// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.toFixed(0) + "<br>" +
// 	x.toFixed(2) + "<br>" +
// 	x.toFixed(4) + "<br>" +
// 	x.toFixed(6);

// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.toPrecision() + "<br>" +
// 	x.toPrecision(2) + "<br>" +
// 	x.toPrecision(4) + "<br>" +
// 	x.toPrecision(6);


// console.log(header)

// let x = 9.656;
// document.getElementById("header").innerHTML =
// 	x.valueOf() + "<br>" +
// 	(123).valueOf() + "<br>" +
// 	(100 + 23).valueOf();


// console.log(header)

// document.getElementById("header").innerHTML =
//   parseInt("-10") + "<br>" +
//   parseInt("-10.33") + "<br>" +
//   parseInt("10") + "<br>" +
//   parseInt("10.33") + "<br>" +
//   parseInt("10 6") + "<br>" +
//   parseInt("10 years") + "<br>" +
//   parseInt("years 10");

// console.log(header)
// -10
// -10
// 10
// 10
// 10
// 10
// NaN


//                                                                 JavaScript raqamlari xususiyatlari

// const mevalar = ["Olma", "Nok", "Anor", "Behi"];
// let meUzunlik = mevalar.length;

// let text = "<ul>";
// for (let i = 0; i < meUzunlik; i++) {
//   text += "<li>" + mevalar[i] + "</li>";
// }
// text += "</ul>";

// document.getElementById("header").innerHTML = text;
// console.log(header)




// const mevalar = ["Olma", "Nok", "Anor", "Behi"];

// let text = "<ul>";
// mevalar.forEach(myFunks);
// text += "</ul>";

// document.getElementById("header").innerHTML = text;

// function myFunks(value){
//   text += "<li>" + value + "</li>";
// }
// console.log(header)




// const fruits = ["Banana", "Orange", "Apple"];
// fruits[6] = "Lemon";

// let fLen = fruits.length;
// let text = "";
// for (i = 0; i < fLen; i++) {
//   text += fruits[i] + "<br>";
// }

// document.getElementById("header").innerHTML = text;
// console.log(header)


// var fruits = ["Banana", "Orange", "Apple"];
// document.getElementById("demo").innerHTML = fruits instanceof Array;

// const fruits = ["Banana", "Orange", "Apple"];
// document.getElementById("demo").innerHTML = Array.isArray(fruits);

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// document.getElementById("header").innerHTML = fruits.join(" * ");

// // Log to console
// console.log(fruits)


// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// fruits.push("Kivi")
// document.getElementById("header").innerHTML = fruits;

// // Log to console
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// document.getElementById("header").innerHTML = fruits;
// document.getElementById("header").innerHTML = fruits.pop();
// // Log to console
// console.log(fruits)

// const fruits = ["Banana", "Orange", "Apple", "Mango"];
// document.getElementById("header").innerHTML = fruits;
// document.getElementById("header").innerHTML = fruits.shift();
// // Log to console
// console.log(fruits)


// const meva = ["Banana", "Orange", "Apple", "Mango"]
// // Log to console
// console.log(meva)


// let arr = [];

// console.log(arr instanceof Array); // true
// console.log(arr instanceof Object); // true
// console.log(Array.isArray(arr)); // true
// console.log(Object.prototype.toString.call(arr) === '[object Array]');

// const meva = ["apple", "banana", "cherry"];
// meva.forEach(function(narsa, son){
// 	console.log(son, narsa)
// })

// function Mosh(raqam, rusum) {
// 	this.raqam = raqam;
// 	this.rusum = rusum;
// }
// let myCar = new Mosh('Toyota', 'Corolla');

// console.log(myCar instanceof Mosh)

// let arr = [];

// console.log(arr instanceof Array); // true
// console.log(arr instanceof Number); // false
// console.log(Array.isArray(arr)); // true
// console.log(Object.prototype.toString.call(arr) === '[object Array]'); // true

// const user = {
// 	name: "ali",
// 	sayName: function(){
// 		const inner = () => {
// 			console.log(this.name);
// 		};
// 		inner();
// 	}
// };
// user.sayName();

// let fruits = ["Olma", "Banan", "Apelsin"];
// let result = fruits.join(", ");
// console.log(result); // "Olma, Banan, Apelsin"

// let numbers = [1, 2, 3, 4, 5];
// let result = numbers.join(" ");
// console.log(result); // "12345"


// let params = ["name=John", "age=30", "city=NewYork"];
// let queryString = params.join(" ");
// console.log(queryString); // "name=John&age=30&city=NewYork"

// let stack = [3, 4, 5, 1, 2,];
// while (stack.length > 2) {
//   let item = stack.pop();
//   console.log(item);
// }
// 5
// 4
// 3
// 2
// 1

// let sonlar = ["Birinchi"];
// sonlar.unshift("Ikkinchi");
// sonlar.unshift("Uchinchi");
// console.log(sonlar); // ["Uchinchi", "Ikkinchi", "Birinchi"]


// const myObj = {
// 	name: "John",
// 	age: 30,
// 	myCars: {
// 	  car1: "Ford",
// 	  car2: "BMW",
// 	  car3: "Fiat"
// 	}
//   }
//   let a = myObj.myCars.car2;
//   console.log(a)

// const fruits = ["Apple", "Orange", "Apple", "Mango"];
// let position = fruits.indexOf("Orange") + 1;

// let meva = "Apple is found in position " + position;
// console.log(meva)

// const numbers = [4, 9, 16, 25, 29];
// let first = numbers.find(myFunction);

// function myFunction(value, index, array) {
// 	return value > 18;
// }

// const meva = ["Banana", "Orange", "Apple", "Mango"]
// meva.sort()
// console.log(meva)

// const meva = ["Banana", "Orange", "Apple", "Mango"];
// meva.reverse()
// console.log(meva)

// const meva = ["Banana", "Orange", "Apple", "Mango"];
// meva.sort()
// meva.reverse()

// console.log(meva)

// const months = ["Jan", "Feb", "Mar", "Apr"];
// const reversed = months.toReversed();
// console.log(reversed);
// console.log(months);

// const points = [40, 100, 1, 5, 25, 10];
// points.sort(function(a, b){return a - b});
// console.log(points);

// const points = [40, 100, 1, 5, 25, 10];
// points.sort(function (a, b) {
// 	return a - b;
// });
// console.log(points);


