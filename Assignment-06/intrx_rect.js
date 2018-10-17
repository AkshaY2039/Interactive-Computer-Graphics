var canvas = document.getElementById("intrx_rect")
var intrx_rect = canvas.getContext("2d")

/* The intersecting rectangles. */

intrx_rect.font = "15px Arial";
intrx_rect.fillText ("4. Intersecting Rectangles", 10, 20);

setTimeout (() => {
	intrx_rect.fillStyle = "rgba(255, 212, 160, 0.75)";
	intrx_rect.fillRect(80, 80 , 400, 190);
}, 100);

setTimeout (() => {
	intrx_rect.fillStyle = "rgba(0, 25, 0, 0.5)";
	intrx_rect.fillRect(40, 30, 150, 120);
}, 200);

setTimeout (() => {
	intrx_rect.fillStyle = "rgba(5, 40, 15, 0.25)";
	intrx_rect.fillRect(70, 50 , 180, 120);
}, 150);

setTimeout (() => {
	intrx_rect.fillStyle = "rgba(50, 255, 200, 0.5)";
	intrx_rect.fillRect(50, 120 , 80, 130);
}, 300);

setTimeout (() => {
	intrx_rect.fillStyle = "rgba(150, 12, 60, 0.5)";
	intrx_rect.fillRect(200, 150 , 300, 130);
}, 400);