import turtle
t=turtle.Turtle()
t.speed(0)
 
def box():
    for i in range(4):
        t.forward(40)
        t.left(90)


x=0
y=0
count=2

while True:
    t.goto(x,y)
    t.pendown()
    x+=40
    t.begin_fill()
    if count%2==0:
        t.fillcolor("black")

    else:
        t.fillcolor("white")

    count+=1       
    box()
    t.end_fill()
     
    t.penup()
    

   

    if(x>=40*8):
        x=0
        y+=40
        count+=1
         
        t.goto(x,y)

    if(y>=40*8):
        break
         
t.hideturtle()        

