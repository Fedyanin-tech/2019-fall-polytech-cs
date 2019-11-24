rad = 50
cx = 500/2
cy = 500/2
l = 350
a = PI/4
w = 1
c = 0
r = 0
g = 10
b = 150
class myline():
    
    def render(self, cx, cy, a):
        x1 = cx - cos(a)*l/2
        y1 = cy + sin(a)*l/2
        x2 = cx + cos(a)*l/2
        y2 = cy - sin(a)*l/2
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
                
        stroke(150,100)
        strokeWeight(w)
        line(x1,y1,x2,y2)
        
    def colors(self):
        global r, g, b
        r += random(0,10)
        g += random(0,5)
        b += random(10,15)
        
        if g >255:
            g = -g
        if r > 255:
            r =-r
        if b >255:
            b = -b
            
        stroke( r, g, b, 150)
        strokeWeight(10)
        line(self.x2, self.y2, self.x2, self.y2)
        line(self.x1, self.y1, self.x1, self.y1)

mline = myline()

def setup():
    size(500,500)
    smooth()
    background(0)
    
def colOr():
    global r, g, b

def draw():
    global c, rad
    c += 0.05
    
    if c > 2*PI:
        c = 0
        rad += 50
        
    mline.render(width/2 + sin(c)*rad, width/2 + cos(c)*rad, c*2)
    mline.colors()
