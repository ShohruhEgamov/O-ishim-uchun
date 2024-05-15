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
