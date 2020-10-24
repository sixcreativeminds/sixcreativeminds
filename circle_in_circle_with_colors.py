from turtle import *
a = ["red" , "green" , "forest green" , "blue" , "sky blue" , "dark blue" , "dark green" , "yellow" , "orange" , "black"]
import random
for i in range(36):
  color(a[random.randint(0 , 9)])
  begin_fill()
  circle(100)
  end_fill()
  left(10)
  
