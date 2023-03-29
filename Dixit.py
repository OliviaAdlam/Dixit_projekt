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
wroc=font.render("Wróć",True,black)
wybor1=font.render("Wybierz ilość graczy",True,black)
wybor2=font.render("Wybierz ilość punktów",True,black)
wybgr1=font.render("4",True,black)
wybgr2=font.render("5",True,black)
wybgr3=font.render("6",True,black)
wybpun1=font.render("10",True,black)
wybpun2=font.render("20",True,black)
wybpun3=font.render("30",True,black)
start=False
while True:
      
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()
              
    if(start==False):              
        
        screen.fill(color)
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(screen,blue,[375,200,250,75])
        pygame.draw.rect(screen,green,[375,400,250,75])
        pygame.draw.rect(screen,yellow,[375,600,250,75])
        screen.blit(graj,(460,210))
        screen.blit(zasady,(440,410))
        screen.blit(wyjdz,(440,610))
        if pygame.mouse.get_pressed()[0]==1 and 375 <= mouse[0] <= 625 and 600 <= mouse[1] <= 675:
            pygame.quit()
        elif pygame.mouse.get_pressed()[0]==1 and 375 <= mouse[0] <= 625 and 400 <= mouse[1] <= 475:
            start=True
            mouse = pygame.mouse.get_pos()
            screen.fill(color)
            screen.blit(zasady,(440,75))
            pygame.draw.rect(screen,blue,[50,650,100,75])
            screen.blit(wroc,(53,655))
            if pygame.mouse.get_pressed()[0]==1 and 50 <= mouse[0] <= 150 and 650 <= mouse[1] <= 725:
                start=True
        elif pygame.mouse.get_pressed()[0]==1 and 375 <= mouse[0] <= 625 and 200 <= mouse[1] <= 275:
            start=True
            screen.fill(color)
            pygame.draw.rect(screen,yellow,[100,250,200,75])
            pygame.draw.rect(screen,yellow,[400,250,200,75])
            pygame.draw.rect(screen,yellow,[700,250,200,75])
            pygame.draw.rect(screen,green,[100,500,200,75])
            pygame.draw.rect(screen,green,[400,500,200,75])
            pygame.draw.rect(screen,green,[700,500,200,75])
            screen.blit(wybor1,(300,100))
            screen.blit(wybor2,(300,400))
            screen.blit(wybgr1,(190,260))
            screen.blit(wybgr2,(490,260))
            screen.blit(wybgr3,(790,260))
            screen.blit(wybpun1,(180,510))
            screen.blit(wybpun2,(480,510))
            screen.blit(wybpun3,(780,510))
            
            
        pygame.display.update()
