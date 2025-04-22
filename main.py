import turtle
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
y = -170

for racer in range(6):
    # variable racer is an int number, t_racer is a str to identify a new turtle. Turtles are named after their color.
    t_racer = colors[racer]
    t_racer = Turtle("turtle")
    t_racer.color(colors[racer])
    t_racer.penup()
    t_racer.goto(-230, y)
    all_turtles.append(t_racer)
    y += 60

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color =  turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won the race!")
            else:
                print(f"You've lost. The {winning_color} turtle won the race!")

        rand_distance = random.randint(0,10)
        turtle.forward((rand_distance))




screen.exitonclick()