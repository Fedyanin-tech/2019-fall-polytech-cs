def setup():
    size(1000,1000)
    smooth()
    background(150)
    strokeWeight(1)
    noStroke()

flug = 1

def draw():
    global flug
    myY2 = mouseY/4+random(-5,5)
    myX2 = mouseX/4+random(-5,5)
    fill(flug,random(0,25))
    ellipse(mouseX,mouseY,myX2,myY2)
    
def keyPressed():
    global flug
    if key == "w":
        flug = 255
    if key == "b":
        flug = 0
    if key == "s":
        saveFrame("Photo")
