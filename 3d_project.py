import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

xrot, yrot = 0.0, 0.0
ambient = (1.0, 1.0, 1.0, 1)
greencolor = (0.2, 0.8, 0.0, 0.8)
treecolor = (0.9, 0.6, 0.3, 0.8)
lightpos = (1.0, 1.0, 1.0)

def init():
    global ambient, lightpos

    glClearColor(0.5, 0.5, 0.5, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

def key_callback(window, key, scancode, action, mods):
    global xrot, yrot

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            xrot -= 2.0
        elif key == glfw.KEY_DOWN:
            xrot += 2.0
        elif key == glfw.KEY_LEFT:
            yrot -= 2.0
        elif key == glfw.KEY_RIGHT:
            yrot += 2.0

def draw():
    global xrot, yrot, lightpos, greencolor, treecolor

    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, treecolor)
    glTranslatef(0.0, 0.0, -0.7)
    gluCylinder(gluNewQuadric(), 0.1, 0.1, 0.2, 20, 20)  # Используем gluCylinder вместо glutSolidCylinder

    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, greencolor)
    glTranslatef(0.0, 0.0, 0.2)
    #gluCylinder(gluNewQuadric(), 0.0, 0.5, 0.5, 20, 20)
    gluCylinder(gluNewQuadric(), 0.5, 0.0, 0.5, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)
    gluCylinder(gluNewQuadric(), 0.4, 0.0, 0.4, 20, 20)
    glTranslatef(0.0, 0.0, 0.3)
    gluCylinder(gluNewQuadric(), 0.3, 0.0, 0.3, 20, 20)

    glPopMatrix()
    glfw.swap_buffers(window)

if not glfw.init():
    sys.exit()

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
window = glfw.create_window(300, 300, "Happy New Year!", None, None)

if not window:
    glfw.terminate()
    sys.exit()

glfw.make_context_current(window)
glfw.set_key_callback(window, key_callback)

init()

while not glfw.window_should_close(window):
    draw()
    glfw.poll_events()

glfw.terminate()
