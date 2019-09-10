class Subject():
    #直线方程约束
    def __init__(self,constant):
        self.a = constant[0]
        self.b = constant[1]
        self.c = constant[2]
        
    #点p与直线方程约束关系
    def setFlag(self,p):
        flag = self.a*p.x + self.b*p.y +self.c
        if flag >0 :
            self.flag = 1
        elif flag<0 :
            self.flag = -1
        else:
            self.flag = 0   
                 
    def __str__(self):
        return "Subject\n a,b,c :  %f\t%f\t%f \t  flag: %s \t "%(self.a,self.b,self.c,self.flag)
