import pygame
import sys
import random 

pygame.init()
clock = pygame.time.Clock() 
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
gracz=1
font=pygame.font.SysFont("Arial",50)
title_font=pygame.font.SysFont("Arial",100)
graj=font.render("Graj",True,black)
title=title_font.render("Dixit",True,black)
zasady=font.render("Zasady",True,black)
wyjdz=font.render("Wyjdź",True,black)
wroc=font.render("Wróć",True,black)
wybor1=font.render("Wybierz ilość graczy",True,black)
wybor2=font.render("Wybierz ilość punktów",True,black)
choose=font.render("Wybierz",True,black)
wybgr1=font.render("3",True,black)
wybgr2=font.render("4",True,black)
wybgr3=font.render("5",True,black)
wybpun1=font.render("10",True,black)
wybpun2=font.render("20",True,black)
wybpun3=font.render("30",True,black)
wygrana=title_font.render("",True,black)
button1_img=pygame.image.load('blok1.jpg')
button2_img=pygame.image.load('blok2.jpg')
button3_img=pygame.image.load('blok3.jpg')
input_rect = pygame.Rect(100, 150, 300, 75)
opcje=0
il_graczy=0
il_pkt=0
karty=[]
wybrane=[[],[],[],[],[]]
uzyte=[[],[],[],[],[]]
gracz_start=1
count=0
card1=0
card2=1
card3=2
card4=3
card5=4
zagrana=0
user_text = ''
plik=open('plik.txt','r')
ekran=False
tura=1
voting=1
gracz_wyb=1
votes=[]
gracz_punkty=[0,0,0,0,0,0]
for line in plik:
    count+=1
    karty.append(line.strip())
plik.close()

active = False
start=False
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))


