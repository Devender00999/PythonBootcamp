from turtle import Turtle, Screen
import pandas

turtle = Turtle()
image = 'blank_states_img.gif'
screen = Screen()
screen.title("Name the States")
turtle.penup()
turtle.hideturtle()
screen.bgpic(image)
screen.setup(width=725, height=491)

# importing data
states = pandas.read_csv('50_states.csv')
print(states[states['state'] == "Alabama"].to_dict())

score = 0
game_is_on = True
while (game_is_on):
   state = screen.textinput(f"{score}/50 Guess the state", "What's the name of the state in US").title()
   current_state = states[states['state'] == state]
   if len(current_state['state']) == 1:
      x, y = current_state.x.item(), current_state.y.item()
      turtle.goto(x, y)
      turtle.write(state.title(), font=('Times', 10, 'bold'))
      score += 1

screen.mainloop()