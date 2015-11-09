// Print 1-255
// Write a program (sets of instructions) that would print all the numbers from 1 to 255.
// for (var i = 1; i <= 255; i++) {
// 	console.log(i);
// }

// Print odd numbers between 1-255
// Write a program (sets of instructions) that would print all the odd numbers from 1 to 255.
// for (var i = 1; i <= 255; i++) {
// 	if (i % 2 != 0) {
// 		console.log(i);
// 	}
// }

// Print Sum
// Write a program that would print the numbers from 0 to 255 but this time, it would also print the sum of the numbers that have been printed so far. For example, your output should be something like this:

// New number: 0 Sum: 0

// New number: 1 Sum: 1

// New Number: 2 Sum: 3

// New number: 3 Sum: 6

// ...

// New Number: 255 Sum: ___.

// Do NOT use an array to do this exercise.
// var counter = 0;
// for (var i = 0; i <= 255; i++) {
// 	counter = i + counter;
// 	console.log("New number: " , i , " Sum: " , (counter));
// }


// Iterating through an array
// Given an array X, say [1,3,5,7,9,13], write a program that would iterate through each member of the array and print each value on the screen.  Being able to loop through each member of the array is extremely important.
// var myArray = [1,3,5,7,9,13];

// for (var i = 0; i < myArray.length; i++) {
// 	console.log(myArray[i]);
// }

// Find Max
// Write a program (sets of instructions) that takes any array and prints the maximum value in the array. Your program should also work with a given array that has all negative numbers (e.g. [-3, -5, -7]), or even a mix of positive numbers, negative numbers and zero.
// var myArray = [-2, -1, 0, 30, 54, 2, 0];
// var max = myArray[0];

// for (var i = 0; i < myArray.length; i++) {
// 	if (myArray[i] >= max) {
// 		max = myArray[i];
// 	} 
// }
// console.log(max);

// Get Average
// Write a program that takes an array, and prints the AVERAGE of the values in the array. For example for an array [2, 10, 3], your program should print an average of 5. Again, make sure you come up with a simple base case and write instructions to solve that base case first, then test your instructions for other complicated cases. You can use a count function with this assignment.
// var myArray = [2, 4, 10];
// var sum = 0;
// var len = myArray.length;

// for (var i = 0; i < len; i++) {
// 	sum = sum + myArray[i];
// }

// console.log(sum/len);

// Array with Odd Numbers
// Write a program that creates an array 'Y' that contains all the odd numbers between 1 to 255. When the program is done, 'y' should have the value of [1, 3, 5, 7, ... 255].
// var y = [];
// for (var i = 1; i <= 255; i++) {
// 	if (i % 2 != 0) {
// 		y.push(i);
// 	}
// }
// console.log(y);


// Greater Than y
// Write a program that takes an array and returns the number of values in that array whose value is greater than a given value y. For example if array = [1, 3, 5, 7] and y = 3, after your program is run it will print 2 (since there are two values in the array that are greater than 3).
// var myArray = [1,3,4,6,7];
// var y = 2;
// var count = 0;

// for (var i = 0; i < myArray.length; i++) {
// 	if (myArray[i] > y) {
// 		count++;
// 	}
// }
// console.log(count);

// Square the values
// Given any array x, say [1, 5, 10, -2], create an algorithm (sets of instructions) that multiplies each value in the array by itself.  When the program is done, the array x should have values that have been squared, say [1, 25, 100, 4].
// var myArray = [1, 5, 10, -2];
// for (var i = 0; i < myArray.length; i++) {
// 	myArray[i] = myArray[i] * myArray[i];
// }
// console.log(myArray);

// Eliminate Negative Numbers
// Given any array x, say [1, 5, 10, -2], create an algorithm that replaces any negative number with the value of 0.  When the program is done, x should have no negative values, say [1, 5, 10, 0].
// var myArray = [1, 5, 10, -2];
// for (var i = 0; i < myArray.length; i++) {
// 	if (myArray[i] < 0) {
// 		myArray[i] = 0;
// 	}
// }
// console.log(myArray);

// Max, Min, and Average 
// Given any array x, say [1, 5, 10, -2], create an algorithm that prints the maximum number in the array, the minimum value in the array, and the average of the values in the array. 
// var myArray = [1, 5, 10, -2];
// var max = myArray[0];
// var min = myArray[0];
// var sum = 0;
// var len = myArray.length;

// for (var i = 0; i < len; i++) {
// 	if (myArray[i] >= max) {
// 		max = myArray[i];
// 	}

// 	if (myArray[i] <= min) {
// 		min = myArray[i];
// 	}

// 	sum = myArray[i] + sum;
// 	var avg = sum/len;
// }
// console.log(max, min, avg);


// Shifting the values in the array
// Given any array x, say [1, 5, 10, 7, -2], create an algorithm that shifts each number by one to the front.  For example, when the program is done, an x of [1, 5, 10, 7, -2] should become [5, 10, 7, -2, 0].
// var x = [1, 5, 10, 7, -2];
// x.shift();
// x.push(0);
// console.log(x);


// Number to string
// Write a program that takes an array of numbers and replaces any negative number with the string 'Dojo'.  For example if array x is initially [-1, -3, 2], after your program is done that array should be ['Dojo', 'Dojo', 2].
// var myArray = [-3, -1, 4, 2, -4];
// for (var i = 0; i < myArray.length; i++) {
// 	if (myArray[i] < 0) {
// 		myArray[i] = "Dojo";
// 	}
// }
// console.log(myArray);



