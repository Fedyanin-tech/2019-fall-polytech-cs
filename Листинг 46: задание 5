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
    global counter1,cx,cy,cR,counter
    nx=sin(counter1)*cR+cx
    ny=cos(counter1)*cR+cy
    x1=nx-sin(counter)*20
    y1=ny-cos(counter)*20
    x2=nx +sin(counter)*20
    y2=ny+ cos(counter)*20
    fill(random(0,255),random(0,255),random(0,255),random(0,100))
    ellipse(x1,y1,x2/8,y2/8)
    counter +=mouseX/float(width*2)
    if counter > 2*PI:
        counter=0
    counter1 += mouseX/float(width*2)
    cR += mouseX/float(width*2)
    if counter1 > 2*PI:
        counter1=0
