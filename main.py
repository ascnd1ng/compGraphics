import glfw
from OpenGL.GL import *
delta = 0.1 # скорость поворота
angle = 0.0 # текущий угол
posx = 0.0
posy = 0.0
size = 0.0

def display(window):
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(0.1,0.1,0.1)
    glVertex2f(posx + size + 0.5,posy + size + 0.5)
    glColor3f(0.35,0.0,0.89)
    glVertex2f(posx - size + -0.5,posy + size + 0.5)
    glColor3f(0.0,1.0,1.0)
    glVertex2f(posx - size + -0.5,posy - size + -0.5)
    glColor3f(0.78,0.23,1.0)
    glVertex2f(posx + size + 0.5,posy - size + -0.5)
    glEnd()
    glPopMatrix()
    angle += delta
    glfw.swap_buffers(window)
    glfw.poll_events()

def key_callback(window, key, scancode, action,
mods):
    # управляем направлением вращения
    global delta
    global angle
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            delta = -0.1
    if key == 263: # glfw.KEY_LEFT
        delta = 0.1



def scroll_callback(window, xoffset, yoffset):
    #управляем размером
    global size
    if (xoffset > 0):
        size -= yoffset/10
    else:
        size += yoffset/10



def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 640, "Lab1", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

main()

