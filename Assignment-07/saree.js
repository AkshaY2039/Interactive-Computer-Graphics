/*
	Assignment 7.2 - Saree
		- Akshay Kumar (CED15I031)
*/

main ();

// Start here
function main () {
	const canvas = document.getElementById ('saree');
	const gl_canvas = canvas.getContext ('webgl') || canvas.getContext ('experimental-webgl');
	

	// If we don't have a GL context, give up now

	if (!gl_canvas) {
		alert ('Unable to initialize WebGL_gl_canvas. Your browser or machine may not support it.');
		return;
	}

	// Vertex shader program
	const vsSource = `
		attribute vec4 aVertexPosition;
		attribute vec2 aTextureCoord;

		uniform mat4 uModelViewMatrix;
		uniform mat4 uProjectionMatrix;

		varying highp vec2 vTextureCoord;

		void main (void) {
			gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
			vTextureCoord = aTextureCoord;
		}
	`;

	// Fragment shader program
	const fsSource = `
		varying highp vec2 vTextureCoord;

		uniform sampler2D uSampler;

		void main (void) {
			gl_FragColor = texture2D (uSampler, vTextureCoord);
		}
	`;

	// Initialize a shader program; this is where all the lighting
	// for the vertices and so forth is established.
	const shaderProgram = initShaderProgram (gl_canvas, vsSource, fsSource);

	// Collect all the info needed to use the shader program.
	// Look up which attributes our shader program is using
	// for aVertexPosition, aVevrtexColor and also
	// look up uniform locations.
	const programInfo = {
		program: shaderProgram,
		attribLocations: {
			vertexPosition: gl_canvas.getAttribLocation (shaderProgram, 'aVertexPosition'),
			textureCoord: gl_canvas.getAttribLocation (shaderProgram, 'aTextureCoord'),
		},
		uniformLocations: {
			projectionMatrix: gl_canvas.getUniformLocation (shaderProgram, 'uProjectionMatrix'),
			modelViewMatrix: gl_canvas.getUniformLocation (shaderProgram, 'uModelViewMatrix'),
			uSampler: gl_canvas.getUniformLocation (shaderProgram, 'uSampler'),
		},
	};

	// Here's where we call the routine that builds all the
	// objects we'll be drawing.
	const buffers = initBuffers (gl_canvas);

	const texture = new Array (2);
	texture[0] = loadTexture (gl_canvas, 'https://raw.githubusercontent.com/AkshaY2039/Interactive-Computer-Graphics/master/Assignment-07/fractal-1.png');
	texture[1] = loadTexture (gl_canvas, 'https://raw.githubusercontent.com/AkshaY2039/Interactive-Computer-Graphics/master/Assignment-07/img-2.png');

	var then = 0;

	// Draw the scene repeatedly
	function render (now) {
		drawScene (gl_canvas, programInfo, buffers, texture);

		requestAnimationFrame (render);
	}
	requestAnimationFrame (render);
}

