img=0
x=50
a=216
x2=50
mode="вправо"
mode1="вверх"
mode2="вверх1"
x3=70
x4=200
y=50
y2=580
x5=470
b=54
def setup():
    size(800,800)
    global img
    img= loadImage("img.jpg")
def draw():
    global img,x,mode,a,x2,x3,x4,y,mode1,mode2,y2,b
    background(0,0,a)
    image(img,x,450,150,150)
    fill(105,214,63)
    rect(0,600,800,200)
    fill(90,79,66)
    rect(560,439,220,220)
    triangle(675,300,555,440,790,440)
    fill(208,232,b)
    rect(675,530,70,70) # окно
    fill(255,255,255)
    rect(520,550,60,150)
    line(530,700,530,780)
    line(560,700,560,780)
    line(530,600,470,y2)#рука
    line(570,600,630,580)
    ellipse(550,530,70,70)
    ellipse(535,520,10,10)
    ellipse(560,520,10,10)
    line(530,545,540,550)
    line(540,550,547,553)
    line(547,553,553,553)
    line(553,553,557,552)
    line(557,552,560,548)
    fill(204,247,17)
    ellipse(x2,y,50,50)
    fill(255,255,255)
    ellipse(x3,60,120,90)
    ellipse(x4,50,130,85)
    fill(247,120,245)
    ellipse(50,770,10,30)
    ellipse(40,765,10,30)
    ellipse(60,765,10,30)
    ellipse(30,750,30,10)
    ellipse(30,758,30,10)
    ellipse(73,750,30,10)
    ellipse(73,758,30,10)
    ellipse(50,730,10,30)
    ellipse(40,735,10,30)
    ellipse(60,735,10,30)
    fill(67,67,66)
    ellipse(200,760,50,30)
    fill(39,38,38)
    ellipse(270,700,50,35)
    fill(80,77,73)
    ellipse(700,740,75,50)
    fill(247,225,202)
    ellipse(50,750,20,20)
    a=a+1
    x2=x2+2.4
    x3=x3+2.7
    x4=x4+3.2
    b=b+1
    if b>=255:
        b=54
    if y2>=670:
        mode2="вверх1"
    if y2 <=530:
        mode2="вниз1"
    if mode2=="вниз1":
        y2=y2+1
    if mode2=="вверх1":
        y2=y2-1
    if y >=150:
        mode1="вверх"
    if y <=0:
       mode1="вниз"
    if mode1=="вверх":
       y=y-1
    if mode1=="вниз":
       y=y+1
    if x<=50:
       mode="вправо"
    if x>=630:
       mode="влево"
    if mode=="влево":
       x=x-1
    if mode=="вправо":
       x=x+1
    if a>=255:
       a=0
    if x2>= 800 and x3>=800 and x4>=800:
        x2=0
        x3=0
        x4=0
