def setup():
    size(800, 800)
    background(100)
    smooth()
    colorMode(HSB)
    
def draw():
    background(100)
    img0 = loadImage("000.jpg")
    img1 = loadImage("001.jpg")
    for i in range(0, 10):
        tint(i*25, 150, 255)
        if (mouseX < i*120 + 120 and mouseX > i*120):
            noTint()
            image(img1, i*120, 0)
        else:
            image(img0, i*120,0)
