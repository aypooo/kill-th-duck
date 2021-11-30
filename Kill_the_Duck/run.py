import pygame 
import object
from datetime import datetime
import random


pygame.init()

size = [900,400] #창사이즈를 배열로 받음
screen = pygame.display.set_mode(size)

title = "KILL THE DUCK"
pygame.display.set_caption(title)

clock = pygame.time.Clock()


def Crash (a,b):
    if a.x-b.get_x <= b.x and b.x <= a.x + a.get_x:
        if (a.y-b.get_y <= b.y) and (b.y <= a.y+a.get_y):
            return True
        else:
            return False
    else:
        return False


#플레이어 캐릭터
player = object.obj()
player.put_img("./png/character.png")
player.resize(30,20)
player.x = 15 #플레이어 캐릭터 위치 초기화
player.y = round(size[1]/2-player.get_y/2)
player.move = 5

enermy = object.obj()
enermy.put_img("./png/duck.png")
enermy.resize(200,200)
enermy.x = size[0]-enermy.get_y-20 #플레이어 캐릭터 위치 초기화
enermy.y = round(size[1]/2-enermy.get_y/2)
enermy.move = 5

enermy_life = 200
player_life = 3

enermy_crash = False
player_crash = False
left_go = False
right_go = False
up_go = False
down_go = False
space_go = False


bullet_list = []
e_bullet_list =[]
e_bullet1_list =[]

black = (0,0,0)
k = 0
ek = 0
go = False
run = True
while run == True:
    clock.tick(60)
    for event in pygame.event.get(): #입력감지
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: # 키 입력 
            if event.key == pygame.K_LEFT:
                left_go = True 
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_UP:
                up_go = True
            elif event.key == pygame.K_DOWN:
                down_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0
            elif event.key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_UP:
                up_go = False
            elif event.key == pygame.K_DOWN:
                down_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False

  
    #x,y 이동 범위 지정    
    if left_go == True: 
        player.x -= player.move
        if player.x <= 0:
            player.x = 0
    elif right_go == True:
        player.x += player.move
        if player.x >= size[0]-enermy.get_y -10:
            player.x = size[0]-enermy.get_y -10 
    elif up_go == True:
        player.y -= player.move
        if player.y <= 0:
            player.y = 0
    elif down_go == True:
        player.y += player.move
        if player.y >= size[1]-player.get_y:
            player.y = size[1]-player.get_y
    k += 1
    if space_go == True and k % 6 == 0: #총알 위치 지정
        bullet = object.obj()
        bullet.put_img("./png/bullet.png")
        bullet.resize(6,6)
        bullet.x = player.x+player.get_x + 5
        bullet.y = round(player.y+player.get_y/2)-3
        bullet.move = 20
        bullet_list.append(bullet)
    #플레이어 총알
    d_list = []
    for i in range(len(bullet_list)): #총알을 여러발 쏠 수 있게 
        b = bullet_list[i]
        b.x += b.move
        if b.x >= size[0]: #총알이 화면 범위를 벗어나면 삭제
            d_list.append(i) #삭제 리스트에 값을 저장
    d_list.reverse
    for d in d_list: #for문으로 삭제리스트에 저장한 값으로 총알을 삭제 
        del bullet_list[d]

    if enermy_life >=0 or player_life >=0:
        if random.random() >0.96:
            for i in range(2):
                e_bullet = object.obj()        
                e_bullet.put_img("./png/e_bullet.png")
                e_bullet.resize(20,20)                
                e_bullet.x = size[0]-enermy.get_x -10                    
                e_bullet.y = random.randrange(0, size[1])
                e_bullet.move = 4
                e_bullet_list.append(e_bullet)
        if random.random() >0.98:
            for i in range(2):
                e_bullet1 = object.obj()        
                e_bullet1.put_img("./png/e_bullet.png")
                e_bullet1.resize(10,10)
                e_bullet1.x = size[0]-enermy.get_x -10
                e_bullet1.y = random.randrange(0, size[1])
                e_bullet1.move = 2
                e_bullet1_list.append(e_bullet1)
            
    ed_list = []
    for i in range(len(e_bullet_list)): #총알을 여러발 쏠 수 있게 
        e = e_bullet_list[i]
        e.x -= e.move
        if e.x <= -50: #총알이 화면 범위를 벗어나면 삭제
            ed_list.append(i) #삭제 리스트에 값을 저장
    ed_list.reverse()
    for d in ed_list: #for문으로 삭제리스트에 저장한 값으로 총알을 삭제 
        del e_bullet_list[d]
    ed_list1 = []
    for i in range(len(e_bullet1_list)): #총알을 여러발 쏠 수 있게 
        e = e_bullet1_list[i]
        e.x -= e.move
        if e.x <= -50: #총알이 화면 범위를 벗어나면 삭제
            ed_list1.append(i) #삭제 리스트에 값을 저장
    ed_list1.reverse()
    for d in ed_list1: #for문으로 삭제리스트에 저장한 값으로 총알을 삭제 
        del e_bullet1_list[d]

    #총알 충돌 판정 구현
    db_list = []
    eb_list = []
    for i in range(len(bullet_list)):
        b = bullet_list[i]
        enermy_crash = Crash(b,enermy)
        if enermy_crash == True:
            db_list.append(i)
            enermy_life -= 1
    db_list = list(set(db_list))
    db_list.reverse()
   
    for i in range(len(e_bullet_list)):
        e = e_bullet_list[i]
        player_crash = Crash(e,player)
        if player_crash == True:
            player_life -= 1
            eb_list.append(i)
    eb_list = list(set(eb_list))
    
    for i in range(len(e_bullet1_list)):
        e = e_bullet1_list[i]
        if Crash(e, player) == True:
            player_life -= 1
            eb_list.append(i)
    eb_list = list(set(eb_list))
    eb_list.reverse()

    try:
        for db in db_list:
            del bullet_list[db]
        for db in eb_list:
            del e_bullet_list[db]
        for db in eb_list:
            del e_bullet1_list[db]
    except:
        pass

    if enermy_life == 0:
        run = False 
    if player_life == 0:
        run = False  #충돌하면 종료



   
    #구현
    screen.fill(black)#배경색
    for bullet in bullet_list:#총알 구현
        bullet.show(screen)
    for e_bullet in e_bullet_list:#총알 구현
        e_bullet.show(screen)
    for e_bullet1 in e_bullet1_list:#총알 구현
        e_bullet1.show(screen)

    # font = pygame.font.Font("./font/AmaticSC-Bold.ttf",20)
    # text = font.render("YOU DIED",True,(255,255,255))
    # screen.blit(text(100,100))
 
    player.show(screen)
    enermy.show(screen)
    pygame.display.flip()


pygame.quit()



