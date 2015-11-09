// 10by10
// Create a 10 X 10 array and randomly fill each cell with "D" or "E"

var xMax = 10;
var yMax = 10;
var z = new Array();

for (var i = 0; i < xMax; i++) {
	z[i] = new Array();
	var possible = "DE";

	for (j = 0; j < yMax; j++) {
		z[i][j] = possible.charAt(Math.floor(Math.random() * possible.length));
	}
}

console.log(z);