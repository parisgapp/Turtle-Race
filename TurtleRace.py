from turtle import *
from random import randint

speed(10)
penup()
goto(-140,140)

for step in range(6):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)
  
toddy = Turtle()
toddy.color('deep sky blue')
toddy.shape('turtle')

toddy.penup()
toddy.goto(-160,100)
toddy.pendown()

tory = Turtle()
tory.color('blue violet')
tory.shape('turtle')

tory.penup()
tory.goto(-160,70)
tory.pendown()

paisley = Turtle()
paisley.color('deep pink')
paisley.shape('turtle')

paisley.penup()
paisley.goto(-160,40)
paisley.pendown()

paris = Turtle()
paris.color('lime')
paris.shape('turtle')

paris.penup()
paris.goto(-160,10)
paris.pendown()

robbie = Turtle()
robbie.color('brown')
robbie.shape('turtle')

robbie.penup()
robbie.goto(-160,-20)
robbie.pendown()



for turn in range(100):
  toddy.forward(randint(1,5))
  tory.forward(randint(1,5))
  paisley.forward(randint(1,5))
  paris.forward(randint(1,5))
  robbie.forward(randint(1,5))

