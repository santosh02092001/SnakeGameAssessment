# I acknowledge the use of ChatGPT (version GPT-5 Mini, OpenAI) to assist in creating this file.

import random
from turtle import Turtle

class Food(Turtle):
    # Food class spawns randomly on screen
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
