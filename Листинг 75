isAnimate = True
currentFrame = 1

def setup():
    global img1, img2, img3
    smooth()
    size(800,800)
    frameRate(12)
    img1 = loadImage("001.jpg")
    img2 = loadImage("002.jpg")
    img3 = loadImage("003.jpg")
    
    
def draw():
    global currentFrame, isAnimate
    if isAnimate:
        if currentFrame == 1:
            background(100)
            image(img1, mouseX, mouseY)
        if currentFrame == 2:
            background(100)
            image(img2, mouseX, mouseY)
        if currentFrame == 3:
            background(100)
            image(img3, mouseX, mouseY)
            
        currentFrame += 1
        if currentFrame > 3:
            currentFrame = 1
        
    else:
        background(100)
        image(img3, mouseX, mouseY)
        
def keyPressed():
    global isAnimate
    if key == "s":
        if isAnimate:
            isAnimate = False
        else:
            isAnimate = True
