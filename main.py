import pygame, sys
from pygame.locals import *
from obstacle import *
from pygame import *


# global variables
score = 0

GROUND_Y = 330

OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHT = 50

OBSTACLE_INIT_X = 1000
OBSTACLE_INIT_Y = GROUND_Y - OBSTACLE_HEIGHT

OBSTACLE_INCREMENT = -5

FPS = 30 # frames per second setting
screen = pygame.display.set_mode((700, 600), 0, 32)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)

counter = 0






#___________________________
def genObstacle():
  newObs = Obstacle(OBSTACLE_INIT_X, OBSTACLE_INIT_Y, OBSTACLE_HEIGHT, OBSTACLE_WIDTH)
  obstacleList.append(newObs)

def moveAndDelObstacles(obsIncrement):
  """
    Moves obstacles towards  the dino
  """
  length = len(obstacleList)
  index = 0
  while index < length:
    if obstacleList[index].x < 0:
      print("off the grid")
      obstacleList.pop(index)
      length -= 1
    else:
      obstacleList[index].move(OBSTACLE_INCREMENT)
      index += 1

def renderObstacles():
  for obstacle in obstacleList:
    pygame.draw.rect(screen, obstacle.color, (obstacle.x, obstacle.y, obstacle.width, obstacle.height))

def scoreKeeper():
  if dinox == obstacle.x + 30:
    score += 1
    
pygame.init()

fpsClock = pygame.time.Clock()

# set up the window

pygame.display.set_caption('Animation')

obstacleList = []


dinoImg = pygame.image.load('dino.png')
dinoImg = pygame.transform.scale(dinoImg, (130, 80))
dinox = 100
dinoy = 250

dinoDir = 0

gameRunning = False

while True: # the main game loop
  screen.fill(GRAY)
  for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            dinoy -= 60
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_SPACE:
            dinoy += 60

          
  if dinoDir == 0:
    False

  if counter >= 100:
    print("Counter ticked")
    genObstacle()
    counter = 0
  else:
    counter += 1

  # Dino Jump

  


  moveAndDelObstacles(OBSTACLE_INCREMENT)
  renderObstacles()
  screen.blit(dinoImg, (dinox, dinoy))
  pygame.display.update()
  fpsClock.tick(FPS)


  font = pygame.font.SysFont('Calibri', 25, True, False)

  text = font.render("Score: ", True, (255, 125, 0))

  #screen.blit(text, [0, 0])
  pygame.display.flip()
  clock.tick(FPS)
  #print(obstacleList)