while True:
      
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(ev.pos):
                active = True
            else:
                active = False
  
        if ev.type == pygame.KEYDOWN and gracz==gracz_start:
  
         
            if ev.key == pygame.K_BACKSPACE:
  
                
                user_text = user_text[:-1]
  
           
            else:
                user_text += ev.unicode
              
    if(start==False):              
        if(opcje==0):
            screen.fill(color)
            Button1=Button(375,200,button1_img)
            Button2=Button(375,400,button2_img)
            Button3=Button(375,600,button3_img)
            Back=Button(50,650,button1_img)
            position=pygame.mouse.get_pos()
            Button1.draw()
            Button2.draw()
            Button3.draw()
            screen.blit(graj,(460,210))
            screen.blit(title,(410,25))
            screen.blit(zasady,(440,410))
            screen.blit(wyjdz,(440,610))
            
            if Button3.rect.collidepoint(position):
                            if pygame.mouse.get_pressed()[0]==1 and Button3.clicked==False:
                                Button3.clicked=True
                                pygame.quit()
                            if pygame.mouse.get_pressed()[0]==0:
                                Button3.clicked=False
            if Button2.rect.collidepoint(position):
                            if pygame.mouse.get_pressed()[0]==1 and Button2.clicked==False:
                                Button2.clicked=True
                                opcje=2
                            if pygame.mouse.get_pressed()[0]==0:
                                Button2.clicked=False
            if Button1.rect.collidepoint(position):
                            if pygame.mouse.get_pressed()[0]==1 and Button3.clicked==False:
                                Button1.clicked=True
                                opcje=1
                            if pygame.mouse.get_pressed()[0]==0:
                                Button1.clicked=False
                           
        elif(opcje==2):
            position=pygame.mouse.get_pos()
            screen.fill(color)
            screen.blit(zasady,(440,75))
            Back=Button(50,650,button1_img)
            Back.draw()
            screen.blit(wroc,(125,655))
            if Back.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Back.clicked==False:
                    Back.clicked=True
                    opcje=0
                if pygame.mouse.get_pressed()[0]==0:
                    Back.clicked=False
                            
        
       
        elif (opcje==1):
            position=pygame.mouse.get_pos()
            screen.fill(color)
            Players1=Button(75,250,button2_img)
            Players2=Button(375,250,button2_img)
            Players3=Button(675,250,button2_img)
            Points1=Button(75,500,button3_img)
            Points2=Button(375,500,button3_img)
            Points3=Button(675,500,button3_img)
            Players1.draw()
            Players2.draw()
            Players3.draw()
            Points1.draw()
            Points2.draw()
            Points3.draw()
            screen.blit(wybor1,(300,100))
            screen.blit(wybor2,(300,400))
            screen.blit(wybgr1,(190,260))
            screen.blit(wybgr2,(490,260))
            screen.blit(wybgr3,(790,260))
            screen.blit(wybpun1,(180,510))
            screen.blit(wybpun2,(480,510))
            screen.blit(wybpun3,(780,510))
            if Players1.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Players1.clicked==False:
                    Players1.clicked=True
                    il_graczy=3
                if pygame.mouse.get_pressed()[0]==0:
                    Players1.clicked=False
            if Players2.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Players2.clicked==False:
                    Players2.clicked=True
                    il_graczy=4
                if pygame.mouse.get_pressed()[0]==0:
                    Players2.clicked=False
            if Players3.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Players3.clicked==False:
                    Players3.clicked=True
                    il_graczy=5
                if pygame.mouse.get_pressed()[0]==0:
                    Players3.clicked=False
            if Points1.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Points1.clicked==False:
                    Points1.clicked=True
                    il_pkt=10
                if pygame.mouse.get_pressed()[0]==0:
                    Points1.clicked=False
            if Points2.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Points2.clicked==False:
                    Points2.clicked=True
                    il_pkt=20
                if pygame.mouse.get_pressed()[0]==0:
                    Points2.clicked=False
            if Points3.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Points3.clicked==False:
                    Points3.clicked=True
                    il_pkt=30
                if pygame.mouse.get_pressed()[0]==0:
                    Points3.clicked=False
            if(il_graczy!=0 and il_pkt!=0):
                opcje=3
                for i in range(il_graczy):
                    for j in range(5):
                        uzyte[i].append(random.randint(0,59))
                      
                        
                print(uzyte)
        elif(opcje==3):
            if(ekran==False):
                screen.fill(color)
                if gracz==gracz_start:
                    skojarzenie=font.render('Wpisz skojarzenie:', True, black)
                if gracz!=gracz_start:
                    skojarzenie=font.render('Podane skojarzenie to:', True, black)
                    
                position=pygame.mouse.get_pos()
                pygame.draw.rect(screen, green, input_rect)
                text_surface = font.render(user_text, True, (255, 255, 255))
                screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                input_rect.w = max(100, text_surface.get_width()+10)
                karta1=Button(50,300,pygame.image.load(karty[uzyte[gracz-1][0]]))
                karta2=Button(250,300,pygame.image.load(karty[uzyte[gracz-1][1]]))
                karta3=Button(450,300,pygame.image.load(karty[uzyte[gracz-1][2]]))
                karta4=Button(650,300,pygame.image.load(karty[uzyte[gracz-1][3]]))
                karta5=Button(850,300,pygame.image.load(karty[uzyte[gracz-1][4]]))
                wybierz=Button(375,650,button1_img)
                screen.blit(skojarzenie, (100,50))
                karta1.draw()
                karta2.draw()
                karta3.draw()
                karta4.draw()
                karta5.draw()
                
                wybierz.draw()
                screen.blit(choose,(425,650))
                if karta1.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta1.clicked==False:
                        karta1.clicked=True
                        zagrana=1
                    if pygame.mouse.get_pressed()[0]==0:
                        karta1.clicked=False
                if karta2.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta2.clicked==False:
                        karta2.clicked=True
                        zagrana=2
                    if pygame.mouse.get_pressed()[0]==0:
                        karta2.clicked=False
                if karta3.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta3.clicked==False:
                        karta3.clicked=True
                        zagrana=3
                    if pygame.mouse.get_pressed()[0]==0:
                        karta3.clicked=False
                if karta4.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta4.clicked==False:
                        karta4.clicked=True
                        zagrana=4
                    if pygame.mouse.get_pressed()[0]==0:
                        karta4.clicked=False
                if karta5.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta5.clicked==False:
                        karta5.clicked=True
                        zagrana=5
                    if pygame.mouse.get_pressed()[0]==0:
                        karta5.clicked=False
                if wybierz.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and wybierz.clicked==False and zagrana!=0:
                        wybierz.clicked=True
                        if zagrana==1:
                            wybrane[gracz-1].append(uzyte[gracz-1][0])
                            uzyte[gracz-1][0]=random.randint(0,59)
                            zagrana=0
                        if zagrana==2:
                            wybrane[gracz-1].append(uzyte[gracz-1][1])
                            uzyte[gracz-1][1]=random.randint(0,59)
                            zagrana=0
                        if zagrana==3:
                            wybrane[gracz-1].append(uzyte[gracz-1][2])
                            uzyte[gracz-1][2]=random.randint(0,59)
                            zagrana=0
                        if zagrana==4:
                            wybrane[gracz-1].append(uzyte[gracz-1][3])
                            uzyte[gracz-1][3]=random.randint(0,59)
                            zagrana=0
                        if zagrana==5:
                            wybrane[gracz-1].append(uzyte[gracz-1][4])
                            uzyte[gracz-1][4]=random.randint(0,59)
                            zagrana=0
                        ekran=True
                        gracz+=1
                        tura+=1
                        if gracz>il_graczy:
                            gracz=1
             
                        ekranik=title_font.render("Gracz nr "+str(gracz),True,black)
                    if pygame.mouse.get_pressed()[0]==0:
                        wybierz.clicked=False
                    
            elif(ekran==True and tura<=il_graczy):
                screen.fill(color)
                position=pygame.mouse.get_pos()
                Button2.draw()
                screen.blit(graj,(460,410))
                screen.blit(ekranik,(300,200))
                if Button2.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and Button2.clicked==False:
                        Button2.clicked=True
                        ekran=False
                    if pygame.mouse.get_pressed()[0]==0:
                        Button2.clicked=False
            elif (ekran==True and tura>il_graczy and voting<=il_graczy):
                screen.fill(color)
                position=pygame.mouse.get_pos()
                wybierz.draw()
                screen.blit(graj,(460,410))
                karta1=Button(50,300,pygame.image.load(karty[wybrane[0][0]]))
                karta2=Button(250,300,pygame.image.load(karty[wybrane[1][0]]))
                karta3=Button(450,300,pygame.image.load(karty[wybrane[2][0]]))
                karta1.draw()
                karta2.draw()
                karta3.draw()
                if gracz_wyb==gracz_start:
                    gracz_wyb+=1
                if il_graczy==4:
                    karta4=Button(650,300,pygame.image.load(karty[wybrane[3][0]]))
                    karta4.draw()
                if il_graczy==5:
                    karta4=Button(650,300,pygame.image.load(karty[wybrane[3][0]]))
                    karta5=Button(850,300,pygame.image.load(karty[wybrane[4][0]]))
                    karta5.draw()
                    karta4.draw()
                skojarzenie=font.render('gracz nr'+str(gracz_wyb)+" wybierz kartę", True, black)
                screen.blit(choose,(425,650))
                screen.blit(skojarzenie, (100,50))
                if karta1.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta1.clicked==False and gracz_wyb!=1:
                        karta1.clicked=True
                        zagrana=1
                    if pygame.mouse.get_pressed()[0]==0:
                        karta1.clicked=False
                if karta2.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta2.clicked==False and gracz_wyb!=2:
                        karta2.clicked=True
                        zagrana=2
                    if pygame.mouse.get_pressed()[0]==0:
                        karta2.clicked=False
                if karta3.rect.collidepoint(position):
                    if pygame.mouse.get_pressed()[0]==1 and karta3.clicked==False and gracz_wyb!=3:
                        karta3.clicked=True
                        zagrana=3
                    if pygame.mouse.get_pressed()[0]==0:
                        karta3.clicked=False
                if karta4.rect.collidepoint(position) and (il_graczy==4 or il_graczy==5)and gracz_wyb!=4:
                    if pygame.mouse.get_pressed()[0]==1 and karta4.clicked==False:
                        karta4.clicked=True
                        zagrana=4
                    if pygame.mouse.get_pressed()[0]==0:
                        karta4.clicked=False
                if karta5.rect.collidepoint(position) and il_graczy==5:
                    if pygame.mouse.get_pressed()[0]==1 and karta5.clicked==False and gracz_wyb!=5:
                        karta5.clicked=True
                        zagrana=5
                    if pygame.mouse.get_pressed()[0]==0:
                        karta5.clicked=False
                if wybierz.rect.collidepoint(position) and zagrana!=0:
                    if pygame.mouse.get_pressed()[0]==1 and wybierz.clicked==False:
                        if zagrana==1:
                            votes.append(1)
                            zagrana=0
                        if zagrana==2:
                            votes.append(2)
                            zagrana=0
                        if zagrana==3:
                            votes.append(3)
                            zagrana=0
                        if zagrana==4:
                            votes.append(4)
                            zagrana=0
                        if zagrana==5:
                            votes.append(5)
                            zagrana=0
                        wybierz.clicked=True
                        voting+=1
                        gracz_wyb+=1
                        if gracz_wyb>il_graczy and voting<il_graczy:
                            gracz_wyb=1
                        if voting==il_graczy:
                            for i in votes:
                                gracz_punkty[i-1]+=1
                            for i in range(il_graczy):
                                if gracz_punkty[i]>=il_pkt:
                                    opcje=4
                                    screen.fill(color)
                                    wygrana=title_font.render("Wygrywa gracz nr "+ str(i+1)+"!",True,black)
                            votes.clear()
                            wybrane=[[],[],[],[],[],[]]
                            screen.fill(color)
                            print(votes)
                            print(wybrane)
                            print(gracz_punkty)
                            tura=1
                            gracz_start+=1
                            gracz=gracz_start
                            gracz_wyb=1
                            voting=1
                            screen.fill(color)
                            
                            position=pygame.mouse.get_pos()
                            wybierz.draw()
                            screen.blit(graj,(460,410))
                            
                            if gracz_start>il_graczy:
                                gracz_start=1
                                gracz=gracz_start
                            ekranik=title_font.render("Gracz nr "+str(gracz),True,black)
                            screen.blit(ekranik,(300,200))
                        
                    if pygame.mouse.get_pressed()[0]==0:
                        wybierz.clicked=False
        elif(opcje==4):
            screen.fill(color)
            screen.blit(wygrana,(100,200))
            position=pygame.mouse.get_pos()
            Button2=Button(375,500,button2_img)
            Button2.draw()
            screen.blit(graj,(460,510))
            if Button2.rect.collidepoint(position):
                if pygame.mouse.get_pressed()[0]==1 and Button2.clicked==False:
                    Button2.clicked=True
                    votes.clear()
                    wybrane=[[],[],[],[],[],[]]
                    il_graczy=0
                    il_pkt=0
                    uzyte=[[],[],[],[],[]]
                    gracz_start=1
                    ekran=False
                    tura=1
                    voting=1
                    gracz_wyb=1
                    gracz=1
                    votes=[]
                    gracz_punkty=[0,0,0,0,0,0]
                    opcje=0
                if pygame.mouse.get_pressed()[0]==0:
                    Button2.clicked=False
            
        pygame.display.update()
        clock.tick(60)
