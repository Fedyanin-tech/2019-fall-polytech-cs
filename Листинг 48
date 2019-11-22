def setup():
    size(800,800)
    smooth()
    
def draw():
    background(255)
    stroke(100)
    strokeWeight(5)

    anc1X=mouseX
    anc1Y=mouseY
    cont1X=width/2
    cont1Y=height/2 - 100
    cont2X=width/2
    cont2Y=height/2 + 100
    anc2X=width - mouseX
    anc2Y=height-mouseY
    noFill()
    bezier(anc1X,anc1Y,cont1X,cont1Y,cont2X,cont2Y,anc2X,anc2Y)
    
    stroke(50)
    strokeWeight(1)
    line(anc1X,anc1Y,cont1X,cont1Y)
    line(anc2X,anc2Y,cont2X,cont2Y)
    
    fill(150)
    noStroke()
    rectMode(CENTER)
    rect(cont1X,cont1Y,6,6)
    rect(cont2X,cont2Y,6,6)
    
    fill(170,0,0)
    noStroke()
    ellipseMode(CENTER)
    ellipse(anc1X,anc1Y,10,10)
    ellipse(anc2X,anc2Y,10,10)
