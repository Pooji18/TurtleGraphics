#Animated video through python program

from turtle import*


speed (150)

bgcolor("black")
c=['violet','green','red','orange','blue','yellow','pink']
pensize(0.1)
for i in range(350):
     color(c[(i%6)+1])
     fd(i+75)
     lt(91) 
done()
