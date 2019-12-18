#библиотеки
add_library('sound')
from processing import sound


def reset():
    
    global x, y, diam, rectSize, speedX, speedY, q
    
#начальное положение мячика
    x = width/2 - 500
    y = height/2
    
#переменные задающие скорость
    speedX = random(20, 25)
    speedY = random(5, 7)
    
#параметры    
    diam = 15
    rectSize = 200;
    q=0
    
    
def setup():
    size(1200, 800)
    noSmooth()
    global img1, img2, s, sin
    img1 = loadImage("kianu.jpg")
    img2 = loadImage("pianu.jpg")
    loadFont("123.vlw")
    textFont(loadFont("123.vlw"), 48)
    s = sound.Sound(this)
    sin = sound.SoundFile(this, 'otskok0.wav')
#начало
    reset()
    
    
def draw():
    noStroke()
    global x, y, speedX, speedY, diam, rectSize, s, q, img1, img2, sin
#фон
    fill(0, 0, 0)
    rect(0, 0, width, height)
    
    
#объекты:
 #мячик
    fill(255)
    ellipse(x, y, diam, diam)
    
 #платформы
    rectMode(CORNER)
    fill(255)
    rect(0, 0, 20, height)
    rect(20, 0, width-25, 20)
    rect(20, height-20, width-25, 20)
 #ракетка
    rect(width-30, mouseY-rectSize/2, 10, rectSize)
    
 #граница
    stroke(255, 0, 0)
    line(width-5, 0, width-5, height)
    
    
#процесс:    
 #движение(отрисовка) мячика задаваемое "скоростью" 
    x += speedX
    y += speedY

 #если игрок отбивает мяч
    if x > width - 45 and x < width + 30 and y > mouseY - rectSize/2 and  y < mouseY + rectSize/2:
        speedX = speedX * -1
        
       #звук отскока
        sin.play()
       
  #отрисовка поинтов
        q = q + 1
    textAlign( RIGHT )         
    text(str(q), 80, 80)
            
 #если мячик отскакивает от стенки
    if x < 45:
        speedX *= -random(0.9, 1.2)
        speedY *=  random(0.8, 1.2)
        
      #звук отскока
        sin.play()
    
        
 #если мячик отскакивает от пола или потолка   
    if  y > height - 35 or y < 35:  
        speedY *= -1
        
     #звук отскока
        sin.play()
    
        
 #game over    
    if x > width + 31:
        #фон:
        rectMode(CENTER)
        fill(255)
        rect(width/2, height/2, width, height)
        
        #текст:
        fill(0)
        textAlign( RIGHT )
        text('YOUR SCORE =', width/2, height/2 -50)    
        text(str(q), width/2 +50, height/2 -50)
        text('Press R to restart', width/2, height/2 +50)
        
        #условие пасхалок
        if q > 20:
            imageMode(CENTER)
            image(img1, mouseX, mouseY)
        if q > 35:
            img = loadImage("pianu.jpg")
            imageMode(CENTER)
            image(img2, mouseX, mouseY)
        if mousePressed:
            background(255)
            for t  in range(0, 10):
                for ty in range(-6, 7):
                    text('your score will never reach 2153',210 + t * 200, ty * 150 + t * 50)
  
                                      
#рестарт
def keyPressed():
    if key == 'r':
        reset()
