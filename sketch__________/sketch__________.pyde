add_library('sound')
from processing import sound
s = sound.Sound(this)
def reset():
    global x, y, diam, rectSize, speedX, speedY, s, q
    #движение мячика
    x = width/2 - 500
    y = height/2
    #переменные задающие скорость
    i=random(15,20)
    j=random(15,20)
    speedX = i
    speedY = j
    diam = 15
    rectSize = 200;
    q=0
    
def setup():
    loadFont("123.vlw")
    textFont(loadFont("123.vlw"),48)
    smooth(8)
    fullScreen()
    reset()
    
def draw():
    global x, y, speedX, speedY, diam, rectSize, s, q
    noStroke()
    #фон
    fill(0,0,0)
    rect(0,0,width-30,height)
    fill(0,0,0)
    rect(width-30,0,30,height)
    
    # мячик
    fill(255)
    ellipse(x, y, diam, diam)
    
    # платформы
    rectMode(CORNER)
    fill(255, 255, 255)
    rect(0, 0, 20, height)
    rect(20,0,width-25,20)
    rect(20,height-20,width-25,20)
    
    rect(width-30, mouseY-rectSize/2, 10, rectSize)
    
    # граница
    stroke(255,0,0)
    line(width-5,0,width-5,height)
    
    #движение(отрисовка) мячика задаваемое "скоростью" 
    x += speedX
    y += speedY

    #если игрок отбивает мяч
    if x > width-30 and x < width+30 and y > mouseY-rectSize/2 and  y < mouseY+rectSize/2:
        speedX = speedX * -1
        #звук отскока
        sin = sound.SoundFile(this, 'otskok0.wav')
        sin.play()
        s.volume(1)
       
        q=q+1
        print(q)
        print(speedX)
        
    #отрисовка поинтов
    textAlign( RIGHT )         
    text(str(q),80,80)
            
    # если мячик отскакивает от стенки
    if x < 25:
        #стенка "отбиавает" мячик
        p=random(0.8, 1.2)
        d=random(0.8, 1.2)
        speedX *= -p
        speedY *=  d
        x += speedX
        
        #звук отскока
        sin = sound.SoundFile(this, 'otskok01.wav')
        sin.play()
        s.volume(1)
        
    # если мячик отскакивает от пола или потолка   
    if  y > height-25 or y < 25:  
        speedY *= -1
        
        #звук отскока
        sin = sound.SoundFile(this, 'otskok02.wav')
        sin.play()
        s.volume(1)
        
    #game over    
    if x > width+31:
        rectMode(CENTER)
        fill(255)
        rect(width/2,height/2,width,height)
        fill(0)
        textAlign( RIGHT )
        text('YOUR SCORE =',width/2,height/2 -50)    
        text(str(q),width/2 +50,height/2 -50)
        text('Press R to restart',width/2,height/2 +50)
        if q>24:
            img = loadImage("kianu.jpg")
            imageMode(CENTER)
            image(img, mouseX, mouseY)
        if q>35:
            img = loadImage("pianu.jpg")
            imageMode(CENTER)
            image(img, mouseX, mouseY)
        if mousePressed:
            background(255)
            for t  in range(0,10):
                for ty in range(-6,7):
                    text('your score will never reach 2153',210+t*200,ty*150 +t*50)
                    
#рестарт
def keyPressed():
    if key == 'r':
        reset()
