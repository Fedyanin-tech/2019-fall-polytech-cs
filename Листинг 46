counter=0
counter1=0
cx=125
cy=125
cR=10
def setup():
    size(250,250)
    smooth()
    background(255)
    strokeWeight(1)

def draw():
    global counter1,cx, cy, cR,counter
    stroke(0,50)
    nx = sin(counter1)*cR + cx
    ny = cos(counter1)*cR + cy
    x1=nx-sin(counter)*20
    y1=ny-cos(counter)*20
    x2=nx+sin(counter)*20
    y2=ny+cos(counter)*20
    line(x1,y1,x2,y2)
    counter +=0.1
    if counter > 2*PI:
        counter = 0
    counter1 +=0.01
    cR += counter / 50
    if counter1 > 2*PI:
        counter1 = 0
