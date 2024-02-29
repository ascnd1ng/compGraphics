import glfw
from OpenGL.GL import *
delta = 0.01
angle = 0.0

def display(window):
    vertices = [
        # верх
        (0, 0, 0),  # Вершина 1
        (1, 0, 0),  # Вершина 2
        (1, 1, 0),  # Вершина 3
        (0, 1, 0),  # Вершина 4

        # низ
        (0, 0, -1),  # Вершина 1
        (1, 0, -1),  # Вершина 2
        (1, 1, -1),  # Вершина 3
        (0, 1, -1),

        (0, 0, 0),  # лево
        (0, 1, 0),
        (0, 1, -1),
        (0, 0, -1),
        #
        (1, 0, 0),  # лево
        (1, 1, 0),
        (1, 1, -1),
        (1, 0, -1),

        #фронт
        (0, 0, 0),
        (1, 0, 0),
        (1, 0, -1),
        (0, 0, -1),

        #бэк
        (0, 1, 0),
        (1, 1, 0),
        (1, 1, -1),
        (0, 1, -1)
    ]
    vertices = [(x / 10, y / 10, z / 10) for x, y, z in vertices]
    colors = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glRotatef(angle, 1, 1, 1)  # вращение  (оси)
    glBegin(GL_QUADS)

    c = 0
    for i in range (0, len(vertices), 4):
        c += 1
        index1, index2, index3, index4 = (i, i + 1, i + 2, i + 3)
        vertex1 = vertices[index1]
        vertex2 = vertices[index2]
        vertex3 = vertices[index3]
        vertex4 = vertices[index4]

        glColor3f(*colors[(i // 8)])
        glVertex3f(*vertex1)
        glVertex3f(*vertex2)
        glVertex3f(*vertex3)
        glVertex3f(*vertex4)

    print(c)
    glEnd()
    glPopMatrix()
    glfw.swap_buffers(window)
    glfw.poll_events()
    angle += delta


def key_callback(window, key, scancode, action,
mods):
    # управляем направлением вращения
    global delta
    global angle
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            delta = -0.01
        if key == glfw.KEY_LEFT:
            delta = 0.01
        if key == glfw.KEY_SPACE:
            delta = 0

def main():
    if not glfw.init():
        return
    window = glfw.create_window(1300, 1000, "Isometric Cube", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()

main()