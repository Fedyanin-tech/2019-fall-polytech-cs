centerX = 0
centerY = 0
angle = 0
fsize  = 0
weight = 0
counter = 0
centerX= 500/2
centerY= 500/2
angle= 0
fsize= 150
weight = 1

class MyEllipse():

    def render(self, fsize):
        fill(200, fsize/20)
        x1 = (centerX + sin(counter)*100) - cos(angle)*fsize/2
        y1 = (centerY + cos(counter)*100) + sin(angle)*fsize/2
        
        stroke(250, 100)
        strokeWeight(weight)
        ellipse(x1, y1,fsize,fsize)
        
e = MyEllipse()
        
def setup():
    size(500,500)
    smooth()
    background(10)
    
def draw():
    global counter
    counter += 0.01
    if counter > 2*PI:
        counter = 0
        
    e.render(sin(counter*4)*mouseX)
