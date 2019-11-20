def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(5)
    stroke(250)
    noLoop()

cx=250
cy=250
cR=200
i=0

def draw():
    global cx,cy, cR, i
    
    while i < 2*PI:
        i +=PI/6
        x1 = cos(i)*cR+cx
        y1 = sin(i)*cR+cy
        line(x1,y1,x1,y1)
    line(cx,cy,cx,cy)
    
def keyPressed():
    if key =="s":
        saveFrame("Photo") 
