counter=0
counter1=0
nx=0
ny=0
cx=250
cy=250
cR=10
switcher=1

def setup():
    size(500,500)
    smooth()
    background(0)
    strokeWeight(50)

def draw():
    global counter1,nx,ny,cx,cy,cR,switcher,counter
    if switcher > 0:
        nx=cos(counter1)*cR+cx
        ny=sin(counter1)*cR+cy
        stroke(0,50)
    else:
        nx=sin(counter1)*cR+cx
        ny=cos(counter1)*cR+cy
        stroke(250,50)
        
    switcher *=-1
    
    x1=nx-sin(counter)*20
    y1=ny-cos(counter)*20
    x2=nx+sin(counter)*20
    y2=ny+cos(counter)*20
    
    line(x1,y1,x2,y2)
    
    counter +=0.1
    if counter > 2*PI:
        counter=0
    
    counter1 +=0.01
    cR += counter / 50
    if counter1 > 2*PI:
        counter1=0
