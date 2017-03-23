import turtle
import random

screen=turtle.Screen()
screen.bgcolor('black')

bing=turtle.Turtle()
bing.speed(0)
colours=['green','red','yellow','white']

def dots(radius,x,y):
    bing.penup()
    bing.color(random.choice(colours))
    bing.fillcolor(random.choice(colours))
    bing.goto(x,y)
    bing.pendown()
    bing.begin_fill()
    bing.circle(radius)
    bing.end_fill()
    
    

for i in range(10):
    dots(50,random.randint(-5,5),random.randint(-5,5))
    bing.right(33)

for i in range(1):
    bing.fillcolor('brown')
    bing.begin_fill()
    bing.forward(10)
    bing.right(120)
    bing.forward(250)
    bing.right(90)
    bing.forward(20)
    bing.right(90)
    bing.forward(250)
    bing.end_fill()
    
    
