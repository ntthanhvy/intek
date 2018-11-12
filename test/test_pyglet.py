import pyglet
xsize, ysize = 800, 500
window = pyglet.window.Window(xsize,ysize)

pyglet.resource.path = ["./"]
pyglet.resource.reindex()

red = pyglet.resource.image("green-square.png")
blue = pyglet.resource.image('square.png')
red.width = 60
red.height = 60
blue.width, blue.height = 60, 60

b = pyglet.graphics.Batch()

class RedSquare():

    def __init__(self,img,x=100,y=100,velocity_x=1, velocity_y=1):
        self.sprite = pyglet.sprite.Sprite(img=img,x=x,y=y,batch=b)
        self.velocity_x, self.velocity_y = velocity_x, velocity_y

    def update_up(self,dt):
        # self.sprite.x += self.velocity_x*dt
        # self.sprite.y += self.velocity_y*dt
        # self.sprite.y += self.velocity_y * dt
        # if self.sprite.y < self.sprite.y + 150:
        #     self.sprite.y = self.sprite.y + 150
        #     self.sprite.x += self.velocity_x * dt
        #     if self.sprite.x > self.sprite.x + 150\
        #        or self.sprite.x < self.sprite.x - 150:
        #         self.sprite.x = self.sprite.x + 150

        # self.checkBoundaries()
        move_right = True
        move_up = True
        if self.sprite.y != 210:
            if move_up == True:
                self.sprite.y = min(self.sprite.y + self.velocity_y * dt, 210)
                move_up = False
                print(self.sprite.y)
        elif self.sprite.y != 150:
            if move_up == False:
                self.sprite.y = min(self.sprite.y - self.velocity_y * dt, 150)
                move_up = True
                print(self.sprite.y)
        if self.sprite.x != 210:
            if move_right == True:
                self.sprite.x = min(self.sprite.x + self.velocity_x * dt, 210)
                move_right = False
                print(self.sprite.x)
        # if self.sprite.y != 150:
        #     if move_up is False:
        #         self.sprite.y = min(self.sprite.y - self.velocity_y * dt, 150)
        #         move_up = True
        #         print(self.sprite.y)

    def update_down(self, dt):
        move_right = True
        move_down = True
        if self.sprite.y != 150:
            if move_down == True:
                self.sprite.y = min(self.sprite.y - self.velocity_y * dt, 150)
                move_down = False
                print(self.sprite.y)
        # if self.sprite.x != 270:
        #     if move_right == True:
        #         self.sprite.x = min(self.sprite.x + self.velocity_x * dt, 270)
        #         move_right = False
        #         print(self.sprite.x)


    def checkBoundaries(self):
        if self.sprite.x < 0:
            self.sprite.x = 500
        if self.sprite.x > 500:
            self.sprite.x = 0
        if self.sprite.y < 0:
            self.sprite.y = 500
        if self.sprite.y > 500:
            self.sprite.y = 0


squares = []

squares.append(RedSquare(red, x=100, y=210, velocity_x=100, velocity_y=100))
squares.append(RedSquare(blue,x=40, y=210, velocity_x=100, velocity_y=100))
# squares.append(RedSquare(red,x=600,y=150, velocity_x=10, velocity_y=50))



def update(dt):
    for s in squares:
        s.update_up(dt)
        # s.update_down(dt)

pyglet.clock.schedule_interval(update, 1/120.0)



@window.event
def on_key_press(symbol,modifiers):
    print("key %s modifiers %s" % (symbol, modifiers))
@window.event
def on_draw():
    window.clear()
    b.draw()

if __name__ == '__main__':
    pyglet.app.run()