// initBuffers
//
// Initialize the buffers we'll need. For this demo, we just
// have one object -- a simple three-dimensional cube.
function initBuffers (gl_canvas) {

	// Create a buffer for the cube's vertex positions.
	const positionBuffer = gl_canvas.createBuffer ();

	// Select the positionBuffer as the one to apply buffer
	// operations to from here out.
	gl_canvas.bindBuffer (gl_canvas.ARRAY_BUFFER, positionBuffer);

	// Now create an array of positions for the cube.
	const positions = [
		// saree background
		-5.0,	-1.5,	 1.5,
		5.0,	-1.5,	1.5,
		5.0,	1.5,	1.5,
		-5.0,	1.5,	1.5,

		// lower borders
		-5.0,	-1.5,	1.5,
		-5.0,	-1.2,	1.5,
		-2.5,	-1.2,	1.5,
		-2.5,	-1.5,	1.5,

		-2.5,	-1.5,	1.5,
		-2.5,	-1.2,	1.5,
		0.0,	-1.2,	1.5,
		0.0,	-1.5,	1.5,

		0.0,	-1.5,	1.5,
		0.0,	-1.2,	1.5,
		2.5,	-1.2,	1.5,
		2.5,	-1.5,	1.5,

		2.5,	-1.5,	1.5,
		2.5,	-1.2,	1.5,
		5.0,	-1.2,	1.5,
		5.0,	-1.5,	1.5,

		// top borders
		0.0,	1.5,	1.5,
		0.0,	1.2,	1.5,
		2.5,	1.2,	1.5,
		2.5,	1.5,	1.5,

		2.5,	1.5,	1.5,
		2.5,	1.2,	1.5,
		5.0,	1.2,	1.5,
		5.0,	1.5,	1.5,

		// side borders
		5.0,	1.5,	1.5,
		4.6,	1.5,	1.5,
		4.6,	0.0,	1.5,
		5.0,	0.0,	1.5,

		// side borders
		5.0,	0.0,	1.5,
		4.6,	0.0,	1.5,
		4.6,	-1.5,	1.5,
		5.0,	-1.5,	1.5,
	];

	// Now pass the list of positions into WebGL to build the
	// shape. We do this by creating a Float32Array from the
	// JavaScript array, then use it to fill the current buffer.
	gl_canvas.bufferData (gl_canvas.ARRAY_BUFFER, new Float32Array (positions), gl_canvas.STATIC_DRAW);

	// Now set up the texture coordinates for the faces.
	const textureCoordBuffer = gl_canvas.createBuffer ();
	gl_canvas.bindBuffer (gl_canvas.ARRAY_BUFFER, textureCoordBuffer);

	const textureCoordinates = [
		// background cloth
		0.0,	0.0,
		1.0,	0.0,
		1.0,	1.0,
		0.0,	1.0,

		//lower borders
		1.0,	0.0,
		1.0,	1.0,
		0.0,	1.0,
		0.0,	0.0,

		1.0,	0.0,
		1.0,	1.0,
		0.0,	1.0,
		0.0,	0.0,

		1.0,	0.0,
		1.0,	1.0,
		0.0,	1.0,
		0.0,	0.0,

		1.0,	0.0,
		1.0,	1.0,
		0.0,	1.0,
		0.0,	0.0,

		// upper borders
		1.0,	0.0,
		1.0,	1.0,
		0.0,	1.0,
		0.0,	0.0,

		1.0,	0.0,
		1.0,	1.0,
		0.0,	1.0,
		0.0,	0.0,

		// side borders
		1.0,	1.0,
		1.0,	0.0,
		0.0,	0.0,
		0.0,	1.0,

		1.0,	1.0,
		1.0,	0.0,
		0.0,	0.0,
		0.0,	1.0,
	]

	gl_canvas.bufferData (gl_canvas.ARRAY_BUFFER, new Float32Array (textureCoordinates), gl_canvas.STATIC_DRAW);

	// Build the element array buffer; this specifies the indices
	// into the vertex arrays for each face's vertices.
	const indexBuffer = gl_canvas.createBuffer ();
	gl_canvas.bindBuffer (gl_canvas.ELEMENT_ARRAY_BUFFER, indexBuffer);

	// This array defines each face as two triangles, using the
	// indices into the vertex array to specify each triangle's
	// position.
	const indices = [
		0,	1,	2,	    0,	2,	3,	// saree cloth
		4,	5,	6,		4,	6,	7,	// lower border
		8,	9,	10,		8,	10,	11,	// lower border
		12,	13,	14,		12,	14,	15,	// lower border
		16,	17,	18,		16,	18,	19,	// lower border
		20,	21,	22,		20,	22,	23,	// upper border
		24,	25,	26,		24,	26,	27,	// upper border
		28,	29,	30,		28,	30,	31,	// side border
		32,	33,	34,		32,	34,	35,	// side border
	];

	// Now send the element array to GL
	gl_canvas.bufferData (gl_canvas.ELEMENT_ARRAY_BUFFER, new Uint16Array (indices), gl_canvas.STATIC_DRAW);

	return {
		position: positionBuffer,
		textureCoord: textureCoordBuffer,
		indices: indexBuffer,
	};
}

