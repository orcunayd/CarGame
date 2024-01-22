import turtle , time , random
from playsound import playsound

pencere = turtle.Screen()
pencere.title('Araba Yarişi')
pencere.bgcolor('gray')
pencere.setup(height=700 ,width=500)
pencere.tracer(0)

pencere.register_shape('racingback.gif')
pencere.register_shape('racingcar.gif')
pencere.register_shape('car2.png',turtle.Shape("image","car2.png"))


araba = turtle.Turtle()
araba.speed(0)
araba.shape('racingcar.gif')
araba.shapesize(2)
araba.color('red')
araba.setheading(90)
araba.penup()
araba.goto(0,-200)

arkaplan = turtle.Turtle()
arkaplan.speed(0)
arkaplan.pensize(3)
arkaplan.shape('square')
arkaplan.color('white')
arkaplan.penup()
arkaplan.hideturtle()
arkaplan.goto(0,0)

puan = 0
puan_turtle= turtle.Turtle()
puan_turtle.hideturtle()
puan_turtle.penup()
puan_turtle.color('black')
puan_turtle.goto(0,290)
puan_turtle.write("Puan: {}".format(puan),align='center',font=('Courier',12,'bold'))

kamera_dy = 0
kamera_y = 0

def sol():
    x = araba.xcor()
    x = x - 10
    if x < -170:
        x = -170
    araba.setx(x)

def sağ():
    x = araba.xcor()
    x = x + 10
    if x > 170:
        x = 170
    araba.setx(x)

engeller = []
for i in range(10):
    engel = turtle.Turtle()
    engel.speed(0)
    engel.shape('square')
    engel.shapesize(3,6)
    engel.color('red')
    engel.setheading(90)
    engel.penup()
    engel.dx = random.randint(-170,170)
    engel.dy = 500
    engel.goto(engel.dx,engel.dy)
    engeller.append(engel)

pencere.listen()
pencere.onkeypress(sol,"Left")
pencere.onkeypress(sağ,"Right")
baslangic_zaman = time.time()
i = -1


while True:
    kamera_dy = -2
    kamera_y = kamera_y + kamera_dy
    kamera_y = kamera_y % 700

    arkaplan.goto(0,kamera_y - 700)
    arkaplan.shape('racingback.gif')
    arkaplan.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()

    arkaplan.goto(0, kamera_y)
    arkaplan.shape('racingback.gif')
    arkaplan.stamp()
    araba.shape('racingcar.gif')
    araba.stamp()

    if time.time() - baslangic_zaman > random.randint(2,6):
        baslangic_zaman = time.time()
        i = i + 1
        if i == 9:
            i = -1
            engel.dx = random.randint(-170,170)
            engel.dy = 500
            engel.goto(engel.dx, engel.dy)
    y = engeller[i].ycor()
    y = y - 2
    engeller[i].sety(y)

    if engeller[i].distance(araba) < 15:
        break
    
    if engeller[i].distance(araba) > 15:
        puan = puan + 1
        puan_turtle.clear()
        puan_turtle.write("Puan: {}".format(puan),align='center',font=('Courier',12,'bold'))

    pencere.update()

    arkaplan.clear()
    araba.clear()






