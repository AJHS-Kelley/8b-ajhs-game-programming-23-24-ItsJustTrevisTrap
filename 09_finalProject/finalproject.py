import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn.setup(700,700)

#Create Pen
class Pen(turtle.Turtle):
    def _init_(self):
        turtle.Turtle._init_(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Create levels list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Add maze to mazes list
levels.append(level_1)






