import colorgram
import turtle as t
import random


t.colormode(255)
tortuga = t.Turtle()
tortuga.speed('fastest')
tortuga.shape("turtle")
tortuga.shapesize(4)
tortuga.penup()

colors = colorgram.extract('./dots_and_squares.jpg', 24)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    rgb_colors.append(rgb_color)

rgb_colors = rgb_colors[:12]
reverse_rgb_colors = rgb_colors[::-1]

tortuga.forward(200)
tortuga.setheading(90)
tortuga.forward(200)
tortuga.pendown()
tortuga.pensize(10)
tortuga.color((0, 0, 0))

number_of_squares = 41
move_forward = 400

for square in range(1, number_of_squares):
            tortuga.pencolor((20, 20, 20))
            tortuga.setheading(180)
            tortuga.forward(move_forward)
            tortuga.setheading(270)
            tortuga.forward(move_forward)
            tortuga.setheading(0)
            tortuga.forward(move_forward)
            tortuga.setheading(90)
            tortuga.forward(move_forward)
            move_forward = move_forward - 10
tortuga.setheading(225)
tortuga.forward(565)

tortuga.penup()
tortuga.setheading(0)

tortuga.home()

rad = 400
for _ in range(20):
    tortuga.dot(rad, random.choice(rgb_colors))
    rad = rad - 20

tortuga.pendown()
tortuga.pensize(4)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tortuga.color((20, 20, 20))
        tortuga.circle(100)
        tortuga.setheading(tortuga.heading() + size_of_gap)

draw_spirograph(22)

tortuga.penup()

tortuga.setheading(0)
tortuga.forward(180)
tortuga.setheading(90)
tortuga.forward(180)

tortuga.dot(40, rgb_colors[0])
tortuga.dot(30, reverse_rgb_colors[0])
tortuga.setheading(270)
tortuga.forward(44)
tortuga.dot(40, rgb_colors[1])
tortuga.dot(30, reverse_rgb_colors[1])
tortuga.setheading(90)
tortuga.forward(44)
tortuga.setheading(180)
tortuga.forward(44)
tortuga.dot(40, rgb_colors[2])
tortuga.dot(30, reverse_rgb_colors[2])


angle = 180
for count in range(3, 10, 3):
    tortuga.setheading(angle)
    tortuga.forward(272)
    tortuga.dot(40, rgb_colors[count])
    tortuga.dot(30, reverse_rgb_colors[count])
    tortuga.forward(44)
    tortuga.dot(40, rgb_colors[count+1])
    tortuga.dot(30, reverse_rgb_colors[count+1])
    angle = angle + 90
    tortuga.setheading(angle)
    tortuga.forward(44)
    tortuga.dot(40, rgb_colors[count+2])
    tortuga.dot(30, reverse_rgb_colors[count+2])

tortuga.home()
tortuga.hideturtle()

screen = t.Screen()
screen.exitonclick()