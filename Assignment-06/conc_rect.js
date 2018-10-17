var canvas = document.getElementById("conc_rect")
var conc_rect = canvas.getContext("2d")

/* The concentric rectangles. */

conc_rect.font = "15px Arial";
conc_rect.fillText ("1. Concentric Rectangles", 10, 20);

conc_rect.fillStyle = "#9A031E"
conc_rect.fillRect (50, 30, 500, 240)

setTimeout (() => {
	conc_rect.fillStyle = "#1F2F16"
	conc_rect.fillRect (130, 80, 340, 140)
}, 250);

setTimeout (() => {
	conc_rect.fillStyle = "#97DB4F"
	conc_rect.fillRect (200, 100, 200, 100)
}, 750);