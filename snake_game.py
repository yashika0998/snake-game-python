import turtle       #library for python graphics
import time
import random

delay = 0.1
score=0
high_score=0

#module1
#building the screen
w = turtle.Screen()
w.title("Snake Game by yashika")
w.bgcolor("skyblue")
w.setup(width = 600, height = 600)
w.tracer(0) #turns off screen updates (makes faster)

#module 2
#making head of snake and moving around

head = turtle.Turtle()
head.speed(0)           #Animation speed not snake speed
head.shape("square")
head.color("green")     
head.penup()            #so that head does not draw anhing on screen
head.goto(0,0)          #in starting the head will be at centre of screen
head.direction = "stop"   #initial direction

#module 3
#Function that will aloow snake head to move
#step2)
def go_up():
    if head.direction != "down" :
        head.direction = "up"
def go_down():
    if head.direction != "up" :
        head.direction = "down"
def go_right():
    if head.direction != "left" :
        head.direction = "right"
def go_left():
    if head.direction != "right" :
        head.direction = "left"

#step1)
def move():
    if head.direction == "up" :
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down" :
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right" :
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left" :
        x = head.xcor()
        head.setx(x-20)
# keyboard bindings(connects a keypress with particular function)
w.listen()
w.onkeypress(go_up, "Up")
w.onkeypress(go_down, "Down")
w.onkeypress(go_right, "Right")
w.onkeypress(go_left, "Left")

#module4
#making food for snake
food = turtle.Turtle()
food.speed(0)           #Animation speed not snake speed
food.shape("circle")
food.color("black")     
food.penup()            #so that head does not draw anhing on screen
food.goto(0,100)          #in starting the head will be at centre of screen

segments = []

#module 8
#scoring of snake
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score : 0 High Score: 0" , align = "center" , font=("Courier",24,"normal"))


#module 3(adding other modules to call functions afterward
#Main game loop
while True:
    w.update()

    
        
    #checking snake eat the food
    if head.distance(food) <20 :
        #move the food to random places
        x = random.randint(-290,290)    #so that food doesnt go outside screen
        y = random.randint(-290,290)
        food.goto(x,y)

        #module5
        #making segments of body
        new_segment = turtle.Turtle()
        new_segment.speed(0)        #Animation speed
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -=0.001

        #increase the score
        score = score+1
        if score> high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} high Score: {}".format(score,high_score), align = 'center', font=("Courier",24, "normal"))
        
    #move the segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor() #to move body at back of head
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move body/segment 0 to where head is
    if len(segments) >0 :
       x = head.xcor()
       y = head.ycor()
       segments[0].goto(x,y)
       
    #module6
    #Check the collision with border
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor() > 290 or head.ycor() <-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"     #but when snake touches the boundary its segments are not dissaperaing so :-
        #hide the segments
        for segment in segments :
            segment.goto(1000,1000)
        #but code of module 5 is running continuosly beacause of which snakes body not getting to 0
        #so clearing the segments list
        segments.clear()
        #Reset the score
        score =0
        #reset the delay
        delay = 0.14

        #update the score display
        pen.clear()
        pen.write("Score: {} high Score: {}".format(score,high_score), align = 'center', font=("Courier",24, "normal"))

    
        

    
    move()

    #module 7
    #measue difference between head and tail
    #checking for collision between head and different segments of snake:

    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #hide the segments
            for segment in segments :
                segment.goto(1000,1000)
            #but code of module 5 is running continuosly beacause of which snakes body not getting to 0
            #so clearing the segments list
            segments.clear()
            
    time.sleep(delay)


w.mainloop()       #this will keep the window open for us





