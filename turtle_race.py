
from turtle import Turtle, Screen
import random

screen = Screen()
screen.title(titlestring="Turtle's are faster than rabbits")
screen.setup(width=600, height=600)
screen.bgcolor("black")
position = [(-250, -250), (-250, -150), (-250, 0), (-250, 150), (-250, 250)]
colors = ['red', 'blue', 'pink', 'yellow', 'turquoise']
# I need 5 turtles so range a loop till 5
runners = []
for i in range(5):
    shree = Turtle()
    shree.shape('turtle')
    shree.penup()
    shree.goto(position[i])
    shree.color(colors[i])
    runners.append(shree)
end = False
while not end:
    for runner in runners:
        runner.forward(random.randint(0, 10))
        if runner.xcor() >= 290:
            print(runner.color())
            end = True

screen.mainloop()