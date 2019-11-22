amount=20
num=20

def setup():
    size(640,640)
    stroke(0,150,255,100)
    
def draw():
    global num,amount
    fill(0,40)
    rect(-1,-1,width+1,height+1)
    maxX = map(mouseX,0,width,1,250)
    
    translate(width/2,height/2)
    
    for i in range(0,360, amount):
        x = sin(radians(i+num))*maxX
        y = cos(radians(i+num))*maxX
        
        x2 = sin(radians(i+amount-num))*maxX
        y2 = cos(radians(i+amount-num))*maxX
        
        noFill()
        bezier(x,y,x-x2,y-y2,x2-x,y2-y,x2,y2)
        bezier(x,y,x+x2,y+y2,x2+x,y2+y,x2,y2)
        fill(0,150,255)
        ellipse(x,y,5,5)
        ellipse(x2,y2,5,5)
    num +=0.5
