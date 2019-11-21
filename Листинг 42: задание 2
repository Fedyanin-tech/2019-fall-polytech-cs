counter = 0
cx = 875
cy = 400
nx = 0
ny = 0
counter1 = 0
cR = 250
ncx = 0
ncy = 0
i=5
def setup():
    size(1750,800)
    smooth()
    background(0)
    strokeWeight(1)
    
def oneLineDraw(ncx, ncy):
    global cx,counter,cy,nx,ny,counter1,cR,i
    x1 = ncx - sin(counter1)*100
    y1 = ncy - cos(counter1)*100
    x2 = ncx + sin(counter1)*100
    y2 = ncy + cos(counter1)*100
    line(x1,y1,x2,y2)
    
def draw():
    global cx,counter,cy,nx,ny,counter1,cR, ncx, ncy,i
    i=i+5
    if i<3000:
        stroke(i+150,125,50)
    else:
        stroke(100,i,10)
        if i<6000:
            stroke(20,50,i)
    nx = sin(counter1)*cR + cx
    ny = cos(counter1)*cR + cy
    x1 = nx - sin(counter)*150
    y1 = ny - cos(counter)*150
    x2 = nx + sin(counter)*150
    y2 = ny + cos(counter)*150
    
    oneLineDraw(x2,y2)
    oneLineDraw(x1,y1)
    
    counter += 0.1
    if counter > 2*PI:
        counter = 0
        
    counter1 += 0.01
    cR += counter/20
    if counter1 > 2*PI:
        counter1 = 0
