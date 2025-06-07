# Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    if right_is_clear() and not at_goal():
        turn_right()
        move()
    if wall_on_right():
        turn_left()
    