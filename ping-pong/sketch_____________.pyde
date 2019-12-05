add_library('sound')
from processing import sound
s = sound.Sound(this)
sin = sound.SoundFile(this, 'otskok.wav')
sin = sound.SoundFile(this, 'otskok1.wav')
sin = sound.SoundFile(this, 'otskok2.wav')
def reset():
    global x,y,diam,rectSize,speedX,speedY, s, q
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
        
        sin.play()
        amplitude = map(mouseX, 0, height, 100, 1000000000000)
        s.volume(1)
        #отрисовка поинтов
        q=q+1
        print(q)
        print(speedX)
    textAlign( RIGHT )         
    text(str(q),80,80)
            
    # если мячик отскакивает от стенки
    if x < 25:
        #стенка "отбиавает" мячик
        p=random(0.9, 1.2)
        d=random(0.9, 1.2)
        speedX *= -p
        speedY *=  d
        x += speedX
        
        #звук отскока
        
        sin.play()
        amplitude = map(mouseX, 0, height, 100, 100000000000000)
        s.volume(1)
        
    # если мячик отскакивает от пола или потолка   
    if  y > height-25 or y < 25:  
        speedY *= -1
        
        #звук отскока
        
        sin.play()
        amplitude = map(mouseX, 0, height, 100, 1000000000000)
        s.volume(1)
    
#рестарт
def keyPressed():
    if key=='r':
        reset()       
                                 
