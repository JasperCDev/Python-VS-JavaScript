


/*--------------- JAVASCRIPT DATA TYPES ---------------
------------------------------------------------------ */


// var string = "string";
// console.log(string + ' is ' + typeof string);

// var number = 1;
// console.log(number + ' is ' + typeof number);

// var number = 1.4;
// console.log(number + ' is ' + typeof number);

// var boolean = true;
// console.log(boolean + ' is ' + typeof boolean);

// var array = [];
// console.log(JSON.stringify(array) + ' is ' + typeof array);

// var obj = {};
// console.log(JSON.stringify(obj) + ' is ' + typeof obj);

// var falsey = null;
// console.log(falsey + ' is ' + null);


/*----------------   JAVASCRIPT CONDITIONALS -------------
----------------------------------------------------------*/


/*---------------PART ONE --------------------------------*/

// var num1 = 1
// var num2 = 2

// if (num1 === num2) {
//   console.log(num1 + ' is equal to ' + num2);
// }

// if (num1 !== num2) {
//   console.log(num1 + ' is not equal to ' + num2);
// }

// if (num1 < num2) {
//   console.log(num1 + ' is less than ' + num2);
// }

/*---------------PART TWO --------------------------------*/

// var variable = 'string'

// if (typeof variable === 'number') {
//   console.log('variable is type number');
// } else if (typeof variable === 'string') {
//   console.log('variable is type string');
// } else {
//   console.log('variable is not type string or type number');
// }


/* ------------------ JAVASCRIPT FOR LOOPS ---------------
----------------------------------------------------------*/


// var arr = ['JavaScript', 'Python', 'Jasper', 'Tim', 'Jay'];

// //////////////////////////
// for (var string of arr) {
//   console.log(string);
// }

// //////////////////////////////////////
// for (var i = 0; i < arr.length; i++) {
//   console.log(i);
// }


/*-------------JAVASCRIPT FUNCTIONS-------------------------
----------------------------------------------------------*/


// function add(a, b) {
//   return a + b;
// }

// console.log(add(1, 2));


/*-------------ROCK PAPER SCISSORS EXAMPLE------------------
----------------------------------------------------------*/


// function rockPaperScissors(n) {
//   var permutations = [];
//   var plays = ['R', 'P', 'S'];
//   function loop(string) {
//     if (string.length === n) {
//       permutations.push(string);
//       return;
//     }
//     for (var play of plays) {
//       loop(string + play);
//     }
//   }
//   loop('');
//   return permutations;
// };


// console.log(rockPaperScissors(3));
