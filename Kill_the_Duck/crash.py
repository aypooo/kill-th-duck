  def Crash (a,b):
        if a.x-b.get_x <= b.x and b.x <= a.x + a.get_x:
            if (a.y-b.get_y <= b.y) and (b.y <= a.y+a.get_y):
                return True
            else:
                return False
        else:
            return False







