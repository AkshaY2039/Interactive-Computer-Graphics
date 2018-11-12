#version 300 es
#define attribute in
#define varying out
precision mediump float;

out vec4 outColor;
uniform vec4 u_color;
in vec4 v_color;

void main(void) {
    outColor = u_color;
}