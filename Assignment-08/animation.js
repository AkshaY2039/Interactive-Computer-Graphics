/* 
	Interactive Computer Graphics - Assignment 8 - Animation
		Akshay Kumar (CED15I031)
	reference : https://codepen.io/ykob/pen/oeOrJV
		tex.png --- http://ykob.github.io/sketch-threejs/img/sketch/butterfly/tex.png
 */

var _createClass = function () {
	function defineProperties (target, props) {
		for (var i = 0; i < props.length; i++) {
			var descriptor = props[i];descriptor.enumerable = 
								descriptor.enumerable || false;descriptor.configurable = true;
			if ("value" in descriptor) {
				descriptor.writable = true;
				Object.defineProperty(target, descriptor.key, descriptor);
			}
		}
	}
	return function (Constructor, protoProps, staticProps) {
		if (protoProps)
			defineProperties (Constructor.prototype, protoProps);
		if (staticProps)
			defineProperties(Constructor, staticProps);
		return Constructor;
	};
} ();

function _classCallCheck (instance, Constructor) {
	if (!(instance instanceof Constructor)) {
		throw new TypeError ("Cannot call a class as a function");
	}
}

var debounce = function debounce (callback, duration) {
	var timer;
	return function (event) {
		clearTimeout(timer);
		timer = setTimeout (function () {
			callback(event);
		}, duration);
	};
};
  
var SIZE = 280;

