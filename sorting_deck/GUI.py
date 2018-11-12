from pyglet.gl import *
from pyglet.window import key, mouse
import sorting_deck as s

# --------change resource path-----------------
pyglet.resource.path = ['./image']
pyglet.resource.reindex()

# ------------set up window--------------------
win = pyglet.window.Window(width=800, height=500, resizable=True)
glClearColor(0, 119/255, 138/255, 1)
win.set_minimum_size(500, 300)

# -------------default val and setup-----------
arr = s.get_args().N
elem = []
font = 'DejaVu Sans'
main = pyglet.graphics.Batch()
default = pyglet.resource.image('square.png')
select = pyglet.resource.image('green-square.png')
compare = pyglet.resource.image('red-square.png')
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
label = pyglet.text.Label('0', y=win.height//2,
                          anchor_x='center', anchor_y='center',
                          font_name=font,
                          font_size=20,
                          batch=main, group=foreground)


# -------------change size of img
def changesize(img):
    img.width = 60
    img.height = 60
    img.anchor_x = img.width//2
    img.anchor_y = img.height//2


changesize(default)


# ---------a atribute of a square---------------------
square = pyglet.sprite.Sprite(img=default, x=100, y=win.height//2,
                              batch=main, group=background)


# -----------draw the arr-------------------
def show_arr(arr):
    for i in range(len(arr)):
        dist = 70 * i
        x = 150 + dist
        square.x = x
        label.text = arr[i]
        label.x = x
        elem.append(square)
        main.draw()


# -------get the arr from the sorting_deck--------------
def get_arr(arr):
    args = s.get_args().algo
    if args == 'insert':
        lst = s.insert(arr)
    else:
        lst = s.bubble(arr)
    return lst


# ------------run on keyboard event-----------------
@win.event
def on_key_press(symbol, mods):
    if symbol == key.SPACE or symbol == key.ENTER:
        lst = get_arr(arr)
        show_arr(lst)
        # draw_active(lst)


# -----------draw the first window------------------
@win.event
def on_draw():
    win.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    show_arr(arr)


pyglet.app.run()
