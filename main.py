import pygame
import os

pygame.init()

WIDTH, HEIGHT = 700, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
FPS = 60
WHITE = (255,255,255)
AAA = (123,34,200)
BLACK = (0,0,0)
padd_width = 20
padd_height = 140



def draw(win, paddles):
  win.fill(WHITE)

  for pad in paddles:
    pad.draw(win)
    
  pygame.display.update()
  







class Paddle():
  COLOR = AAA
  VEL = 4
  def __init__(self, x, y ,width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def draw(self,win):
    pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

  def move(self, up = True):
    
    if up:
      self.y -= self.VEL
    else:
      self.y += self.VEL      
            
            
  




    
class Ball():
  def __init__(self, size):
    self.ball = 0



def handle_paddle_movement(keys, left_paddle, right_paddle):
  if keys[pygame.K_w]:
    left_paddle.move(up=True)
  if keys[pygame.K_s]:
    left_paddle.move(up=False)
  if keys[pygame.K_UP]:
    right_paddle.move(up=True)
  if keys[pygame.K_DOWN]:
    right_paddle.move(up=False)
    



    
def main():

  right_paddle = Paddle(WIDTH - 10 - padd_width, HEIGHT//2 - padd_height // 2,padd_width,padd_height )
  
  left_paddle = Paddle(10, HEIGHT//2 - padd_height // 2,padd_width,padd_height )
  
  run = True
  clock = pygame.time.Clock()
  
  while run:
    clock.tick(FPS)
    draw(win, [left_paddle, right_paddle])
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
  #
  
    keys = pygame.key.get_pressed()
    handle_paddle_movement(keys, left_paddle, right_paddle)
  pygame.quit()






#main()
 
if __name__ == "__main__":
  main()
 
    
chars = "interesting"

