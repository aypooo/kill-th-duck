import pygame 
import object


pygame.init()

size = [900,400] #창사이즈를 배열로 받음
screen = pygame.display.set_mode(size)

title = "KILL THE DUCK"
pygame.display.set_caption(title)

clock = pygame.time.Clock()

#플레이어 캐릭터
player = object.obj()
player.put_img("./png/character.png")
player.resize(60,60)
player.x = 15 #플레이어 캐릭터 위치 초기화
player.y = round(size[1]/2-player.get_y/2)
player.move = 5

enermy = object.obj()
enermy.put_img("./png/duck.png")
enermy.resize(300,300)
enermy.x = size[0]-enermy.get_y -30 #플레이어 캐릭터 위치 초기화
enermy.y = round(size[1]/2-enermy.get_y/2)
enermy.move = 5





left_go = False
right_go = False
up_go = False
down_go = False
space_go = False

bullet_list = []

black = (0,0,0)
white = (255,255,255)

k = 0

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
        
    if left_go == True: #x,y 이동 범위 지정
        player.x -= player.move
        if player.x <= 0:
            player.x = 0
    elif right_go == True:
        player.x += player.move
        if player.x >= size[0]-player.get_x:
            player.x = size[0]-player.get_x
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
    
    
    d_list = []
    for i in range(len(bullet_list)): #총알을 여러발 쏠 수 있게 
        b = bullet_list[i]
        b.x += b.move
        if b.x >= size[0]: #총알이 화면 범위를 벗어나면 삭제
            d_list.append(i) #삭제 리스트에 값을 저장
    d_list.reverse
    for d in d_list: #for문으로 삭제리스트에 저장한 값으로 총알을 삭제 
        del bullet_list[d]

   
    #구현
    screen.fill(black)#배경색
    for bullet in bullet_list:#총알 구현
        bullet.show(screen)
 
    player.show(screen)
    enermy.show(screen)
    pygame.display.flip()
    

pygame.quit()



