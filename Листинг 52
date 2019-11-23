cx = 0
cy = 0
fsize = 0

class FunnyCircle():

    def setCenter(self, x,y):
        self.cx = x
        self.cy = y

    def setSize(self, size):
        self.size = size

    def render(self):
        ellipse(self.cx, self.cy, self.size, self.size)


funnyCircle = FunnyCircle()

def setup():
    size(600,600)
    smooth()
    noStroke()
    funnyCircle.setSize(50)

def draw():
    background(255)
    fill(50)
    funnyCircle.setCenter(mouseX, mouseY)
    funnyCircle.render()
