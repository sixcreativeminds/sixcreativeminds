from turtle import *
def square(a):
  for i in range(4):
    fd(a)
    left(90)

color("red" , "yellow")
begin_fill()
square(100)
end_fill()
