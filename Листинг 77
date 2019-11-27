def setup():
    background(100)
    smooth()
    img1 = loadImage("000.jpg")
    img2 = loadImage("001.jpg")
    size(800,800)
    global img1, img2
    
def draw():
    myTint000 = map(mouseX, 0, width, 0, 255)
    myTint001 = map(mouseX, 0, width, 255, 0)
    tint(255, myTint001)
    image(img1, 0, 0)
    tint(255, myTint000)
    image(img2,0,0)
