import pygame
import os

pygame.init()


###################
###   VARS      ###
###################
WIDTH, HEIGHT = 700, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
FPS = 60
WHITE = (255,255,255)
AAA = (123,34,200)
BLACK = (0,0,0)
padd_width = 20
padd_height = 140



  



###################
###   CLASSES   ###
###################
  
class Ball():
  
  MAX_VEL = 5

  def __init__(self, x, y ,radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.x_vel = self.MAX_VEL
    self.y_vel = 0

  
  def draw(self,win):
    pygame.draw.circle(win, AAA, (self.x, self.y) , self.radius)

  
  def move(self):
    self.x += self.x_vel
    self.y += self.y_vel  





    




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
            
            
  









#########################
###  UTIL FUNCTIONS   ###
#########################

def draw(win, paddles, ball):
  win.fill(WHITE)

  for pad in paddles:
    pad.draw(win)

  for i in range(10, HEIGHT, HEIGHT // 20):
    if i % 2 == 1:
      continue
    pygame.draw.rect(win, AAA, (WIDTH//2-5, i, 10, HEIGHT //20))

  ball.draw(win)
  pygame.display.update()










def handle_collision(ball, left_paddle, right_paddle):
  if ball.y + ball.radius >= HEIGHT:
    ball.y_vel *= -1
  elif ball.y - ball.radius <= 0:
    ball.y_vel *= -1

  if ball.x_vel < 0: 
    if ball.y >= left_paddle.y and ball.y <= left_paddle.height:
      if ball.x - ball.radius  <= left_paddle.x + left_paddle.width:
        ball.x_vel *= -1
        
  else: 
    if ball.y >= right_paddle.y and ball.y <= right_paddle.height:
      if ball.x + ball.radius  >= right_paddle.x:
        ball.x_vel *= -1








    

def handle_paddle_movement(keys, left_paddle, right_paddle):
  
  if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
    left_paddle.move(up=True)
  if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
    left_paddle.move(up=False)
  
  if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
    right_paddle.move(up=True)
  if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
    right_paddle.move(up=False)
    



    
def main():

  right_paddle = Paddle(WIDTH - 10 - padd_width, HEIGHT//2 - padd_height // 2,padd_width,padd_height )
  
  left_paddle = Paddle(10, HEIGHT//2 - padd_height // 2,padd_width,padd_height )

  ball = Ball(WIDTH//2, HEIGHT//2, 33)
  
  run = True
  clock = pygame.time.Clock()
  
  while run:
    clock.tick(FPS)
    draw(win, [left_paddle, right_paddle], ball)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
  
    keys = pygame.key.get_pressed()
    
    handle_paddle_movement(keys, left_paddle, right_paddle)
    ball.move()

    
  pygame.quit()






#main()
 
if __name__ == "__main__":
  main()
 
    
chars = "interesting"

