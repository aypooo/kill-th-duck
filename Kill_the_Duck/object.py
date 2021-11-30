import pygame


class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self, address): #오브젝트 이미지 불러오기
        if address[-3:] == "png":
            self.obj = pygame.image.load(address).convert_alpha()
        else:
            self.obj = pygame.image.load(address)
            self.get_x, self.get_y = self.obj.get_size() #오브젝트의 x,y 사이즈를 가져옴 
    
    def resize(self, resize_x, resize_y): #오브젝트 스케일 변경
        self.obj = pygame.transform.scale(self.obj,(resize_x,resize_y)) 
        self.get_x, self.get_y = self.obj.get_size() #바뀐 오브젝트의 크기를 다시 가져옴
    
    def show(self,screen):
        screen.blit(self.obj,(self.x,self.y))    
       
        

