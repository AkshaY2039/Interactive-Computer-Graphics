#version 300 es
#define attribute in
#define varying out

in vec4 a_position;
out vec4 v_color;

void main(void) {
    gl_Position = a_position;
    v_color = gl_Position * 0.5 + 0.5;
}
