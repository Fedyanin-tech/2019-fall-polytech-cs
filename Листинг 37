def setup():
    size(500,500)
    smooth()
    strokeWeight(1)
    background(0)
    noStroke()
    colorMode(HSB)
    
i=0
k=1
flug=True

def draw():
    if flug:
        for i in range(0,10):
            for j in range(0,5):
                fill (255, random (0, 255) , random (10, 250))
                rect(j*40+50,i*40+50,35,35)
                rect ((10-j)*40+10,i*40+50,35,35)
def mouseClicked():
    global flug
    flug = not flug