// Initialize a texture and load an image.
// When the image finished loading copy it into the texture.
function loadTexture (gl_canvas, url) {
	const texture = gl_canvas.createTexture ();
	gl_canvas.bindTexture (gl_canvas.TEXTURE_2D, texture);

	// Because images have to be download over the internet
	// they might take a moment until they are ready.
	// Until then put a single pixel in the texture so we can
	// use it immediately. When the image has finished downloading
	// we'll update the texture with the contents of the image.
	const level = 0;
	const internalFormat = gl_canvas.RGBA;
	const width = 1;
	const height = 1;
	const border = 0;
	const srcFormat = gl_canvas.RGBA;
	const srcType = gl_canvas.UNSIGNED_BYTE;
	const pixel = new Uint8Array ([0, 0, 255, 255]);	// opaque blue
	gl_canvas.texImage2D (gl_canvas.TEXTURE_2D, level, internalFormat, width, height, border, srcFormat, srcType,	pixel);

	const image = new Image ();
	image.crossOrigin = "Anonymous";
	image.onload = function () {
		gl_canvas.bindTexture (gl_canvas.TEXTURE_2D, texture);
		gl_canvas.texImage2D (gl_canvas.TEXTURE_2D, level, internalFormat, srcFormat, srcType, image);

		// WebGL1 has different requirements for power of 2 images
		// vs non power of 2 images so check if the image is a
		// power of 2 in both dimensions.
		if (isPowerOf2 (image.width) && isPowerOf2 (image.height)) {
			// Yes, it's a power of 2. Generate mips.
			gl_canvas.generateMipmap (gl_canvas.TEXTURE_2D);
		} else {
			// No, it's not a power of 2. Turn of mips and set
			// wrapping to clamp to edge
			gl_canvas.texParameteri (gl_canvas.TEXTURE_2D, gl_canvas.TEXTURE_WRAP_S, gl_canvas.CLAMP_TO_EDGE);
			gl_canvas.texParameteri (gl_canvas.TEXTURE_2D, gl_canvas.TEXTURE_WRAP_T, gl_canvas.CLAMP_TO_EDGE);
			gl_canvas.texParameteri (gl_canvas.TEXTURE_2D, gl_canvas.TEXTURE_MIN_FILTER, gl_canvas.LINEAR);
		}
	};
	image.src = url;

	return texture;
}

function isPowerOf2 (value) {
	return (value & (value - 1)) == 0;
}

