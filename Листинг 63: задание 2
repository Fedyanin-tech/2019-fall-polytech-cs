xCt = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
i = 1
def setup():
    size(500,500)
    smooth()
    noStroke()
    myInit()
    
def myInit():
    for i in range (len(xCt)):
        xCt[i] = 250 + random(-100,100)
        ellipse(xCt[i], 250, 10*i,10*i)
        fill(20)
        ellipse(xCt[i], 250, 5, 5)
        fill(250, 40)
def draw():
    background(50)
    if mouseX > 250:
        myInit()
    
def keyPressed():
    if key == "s":
        print( max(xCt))
