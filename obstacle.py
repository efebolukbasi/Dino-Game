import random

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class Obstacle:
  x = 0
  y = 0
  
  def __init__(self, x, y, height, width):
    self.x = x
    self.y = y 
    self.color = colors[random.randint(1, len(colors) -1)]
    self.height = height
    self.width = width

  def move(self, dx):
    self.x += dx
    