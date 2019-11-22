counter=0
counter1=0
cx=400
cy=400
cR=10
def setup():
    size(800,800)
    smooth()
    background(255)
    strokeWeight(1)

def draw():
    global counter1,cx, cy, cR,counter
    stroke(0,50)
    nx = sin(counter1)*cR + cx
    ny = cos(counter1)*cR + cy
    x1=nx-sin(counter)*50
    y1=ny-cos(counter)*50
    x2=nx+sin(counter)*50
    y2=ny+cos(counter)*50
    bezier(x1,y1, y1,x1, x2,y2, y2,x2)
    counter += mouseX/float(width*2)
    if counter > 2*PI:
        counter = 0
    counter1 += mouseX/float(width*2)
    cR += counter / 10
    if counter1 > 2*PI:
        counter1 = 0
