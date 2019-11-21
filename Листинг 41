def setup():
    size(500,500)
    smooth()
    background(255)
    strokeWeight(1)

counter = 1
counter1 = 1
cx = 250
cy = 250
cR = 200

def draw():
    global counter , counter1, cx , cy, cR
    stroke(0,30)
    nx = sin(counter1)*cR + cx
    ny = cos(counter1)*cR + cy

    x1 = nx - sin(counter)*200
    y1 = ny - cos(counter)*200
    x2 = nx + sin(counter)*200
    y2 = ny + cos(counter)*200

    line(x1, y1,x2, y2)

    counter += 0.1
    if counter > 2*PI:
        counter = 0

    counter1 += 0.01
    if counter1 > 2*PI:
        counter1 = 0
