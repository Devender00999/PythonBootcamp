# Move 
# https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_robot():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    move_robot()

