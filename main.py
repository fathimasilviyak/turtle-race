from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []
screen = Screen()
# set screen width ad height
screen.setup(width=500, height=400)
# Ask the user to bet which turtle gonna win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "blue", "green", "purple", ]
y_positions = [-70, -40, -10, 20, 50, 80]
# create the turtle and pass it shape as 'turtle' in constructor
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
# all turtles are 40 by 40 in size, so when x cordinates reaches at 230, which means the centre of the turtle will be at
# 230, since tuttle half size will be 40/2 = 20, then 230+20 = 250 , which is the total width of screen. So the tutrtle
# touches the end the of screen.

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

screen.exitonclick()
