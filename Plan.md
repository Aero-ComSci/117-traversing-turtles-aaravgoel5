# Plan 

### Variables
1. **my_turtles**: A list to store turtle objects
2. **turtle_shapes**: A list of different shapes for turtles
3. **turtle_colors**: A list of colors for turtles
4. **startx, starty**: Variables fpr the starting coordinates for each turtle
5. **angle**: A variable to control the heading of each turtle
6. **distance**: A variable to control how far each turtle moves forward

### Conditionals
1. **List Management**: Check if the shapes or colors list is empty --> refill them from the original lists
2. **Pen Control**: Make sure that the turtle pen is lifted before moving and put down after it reaches

### Loops
1. **For Loop**
2. **While Loop**

## Changes

### Step 1: Setup
- Create an empty list called `my_turtles` (holding objects)
- Define the lists `turtle_shapes` and `turtle_colors` 

### Step 2: Create Turtles
- Use a **for loop** for `turtle_shapes` and create turtle objects
- Inside the loop:
  - Create a turtle object with a specific shape
  - Set the turtle's speed to `0` for maximum speed
  - Lift the pen using `penup()` 
  - Color to the turtle by "popping" from the `turtle_colors` list
  - Append the turtle to `my_turtles`

### Step 3: Positioning and Drawing
- Initialize `startx` and `starty` for positioning
- Create a **while loop** for drawing
  - Move to (`startx`, `starty`)
  - Heading using `setheading(angle)`.
  - Put the pen down with `pendown()` 
  - `distance`.
  - Update `startx` and `starty` --> `xcor()` and `ycor()`.
  - Increment the `angle` 
  - Increase the `distance` 
