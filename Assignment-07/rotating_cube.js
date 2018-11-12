/*
 * main.js
 * Copyright (C) 2018 g <g@ABCL>
 *
 * Distributed under terms of the MIT license.
 */
(function() {
	"use strict";
  
	// Get A WebGL context
	/** @type {HTMLCanvasElement} */
	const canvas = document.getElementById("canvas");
	const gl = canvas.getContext("webgl2");
	if (!gl) {
	  return;
	}
  
	loadScript("fs.shader", "fs", "fs");
	loadScript("vs.shader", "vs", "vs");
	const programInfo = twgl.createProgramInfo(gl, ["vs", "fs"]);
	const arrays = {
	  a_position: { numComponents: 3, data: [-0.5, 0, 0, 0.5, 0, 0, 0, 0.5, 0] }
	};
	const bufferInfo = twgl.createBufferInfoFromArrays(gl, arrays);
  
	const uniforms = {
	  u_color: [Math.random(), Math.random(), Math.random(), 1]
	};
  
	twgl.resizeCanvasToDisplaySize(gl.canvas);
	gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);
  
	// Clear the canvas
	gl.clearColor(0, 0, 0, 0);
	gl.clear(gl.COLOR_BUFFER_BIT);
  
	// Tell it to use our program (pair of shaders)
	gl.useProgram(programInfo.program);
  
	twgl.setBuffersAndAttributes(gl, programInfo, bufferInfo);
	twgl.setUniforms(programInfo, uniforms);
	twgl.drawBufferInfo(gl, bufferInfo);
  })();
  