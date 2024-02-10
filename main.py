from turtle import Turtle, Screen
import random

ran = random.Random()
screen = Screen()

screen.setworldcoordinates(-screen.window_width()/2, -screen.window_height()/2, screen.window_width()/2,
                           screen.window_height()/2)

screen_width = screen.window_width()
screen_height = screen.window_height()

beginning_x = -screen_width / 2
beginning_y = screen_height / 2

end_x = screen_width / 2
end_y = -screen_height / 2

red = Turtle()
green = Turtle()
blue = Turtle()
yellow = Turtle()
indigo = Turtle()
violet = Turtle()
orange = Turtle()

turtles = [red, green, blue, yellow, indigo, violet, orange]

red.color("red")
green.color("green")
blue.color("blue")
yellow.color("yellow")
indigo.color("indigo")
violet.color("violet")
orange.color("orange")

v = beginning_y / 2

for i in turtles:
    i.penup()
    i.shape("turtle")
    i.goto(beginning_x, v)
    v -= 50

flag = True

while flag:
    for i in turtles:
        if i.xcor() < end_x:
            i.forward(ran.randint(10, 20))
        else:
            flag = False
            print(f"{i.color()[0]} Wins")
            break


screen.exitonclick()
