import object
class crach:

    def Crash (a,b):
        if self.a.x-self.b.get_x <= self.b.x and self.b.x <= self.a.x + self.a.get_x:
            if (self.a.y-self.b.get_y <= self.b.y) and (self.b.y <= self.a.y+self.a.get_y):
                return True
            else:
                return False
        else:
            return False






db_list = []

for i in range(len bullet_list)):
    b = bullet_list[i]
    if Crash(b,enermy) == True:
        enermy_lifr -= 1
        db_list.append(i)
db_list = list(set(dm_list))
db_list.reverse()
try:
    for db in db_list:
        del m_list[db]
except:
    pass

for i in range(len(e_bullet_list)):
    e = e_bullet_list[i]
    if Crash(e, player) == True:
        player_life -= 1
