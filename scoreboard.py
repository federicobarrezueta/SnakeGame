from turtle import Turtle
COLOR = "white"
POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ('Courier',18,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(POSITION)
        self.color(COLOR)
        self.hideturtle()
        self.score = 0
        self.highscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

#    def game_over(self):
#        self.goto(0,0)
#        self.write("GAME OVER",align=ALIGNMENT, font=FONT)