// Draw the scene.
function drawScene (gl_canvas, programInfo, buffers, texture, deltaTime) {
	gl_canvas.clearColor (0.0, 0.0, 0.0, 1.0);	// Clear to black, fully opaque
	gl_canvas.clearDepth (1.0);				// Clear everything
	gl_canvas.enable (gl_canvas.DEPTH_TEST);			// Enable depth testing
	gl_canvas.depthFunc (gl_canvas.LEQUAL);			// Near things obscure far things

	// Clear the canvas before we start drawing on it.
	gl_canvas.clear (gl_canvas.COLOR_BUFFER_BIT | gl_canvas.DEPTH_BUFFER_BIT);

	// Create a perspective matrix, a special matrix that is
	// used to simulate the distortion of perspective in a camera.
	// Our field of view is 45 degrees, with a width/height
	// ratio that matches the display size of the canvas
	// and we only want to see objects between 0.1 units
	// and 100 units away from the camera.
	const fieldOfView = 45 * Math.PI / 180;	 // in radians
	const aspect = gl_canvas.canvas.clientWidth / gl_canvas.canvas.clientHeight;
	const zNear = 0.1;
	const zFar = 100.0;
	const projectionMatrix = mat4.create ();

	// note: glmatrix.js always has the first argument
	// as the destination to receive the result.
	mat4.perspective (projectionMatrix,	fieldOfView, aspect, zNear, zFar);

	// Set the drawing position to the "identity" point, which is
	// the center of the scene.
	const modelViewMatrix = mat4.create ();

	// Now move the drawing position a bit to where we want to
	// start drawing the square.
	mat4.translate (modelViewMatrix, 	// destination matrix
					modelViewMatrix, 	// matrix to translate
					[-0.0, 0.0, -6.0]);	// amount to translate

	// Tell WebGL how to pull out the positions from the position
	// buffer into the vertexPosition attribute
	{
		const numComponents = 3;
		const type = gl_canvas.FLOAT;
		const normalize = false;
		const stride = 0;
		const offset = 0;
		gl_canvas.bindBuffer (gl_canvas.ARRAY_BUFFER, buffers.position);
		gl_canvas.vertexAttribPointer (
			programInfo.attribLocations.vertexPosition, 
			numComponents, 
			type, 
			normalize, 
			stride, 
			offset);
		gl_canvas.enableVertexAttribArray (programInfo.attribLocations.vertexPosition);
	}

	// Tell WebGL how to pull out the texture coordinates from
	// the texture coordinate buffer into the textureCoord attribute.
	{
		const numComponents = 2;
		const type = gl_canvas.FLOAT;
		const normalize = false;
		const stride = 0;
		const offset = 0;
		gl_canvas.bindBuffer (gl_canvas.ARRAY_BUFFER, buffers.textureCoord);
		gl_canvas.vertexAttribPointer (
			programInfo.attribLocations.textureCoord, 
			numComponents, 
			type, 
			normalize, 
			stride, 
			offset);
		gl_canvas.enableVertexAttribArray (programInfo.attribLocations.textureCoord);
	}

	// Tell WebGL which indices to use to index the vertices
	gl_canvas.bindBuffer (gl_canvas.ELEMENT_ARRAY_BUFFER, buffers.indices);

	// Tell WebGL to use our program when drawing
	gl_canvas.useProgram (programInfo.program);

	// Set the shader uniforms
	gl_canvas.uniformMatrix4fv (programInfo.uniformLocations.projectionMatrix, false, projectionMatrix);
	gl_canvas.uniformMatrix4fv (programInfo.uniformLocations.modelViewMatrix, false, modelViewMatrix);

	// Specify the texture to map onto the faces.
	/******************** Applying textures *******************************/
	// Tell WebGL we want to affect texture unit 0
	// applying cloth texture
	gl_canvas.activeTexture (gl_canvas.TEXTURE2);
	gl_canvas.bindTexture (gl_canvas.TEXTURE_2D, texture[2]);
	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 2);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 0;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	// side borders
	gl_canvas.activeTexture (gl_canvas.TEXTURE1);
	gl_canvas.bindTexture (gl_canvas.TEXTURE_2D, texture[1]);
	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 1);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 84;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	// side borders
	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 1);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 96;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	// top and bottom borders
	gl_canvas.activeTexture (gl_canvas.TEXTURE0);
	gl_canvas.bindTexture (gl_canvas.TEXTURE_2D, texture[0]);
	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 0);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 12;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 0);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 24;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 0);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 36;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 0);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 48;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 0);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 60;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}

	gl_canvas.uniform1i (programInfo.uniformLocations.uSampler, 0);
	{
		const vertexCount = 6;
		const type = gl_canvas.UNSIGNED_SHORT;
		const offset = 72;
		gl_canvas.drawElements (gl_canvas.TRIANGLES, vertexCount, type, offset);
	}
}

// Initialize a shader program, so WebGL knows how to draw our data
function initShaderProgram (gl_canvas, vsSource, fsSource) {
	const vertexShader = loadShader (gl_canvas, gl_canvas.VERTEX_SHADER, vsSource);
	const fragmentShader = loadShader (gl_canvas, gl_canvas.FRAGMENT_SHADER, fsSource);

	// Create the shader program
	const shaderProgram = gl_canvas.createProgram ();
	gl_canvas.attachShader (shaderProgram, vertexShader);
	gl_canvas.attachShader (shaderProgram, fragmentShader);
	gl_canvas.linkProgram (shaderProgram);

	// If creating the shader program failed, alert
	if (!gl_canvas.getProgramParameter (shaderProgram, gl_canvas.LINK_STATUS)) {
		alert ('Unable to initialize the shader program: ' + gl_canvas.getProgramInfoLog (shaderProgram));
		return null;
	}

	return shaderProgram;
}

// creates a shader of the given type, uploads the source and
// compiles it.
function loadShader (gl_canvas, type, source) {
	const shader = gl_canvas.createShader (type);

	// Send the source to the shader object
	gl_canvas.shaderSource (shader, source);

	// Compile the shader program
	gl_canvas.compileShader (shader);

	// See if it compiled successfully
	if (!gl_canvas.getShaderParameter (shader, gl_canvas.COMPILE_STATUS)) {
		alert ('An error occurred compiling the shaders: ' + gl_canvas.getShaderInfoLog (shader));
		gl_canvas.deleteShader (shader);
		return null;
	}

	return shader;
}