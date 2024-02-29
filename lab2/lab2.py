import glfw
from OpenGL.GL import *
from math import *
deltaA = 0.0
deltaB = 0.0
alpha = 0
beta = 0

def display(window):
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)  # работа с матрицей проекции (см схему)
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT) # убирает эффект перекрытия обьектов, используется при 3d графике

    phi = radians(45)
    gamma = radians(35.26)

    glMultMatrixf([1, 0, 0, 0,
                   0, 1, 0, 0,
                   0, 0, 1, 0,
                   0.8, 0.8, 0, 1])

    def isometricProjection():
        glMultMatrixf([
            cos(phi), sin(phi)*sin(gamma), -sin(gamma)*cos(gamma), 0,
            0, cos(gamma), sin(gamma), 0,
            sin(phi), -cos(phi)*sin(gamma), cos(phi)*cos(gamma), 0,
            0, 0, 0, 1,
        ])

    isometricProjection()

    def cube(sz):
        glBegin(GL_QUADS)

        glColor3f(0.0, 0.0, 1.0) #blue
        glVertex3f(-sz / 2, -sz / 2, -sz / 2)
        glVertex3f(-sz / 2, sz / 2, -sz / 2)
        glVertex3f(-sz / 2, sz / 2, sz / 2)
        glVertex3f(-sz / 2, -sz / 2, sz / 2)

        glColor3f(1.0, 0.0, 0.0) #red
        glVertex3f(sz / 2, -sz / 2, -sz / 2)
        glVertex3f(sz / 2, -sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, -sz / 2)

        glColor3f(0.0, 1.0, 0.0) #green
        glVertex3f(-sz / 2, -sz / 2, -sz / 2)
        glVertex3f(-sz / 2, -sz / 2, sz / 2)
        glVertex3f(sz / 2, -sz / 2, sz / 2)
        glVertex3f(sz / 2, -sz / 2, -sz / 2)

        glColor3f(1.0, 1.0, 0.0) #yellow
        glVertex3f(-sz / 2, sz / 2, -sz / 2)
        glVertex3f(-sz / 2, sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, -sz / 2)

        glColor3f(0.0, 1.0, 1.0) #light blue
        glVertex3f(-sz / 2, -sz / 2, -sz / 2)
        glVertex3f(sz / 2, -sz / 2, -sz / 2)
        glVertex3f(sz / 2, sz / 2, -sz / 2)
        glVertex3f(-sz / 2, sz / 2, -sz / 2)

        glColor3f(1.0, 0.0, 1.0) #purple
        glVertex3f(-sz / 2, -sz / 2, sz / 2)
        glVertex3f(sz / 2, -sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, sz / 2)
        glVertex3f(-sz / 2, sz / 2, sz / 2)
        glEnd()
    # умножаем на матрицу переноса

    cube(0.1)
    glLoadIdentity()
    glMultMatrixf([1, 0, 0, 0,
                   0, 1, 0, 0,
                   0, 0, 1, 0,
                   -0.5, 0, -0.5, 1])
    global alpha, beta

    phi += + beta
    gamma += + alpha

    isometricProjection()
    cube(0.4)

    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action,
mods):
    # управляем направлением вращения
    global alpha, beta
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_RIGHT:
            alpha += -0.05
        if key == glfw.KEY_LEFT:
            alpha += 0.05
        if key == glfw.KEY_A:
            beta += - 0.05
        if key == glfw.KEY_D:
            beta += 0.05

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "isometric cube", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

main()