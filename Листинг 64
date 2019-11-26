num = 60
mx = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
my = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

def setup():
    size(640,360)
    noStroke()
    fill(255,153)
    
def draw():
    background(51)
    which = frameCount % num
    mx[which] = mouseX
    my[which] = mouseY
    
    for i in range(0, num):
        index = (which +1 +i) % num
        ellipse(mx[index], my[index], i, i)
    
    print(frameCount)
