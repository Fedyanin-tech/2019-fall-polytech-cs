r = 50
cx = 500/2
cy = 500/2
l = 350
a = PI/4
w = 1
c = 0

class myline():
    
    def render(self, cx,cy,a):
        x1 = cx - cos(a)*l/2
        y1 = cy + sin(a)*l/2
        x2 = cx + cos(a)*l/2
        y2 = cy - sin(a)*l/2
        
        stroke(50,100)
        strokeWeight(w)
        line(x1,y1,x2,y2)
        strokeWeight(5)
        stroke(50)
        line(x2,y2,x2,y2)    
        line(x1,y1,x1,y1)
    
mline=myline()

def setup():
    size(500,500)
    smooth()
    background(255)
    
def draw():
    global c,r
    c += 0.05
    
    if c>2*PI:
        c = 0
        r += 50
    
    mline.render(width/2 + sin(c)*r, width/2 + cos(c)*r, c*2)
