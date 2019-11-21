counter=0
cx=0
cy=0
nx=0
ny=0
def setup():
    size(500,500)
    smooth()
    background(0)
    strokeWeight(1)

def draw():
    global counter,cx,cy,nx,ny
    stroke(200,5)
    for si in range(0,6,1):
        for ci in range(0,6,1):
            nx=ci*80+50
            ny=si*80+50
            x1=nx-sin(counter)*(50)
            y1=ny-cos(counter)*(50)
            x2=ny+sin(counter)*(50)
            y2=nx+cos(counter)*(50)
            line(x1,y1,x2,y2)
    
    counter += 0.1
    if counter > 2*PI:
        counter=0
