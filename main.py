import turtle as trtl

# Create an empty list of turtles
my_turtles = []

# Use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Create the initial set of turtles
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    t.penup()  
    t.speed(0) 
    color = turtle_colors.pop(0)
    t.color(color)

    my_turtles.append(t)

# Set the starting points
startx = 0
starty = 0
angle = 45
distance = 50  

# Extra Addition: Set up an infinite loop to add turtles in a spiral
while True:
    # Go to point (0,0) and turtle direction
    for t in my_turtles:
        t.goto(startx, starty)
        t.setheading(angle) 
        t.pendown()  

        t.forward(distance)  

        # Update starting position and angle
        startx = t.xcor()  
        starty = t.ycor() 
        angle += 45 
        distance += 10

        if len(turtle_shapes) == 0:
            turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
        if len(turtle_colors) == 0:
            turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

        new_turtle = trtl.Turtle(shape=turtle_shapes.pop(0))
        new_turtle.penup()
        new_turtle.color(turtle_colors.pop(0))
        my_turtles.append(new_turtle)

wn = trtl.Screen()
wn.mainloop()
