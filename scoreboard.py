from turtle import Turtle
import json
COLOR = "white"
POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ('Courier',18,'normal')

class Scoreboard(Turtle):
    def __init__(self,datafile_location):
        super().__init__()
        self.goto(POSITION)
        self.color(COLOR)
        self.hideturtle()
        self.score = 0
        self.datafile = datafile_location
        self.read_scores()
        self.update_scoreboard()


    def read_scores(self):
        i = 0
        with open(self.datafile, 'r') as file:
            contents = file.read()
            self.highscore = int(contents)

    def write_scores(self):
        with open(self.datafile, 'w') as file:
            file.write(str(self.highscore))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_scores()
            #name = "FCB"
            #json_dump = [name,self.highscore]
            #json.dump(json_dump, self.datafile)


        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()






#    def game_over(self):
#        self.goto(0,0)
#        self.write("GAME OVER",align=ALIGNMENT, font=FONT)