class Subject():
    def __init__(self,constant):
        self.a = constant[0]
        self.b = constant[1]
        self.c = constant[2]
    def setFlag(self,p):
        flag = self.a*p.x + self.b*p.y +self.c
        if flag >0 :
            self.flag = 1
        elif flag<0 :
            self.flag = -1
        else:
            self.flag = 0
    def setCheck(self,boolFlag):
        self.boolFlag = boolFlag
        
    def __str__(self):
        return "Subject\n a,b,c :  %f%f%f \t user_flag: %s \t boolFlag:%s"%(self.a,self.b,self.c,self.flag,self.boolFlag)
