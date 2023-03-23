import pygame
import sys

pygame.init()
  
res = (1000,750)
screen = pygame.display.set_mode(res)
color = (112,128,144)
white=(255,255,255)
black=(0,0,0)
yellow = (255,236,139)
blue = (154,192,205)
green=(155,205,155)
width = screen.get_width()
height = screen.get_height()
font=pygame.font.SysFont("Arial",50)
graj=font.render("Graj",True,black)
zasady=font.render("Zasady",True,black)
wyjdz=font.render("Wyjdź",True,black) 
while True:
      
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
                  
    
    screen.fill(color)
    mouse = pygame.mouse.get_pos()
    pygame.draw.rect(screen,blue,[375,200,250,75])
    pygame.draw.rect(screen,green,[375,400,250,75])
    pygame.draw.rect(screen,yellow,[375,600,250,75])
    screen.blit(graj,(460,210))
    screen.blit(zasady,(440,410))
    screen.blit(wyjdz,(440,610))
    pygame.display.update()