var Butterfly = function () {
	function Butterfly (i, texture) {
		_classCallCheck(this, Butterfly);

		this.uniforms = {
			index: {
				type: 'f',
				value: i
			},
			time: {
				type: 'f',
				value: 0
			},
			size: {
				type: 'f',
				value: SIZE
			},
			texture: {
				type: 't',
				value: texture
			}
		};

		this.physicsRenderer = null;
		this.obj = this.createObj ();
	}
	_createClass (Butterfly, 
		[
			{
				key: 'createObj',
				value: function createObj ()
				{
					var geometry = new THREE.PlaneBufferGeometry (SIZE, SIZE / 2, 24, 12);
					var mesh = new THREE.Mesh (
						geometry,
						new THREE.RawShaderMaterial (
							{
								uniforms: this.uniforms,
								vertexShader:
									`attribute vec3 position;
									attribute vec2 uv;

									uniform mat4 modelViewMatrix;
									uniform mat4 projectionMatrix;

									uniform float index;
									uniform float time;
									uniform float size;

									varying vec3 vPosition;
									varying vec2 vUv;

									void main () {
										float flapTime = radians (sin (time * 6.0 - length (position.xy) / size * 2.6 + index * 2.0) * 45.0 + 30.0);
										float hovering = cos (time * 2.0 + index * 3.0) * size / 16.0;
										vec3 updatePosition = vec3 (
											cos (flapTime) * position.x,
											position.y + hovering,
											sin(flapTime) * abs(position.x) + hovering
											);

										vec4 mvPosition = modelViewMatrix * vec4 (updatePosition, 1.0);

										vPosition = position;
										vUv = uv;

										gl_Position = projectionMatrix * mvPosition;
									}`,
								fragmentShader:
									`precision highp float;

									uniform float index;
									uniform float time;
									uniform float size;

									uniform sampler2D texture;

									varying vec3 vPosition;
									varying vec2 vUv;

									// Description : Array and textureless GLSL 2D/3D/4D simplex
									//               noise functions.
									//      Author : Ian McEwan, Ashima Arts.
									//  Maintainer : ijm
									//     Lastmod : 20110822 (ijm)
									//     License : Copyright (C) 2011 Ashima Arts. All rights reserved.
									//               Distributed under the MIT License. See LICENSE file.
									//               https://github.com/ashima/webgl-noise

									vec3 mod289 (vec3 x) {
										return x - floor (x * (1.0 / 289.0)) * 289.0;
									}

									vec4 mod289 (vec4 x) {
										return x - floor (x * (1.0 / 289.0)) * 289.0;
									}

									vec4 permute (vec4 x) {
										return mod289 (((x * 34.0) + 1.0) * x);
									}

									vec4 taylorInvSqrt (vec4 r)
									{
										return 1.79284291400159 - 0.85373472095314 * r;
									}

									float snoise3 (vec3 v)
									{
										const vec2  C = vec2 (1.0/6.0, 1.0/3.0);
										const vec4  D = vec4 (0.0, 0.5, 1.0, 2.0);

										// First corner
										vec3 i  = floor (v + dot (v, C.yyy));
										vec3 x0 =   v - i + dot (i, C.xxx);

										// Other corners
										vec3 g = step (x0.yzx, x0.xyz);
										vec3 l = 1.0 - g;
										vec3 i1 = min (g.xyz, l.zxy);
										vec3 i2 = max (g.xyz, l.zxy);

										//   x0 = x0 - 0.0 + 0.0 * C.xxx;
										//   x1 = x0 - i1  + 1.0 * C.xxx;
										//   x2 = x0 - i2  + 2.0 * C.xxx;
										//   x3 = x0 - 1.0 + 3.0 * C.xxx;
										vec3 x1 = x0 - i1 + C.xxx;
										vec3 x2 = x0 - i2 + C.yyy;	// 2.0 * C.x = 1/3 = C.y
										vec3 x3 = x0 - D.yyy;	// -1.0 + 3.0 * C.x = -0.5 = -D.y

										// Permutations
										i = mod289 (i);
										vec4 p = permute (
													permute (
														permute (
															i.z + vec4(0.0, i1.z, i2.z, 1.0 )
															)
														+ i.y + vec4(0.0, i1.y, i2.y, 1.0 )
														)
													+ i.x + vec4(0.0, i1.x, i2.x, 1.0 )
													);

										// Gradients: 7x7 points over a square, mapped onto an octahedron.
										// The ring size 17*17 = 289 is close to a multiple of 49 (49*6 = 294)
										float n_ = 0.142857142857; // 1.0/7.0
										vec3  ns = n_ * D.wyz - D.xzx;

										vec4 j = p - 49.0 * floor (p * ns.z * ns.z);  //  mod(p,7*7)

										vec4 x_ = floor (j * ns.z);
										vec4 y_ = floor (j - 7.0 * x_);    // mod(j,N)

										vec4 x = x_ * ns.x + ns.yyyy;
										vec4 y = y_ * ns.x + ns.yyyy;
										vec4 h = 1.0 - abs (x) - abs (y);

										vec4 b0 = vec4 (x.xy, y.xy);
										vec4 b1 = vec4 (x.zw, y.zw);

										//vec4 s0 = vec4(lessThan(b0,0.0))*2.0 - 1.0;
										//vec4 s1 = vec4(lessThan(b1,0.0))*2.0 - 1.0;
										vec4 s0 = floor (b0) * 2.0 + 1.0;
										vec4 s1 = floor (b1) * 2.0 + 1.0;
										vec4 sh = -step (h, vec4 (0.0));

										vec4 a0 = b0.xzyw + s0.xzyw * sh.xxyy;
										vec4 a1 = b1.xzyw + s1.xzyw * sh.zzww;

										vec3 p0 = vec3 (a0.xy, h.x);
										vec3 p1 = vec3 (a0.zw, h.y);
										vec3 p2 = vec3 (a1.xy, h.z);
										vec3 p3 = vec3 (a1.zw, h.w);

										// Normalise gradients
										vec4 norm = taylorInvSqrt (
											vec4 (dot (p0,p0), dot (p1,p1), dot (p2, p2), dot (p3,p3))
											);
										p0 *= norm.x;
										p1 *= norm.y;
										p2 *= norm.z;
										p3 *= norm.w;

										// Mix final noise value
										vec4 m = max (0.6 - 
											vec4 (dot (x0,x0), dot (x1,x1), dot (x2,x2), dot (x3,x3)), 
											0.0);
										m = m * m;
										return 42.0 * dot (
											m*m, vec4 (dot (p0,x0), dot (p1,x1), dot (p2,x2), dot (p3,x3))
											);
									}

									vec3 convertHsvToRgb (vec3 c) {
										vec4 K = vec4 (1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
										vec3 p = abs (fract (c.xxx + K.xyz) * 6.0 - K.www);
										return c.z * mix (K.xxx, clamp (p - K.xxx, 0.0, 1.0), c.y);
									}

									void main () {
										vec4 texColor = texture2D (texture, vUv);

										float noise = snoise3 (
											vPosition / vec3 (size * 0.5) + vec3 (0.0, 0.0, time)
											);
										vec3 hsv = vec3 (1.0 + noise * 0.5 + index * 0.7, 0.4, 1.0);
										vec3 rgb = convertHsvToRgb (hsv);

										gl_FragColor = vec4 (rgb, 1.0) * texColor;
									}`,
									depthWrite: false,
									side: THREE.DoubleSide,
									transparent: true
								}
							)
						);
					mesh.rotation.set (-50 * Math.PI / 180, 0, 0);
					return mesh;
				}
			}, 
			{
				key: 'render', 
				value: function render (renderer, time) {
					this.uniforms.time.value += time;
					this.obj.position.z = this.obj.position.z > -900 ? this.obj.position.z - 4 : 900;
				}
			}
		]
	);
	return Butterfly;
} ();

