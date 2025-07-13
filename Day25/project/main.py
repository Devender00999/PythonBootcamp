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
guessed_states = []

score = 0
game_is_on = True
while (game_is_on):
   state = screen.textinput(f"{score}/50 Guess the state", "What's the name of the state in US").title()
   if (state == 'Exit'):
      missing_states = [state for state in states['state'].to_list() if state not in guessed_states]
      # for state in states['state'].to_list():
      #    if state not in guessed_states:
      #       missing_states.append(state)
      missing = pandas.DataFrame(missing_states)
      missing.to_csv('missed_states.csv')
      
      
      break
   current_state = states[states['state'] == state]
   if len(current_state['state']) == 1 and state not in guessed_states:
      x, y = current_state.x.item(), current_state.y.item()
      turtle.goto(x, y)
      turtle.write(state.title(), font=('Times', 10, 'bold'))
      guessed_states.append(state)
      score += 1
   if score == 50:
      game_is_on = False
   

screen.mainloop()