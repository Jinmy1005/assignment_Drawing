from turtle import *

def draw_cat():
    speed(10) # Painting speed control
    bgcolor("yellow") #choose the background color
    pensize(10) #Define the pensize

    #head
    penup()
    goto(0, -100) #Move the pen to the target pixel
    pendown()
    circle(100) # Draw a circle with radius 100 at the left side of point

    #ear
    penup()
    goto(-60, 80)  # Move the pen to the target pixel
    pendown()
    seth(90) #set angle
    circle(100, 70) # draw a curve with radius 120, sector angle 31
    seth(-50) #set angle
    fd(50) #forward 45

    penup()
    goto(60, 80)  # Move the pen to the target pixel
    pendown()
    seth(90)  # set angle
    circle(-100, 70)  # draw a curve with radius 120, sector angle 31
    seth(-130)  # set angle
    fd(50)  # forward 45

    #eye
    penup()
    goto(-40, 50)
    pendown()
    begin_fill()
    color("black")
    circle(10)
    end_fill()

    penup()
    goto(40, 50)
    pendown()
    begin_fill()
    circle(10)
    end_fill()

    #mouse
    penup()
    goto(0, -20)
    pendown()
    circle(20,90)
    penup()
    goto(0, -20)
    pendown()
    circle(20,-90)

    #beard
    penup()
    goto(60, 10)
    pendown()
    seth(10)
    fd(100)

    penup()
    goto(60, -10)
    pendown()
    seth(0)
    fd(100)

    penup()
    goto(60, -30)
    pendown()
    seth(-10)
    fd(100)

    penup()
    goto(-60, 10)
    pendown()
    seth(170)
    fd(100)

    penup()
    goto(-60, -10)
    pendown()
    seth(180)
    fd(100)

    penup()
    goto(-60, -30)
    pendown()
    seth(190)
    fd(100)

    #flower
    penup()
    goto(50, 100)
    pendown()
    begin_fill()
    color("red")
    circle(15)
    end_fill()

    penup()
    goto(35, 120)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    penup()
    goto(65, 120)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    done()


print("----- Welcome to the drawing system ----")
draw_cat()