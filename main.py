import turtle as trtl

class TurtleManager:
    def __init__(self):
        # Create an empty list of turtles
        self.turtles = []
        # Use interesting shapes and colors
        self.turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
        self.turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
        
        self._create_initial_turtles()

    def _create_initial_turtles(self):
        for shape in self.turtle_shapes:
            turtle = trtl.Turtle(shape=shape)
            turtle.penup()
            turtle.speed(0)
            color = self.turtle_colors.pop(0)
            turtle.color(color)
            self.turtles.append(turtle)

    def add_turtle(self):
        if len(self.turtle_shapes) == 0:
            self.turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
        if len(self.turtle_colors) == 0:
            self.turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

        new_turtle = trtl.Turtle(shape=self.turtle_shapes.pop(0))
        new_turtle.penup()
        new_turtle.color(self.turtle_colors.pop(0))
        self.turtles.append(new_turtle)

    def move_turtles_in_spiral(self):
        # Set the starting points
        startx = 0
        starty = 0
        angle = 45
        distance = 50

        # Extra Addition: Set up an infinite loop to add turtles in a spiral
        while True:
            # Go to point (0,0) and turtle direction
            for turtle in self.turtles:
                turtle.goto(startx, starty)
                turtle.setheading(angle)
                turtle.pendown()

                turtle.forward(distance)

                # Update starting position and angle
                startx = turtle.xcor()
                starty = turtle.ycor()
                angle += 45
                distance += 10

                if len(self.turtle_shapes) == 0:
                    self.turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
                if len(self.turtle_colors) == 0:
                    self.turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
                self.add_turtle()

    def __str__(self):
        turtle_info = []
        for turtle in self.turtles:
            turtle_info.append(f"Turtle at ({turtle.xcor()}, {turtle.ycor()}) with shape {turtle.shape()} and color {turtle.color()[0]}")
        return "\n".join(turtle_info)

manager = TurtleManager()
manager.move_turtles_in_spiral()

wn = trtl.Screen()
wn.mainloop()
