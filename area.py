from point import Point
#区域
class Area():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def isPointIn(self,p):
        if( (self.x < p.x) and (self.x +self.w > p.x) and (self.y<p.y) and (self.y+self.h > p.y)):
            return 1
        return 0
