var num1 = 2;
var num2 = 4;
var num3 = 6;
var name = "Garvit Joshi";
var Class = 'K18KY';

var average = (num1+num2+num3)/3;

console.clear();

console.log(average);

console.log("Hello! "+name);

console.log("Class: "+Class);

//Camel case(Recomended for JavaScript)
var firstNum;
//Pascal case
var FirstNum;
//Snake case
var first_num;

//Rules for naming JS Variables
// - Name can contain letters, digits, _ and $
// - Names cannot start with digits
// - Names can start with an _ or $
// - Names are case sensitive
// - Names cannot be reserved keyword
/*
Numbers in Java Script
*/
var n1=10;   //Integer
var n2=10.9;  //Decimal Number
console.log(typeof(n1));
console.log(typeof(n2)); //Numbers are in 64 bit floating Point
var n3=15;
var sum=n3+n1+n2;
console.log(sum);
var mul = num3 * num1;
console.log(mul);
console.log(num3/0);
console.log(typeof(num3/0));
console.log("Hello"*5);  //NaN - Not a Number 
console.log(typeof(NaN));

/*
JS Numbers _ Functions
*/
n1="13";
n2="1.9";
//toString() - Takes no. as input and prints string
console.log(num3.toString());
console.log(typeof(num3.toString()));

console.log(parseInt(n1));
console.log(parseInt(n2)); //Returns int if Float is Given
console.log(parseFloat(n2));
console.log(parseInt(name));  //NaN

//toFixed -- takes a floating no and rounds it off to given pos

var fl=87.12345678;
console.log(fl.toFixed());
console.log(fl.toFixed(4));  // rounds to 4 decimal point

/*********************************
 * Output:
4
Hello! Garvit Joshi
Class: K18KY
number
number
35.9
12
Infinity
number
NaN
number
6
string
13
1
1.9
NaN
87
87.1235
**********************************/