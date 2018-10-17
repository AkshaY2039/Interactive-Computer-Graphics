var canvas = document.getElementById("circles")
var circles = canvas.getContext("2d")

/* Lot of Circles */

circles.font = "15px Arial";
circles.fillText ("2. Lot of Circles", 10, 20);

setTimeout (() => {
	circles.beginPath ()
	circles.arc (85, 75, 30, 0*Math.PI, 2*Math.PI)
	circles.fillStyle = "#F5C1C0"
	circles.stroke ()
	circles.fill ()
}, 200);

setTimeout (() => {
	circles.beginPath ()
	circles.arc (165, 150, 20, 0*Math.PI, 2*Math.PI)
	circles.fillStyle = "#EF9796"
	circles.stroke ()
	circles.fill ()
}, 100);

setTimeout (() => {
	circles.beginPath ()
	circles.arc (80, 170, 40, 0*Math.PI, 2*Math.PI)
	circles.fillStyle = "#E96E6D"
	circles.stroke ()
	circles.fill ()
}, 300);

setTimeout (() => {
	circles.beginPath ()
	circles.arc (245, 190, 35, 0*Math.PI, 2*Math.PI)
	circles.fillStyle = "#E34543"
	circles.stroke ()
	circles.fill ()
}, 150);

setTimeout (() => {
	circles.beginPath ()
	circles.arc (170, 200, 10, 0*Math.PI, 2*Math.PI)
	circles.fillStyle = "#DD1C1A"
	circles.stroke ()
	circles.fill ()
}, 700);

setTimeout (() => {
	circles.beginPath ()
	circles.arc (370, 160, 80, 0*Math.PI, 2*Math.PI)
	circles.fillStyle = "#79100F"
	circles.stroke ()
	circles.fill ()
}, 500);

setTimeout (() => {
	circles.beginPath ()
	circles.arc (250, 70, 50, 0*Math.PI, 2*Math.PI)
	circles.fillStyle = "#290605"
	circles.stroke ()
	circles.fill ()
}, 200);