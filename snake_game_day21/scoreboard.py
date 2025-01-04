from turtle import Turtle

ALIGNMENT = "center"
FONT=('courier', 24, 'normal')


def get_high_score():
    try:
        with open("data.txt", "r") as file:
            high_score = int(file.read().strip())
    except Exception as e:
        print(f"Error reading from file: {e}")
        high_score = 0
    return high_score


def save_high_score(score):
     try:
         with open("data.txt", "w") as file:
             file.write(f"{score}")
     except Exception as e:
         print(f"Error reading from file: {e}")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def reset(self):
        if self.score > get_high_score():
            # self.high_score = self.score
            save_high_score(self.score)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score: {get_high_score()}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()