var resolution = {x: 0, y: 0};

var canvas = document.getElementById ('animation');
var renderer = new THREE.WebGLRenderer ({
	antialias: false,
	canvas: canvas
});

var scene = new THREE.Scene ();
var camera = new THREE.OrthographicCamera (-1, 1, 1, -1, 1, 10000);
var clock = new THREE.Clock ();
var loader = new THREE.TextureLoader ();

var vectorTouchStart = new THREE.Vector2 ();
var vectorTouchMove = new THREE.Vector2 ();
var vectorTouchEnd = new THREE.Vector2 ();

var CAMERA_SIZE_X = 640;
var CAMERA_SIZE_Y = 480;

var BUTTERFLY_NUM = 10;
var butterflies = [];

var resizeCamera = function resizeCamera () {
	var x = Math.min (resolution.x / resolution.y / (CAMERA_SIZE_X / CAMERA_SIZE_Y), 1.0) * CAMERA_SIZE_X;
	var y = Math.min (resolution.y / resolution.x / (CAMERA_SIZE_Y / CAMERA_SIZE_X), 1.0) * CAMERA_SIZE_Y;
	camera.left = x * -0.5;
	camera.right = x * 0.5;
	camera.top = y * 0.5;
	camera.bottom = y * -0.5;
	camera.updateProjectionMatrix ();
};

var resizeWindow = function resizeWindow () {
	resolution.x = window.innerWidth;
	resolution.y = window.innerHeight;
	canvas.width = resolution.x;
	canvas.height = resolution.y;
	resizeCamera ();
	renderer.setSize(resolution.x, resolution.y);
};

var render = function render () {
	var time = clock.getDelta ();
	for (var i = 0; i < butterflies.length; i++) {
		butterflies[i].render (renderer, time);
	}
	renderer.render (scene, camera);
};

var renderLoop = function renderLoop () {
	render ();
	requestAnimationFrame (renderLoop);
};

var on = function on () {
	window.addEventListener('resize', debounce (resizeWindow), 1000);
};

var init = function init () {
	resizeWindow ();
	on ();

	renderer.setClearColor (0xeeeeee, 1.0);
	camera.position.set (250, 500, 1000);
	camera.lookAt (new THREE.Vector3 ());

	loader.crossOrigin = 'Anonymous';
	loader.load ('https://raw.githubusercontent.com/AkshaY2039/Interactive-Computer-Graphics/master/Assignment-08/tex.png', function (texture) {
		texture.magFilter = THREE.NearestFilter;
		texture.minFilter = THREE.NearestFilter;

		for (var i = 0; i < BUTTERFLY_NUM; i++) {
			butterflies[i] = new Butterfly (i, texture);
			butterflies[i].obj.position.set (
					((i + 1) % (2)) * i * 50, 
					0, 
					1800 / BUTTERFLY_NUM * i
				);
			scene.add (butterflies[i].obj);
		}
		renderLoop ();
	});
};

init();
