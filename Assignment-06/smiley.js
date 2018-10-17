var canvas = document.getElementById("smiley")
var smiley = canvas.getContext("2d")

/* The smiley */

smiley.font = "15px Arial";
smiley.fillText ("3. Smiley", 10, 20);

/* face outline */
smiley.beginPath ()
smiley.arc (300, 150, 120, 0*Math.PI, 2*Math.PI)
smiley.fillStyle = "#FCFF4B"
smiley.stroke ()
smiley.fill ()

/* left eye */
setInterval (() => {
	smiley.beginPath ()
	smiley.arc (240, 100, 10, 0*Math.PI, 2*Math.PI)
	smiley.fillStyle = "#FFFFFF"
	smiley.stroke ()
	smiley.fill ()
	smiley.beginPath ()
	smiley.arc (240, 103, 7, 0*Math.PI, 2*Math.PI)
	smiley.fillStyle = "#000000"
	smiley.stroke ()
	smiley.fill ()
}, 200);

/* right eye */
setInterval (() => {
	smiley.beginPath ()
	smiley.arc (360, 100, 10, 0*Math.PI, 2*Math.PI)
	smiley.fillStyle = "#FFFFFF"
	smiley.stroke ()
	smiley.fill ()
	smiley.beginPath ()
	smiley.arc (360, 103, 7, 0*Math.PI, 2*Math.PI)
	smiley.fillStyle = "#000000"
	smiley.stroke ()
	smiley.fill ()
}, 300);

/* nose */
setInterval (() => {
	smiley.beginPath ()
	smiley.arc (300, 160, 15, 0*Math.PI, 2*Math.PI)
	smiley.fillStyle = "#DD1C1A"
	smiley.stroke ()
	smiley.fill ()
}, 300);

/* the smile */
setTimeout (() => {
	smiley.beginPath ()
	smiley.arc (300, 150, 80, (3.5*Math.PI)/4, (0.5*Math.PI)/4, true)
	smiley.fillStyle = "#111D4A"
	smiley.stroke ()
}, 700);