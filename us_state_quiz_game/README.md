### U.S State Quiz Game
`def get_mouse_click_coor(x,y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)`

get coor by position mouse click

### TODO
1. [x] Convert the guess to the Title case
2. [x] Check if the guess is among the 50 states
3. [x] Write the correct guesses onto the map 
4. [x] Use a loop to allow the user to keep guessing 
5. [x] Record the correct guesses in a list
6. [x] Keep track of the score 


### Learnings
- Apply List Comprehension 

 missing_states = [state for state in all_states if state not in guessed_states]