# Move 
# https://reeborg.ca/reeborg.html

# Initial Solution 

move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_robot():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    move()
    
for i in range(5):
    move_robot()
   
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
build_wall()



# Final Solution
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

for i in range(6):
    move_robot()
    
build_wall()
