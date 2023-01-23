import turtle
import time
t = turtle.Turtle()
s = turtle.Screen()
t.speed(10000000)
t.color("white", "white")
#getting position ready for mouth
t.left(180)
t.forward(200)
t.left(180)
t.color("black", "red")
t.begin_fill()
rep = 4
#drawing square for mouth
while rep > 0:
    t.forward(100)
    t.right(90)
    rep -= 1
t.end_fill()
rep = 2
#make white triangle for open mouth
rep2 = 2
t.right(30)
t.forward(100)
t.color("white", "white")
t.begin_fill()
while rep2 > 0:
    t.right(120)
    t.forward(100)
    rep2 -= 1
t.end_fill()
#end of carving out mouth
#begin making body
t.right(90)
t.forward(100)
t.right(90)
t.forward(10)
t.left(90)
t.color("black", "red")
t.begin_fill()
while rep > 0:
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
    rep -= 1
t.end_fill()
#creating scales (NOT upside-down, it was intended.)
t.forward(15)
t.color("black", "green")
t.begin_fill()
rep2 = 14
while rep2 > 0:
    t.left(120)
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.right(240)
    t.forward(15)
    rep2 -= 1
t.end_fill()
rep = 2
#begining of tail
t.color("black", "red")
t.forward(50)
t.right(90)
t.forward(4)
t.left(100)
t.color("black", "red")
t.begin_fill()
while rep > 0:
    t.forward(200)
    t.right(90)
    t.forward(10)
    t.right(90)
    rep -= 1

t.end_fill()
t.color("red", "red")
t.right(100)
t.forward(95)
t.color("black", "green")
#ended tail
#Create Leg 1 (He broke it in a biking accident)
t.begin_fill()
t.forward(50)
t.right(90)
t.forward(12)
t.left(90)
t.begin_fill()
t.backward(50)
t.right(90)
t.backward(12)
t.end_fill()
#End Leg 1
#Create Leg 2 (They inserted the pins into the wrong leg)
t.forward(200)
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.begin_fill()
t.backward(12)
t.left(90)
t.backward(49)
t.end_fill()
#End Leg 2
t.right(90)
t.color("black", "white")
t.forward(38)
t.right(90)
t.forward(90)
t.begin_fill()
t.circle(20)
t.end_fill()
t.left(90)
t.color("white", "white")
t.forward(20)
t.color("black", "black")
t.begin_fill()
t.circle(5)
t.end_fill()
t.color("white", "white")
t.forward(20)

s.exitonclick()
