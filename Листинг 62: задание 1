xCoordinate = [1,2,3,4,5,6,7,8,9,10]
xCdt = [1,2,3,4,5,6,7,8,9,10]
def setup():
    size(500,500)
    smooth()
    noStroke()
    for i in range(len(xCoordinate)):
        xCoordinate[i] = 35*i + 90
    for j in range(len(xCdt)):
        xCdt[j] = 35*j + 90

def draw():
    background(50)
    for j in range(len(xCdt)):
        fill(200,40)
        ellipse( xCdt[j], 340, 150-j*15, 150-j*15)
        fill(0)
        ellipse(xCdt[j], 340, 3, 3)
    for i in range(len(xCoordinate)):
        fill(200,40)
        ellipse(xCoordinate[i], 250, 15*i, 15*i)
        fill(0)
        ellipse(xCoordinate[i], 250, 3, 3)
