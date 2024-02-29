import glfw
from OpenGL.GL import *
deltaA = 0.0
deltaB = 0.0
alpha = 60
beta = 60

def display(window):
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
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
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(-sz / 2, sz / 2, -sz / 2)
        glVertex3f(-sz / 2, sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, -sz / 2)
        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(-sz / 2, -sz / 2, -sz / 2)
        glVertex3f(sz / 2, -sz / 2, -sz / 2)
        glVertex3f(sz / 2, sz / 2, -sz / 2)
        glVertex3f(-sz / 2, sz / 2, -sz / 2)
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(-sz / 2, -sz / 2, sz / 2)
        glVertex3f(sz / 2, -sz / 2, sz / 2)
        glVertex3f(sz / 2, sz / 2, sz / 2)
        glVertex3f(-sz / 2, sz / 2, sz / 2)
        glEnd()

    global alpha, beta
    glRotatef(alpha, 1, 0, 0)  # вращение  (оси)
    glRotatef(beta, 0, 1, 0)  # вращение  (оси)
    alpha += deltaA
    beta += deltaB
    cube(0.4)

    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action,
mods):
    # управляем направлением вращения
    global deltaA, deltaB
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            deltaA += -0.05
        if key == glfw.KEY_LEFT:
            deltaA += 0.05
        if key == glfw.KEY_SPACE:
            deltaA = 0
            deltaB = 0
        if key == glfw.KEY_A:
            deltaB += - 0.05
        if key == glfw.KEY_D:
            deltaB += 0.05

def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "isometric cube", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    # glfw.set_scroll_callback(window, scroll_callback)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

main()