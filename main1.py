#点集
#起止点
origin
remote
dataSet =[]
dataSet.append(origin)
dataSet.append(remote)








###退出条件###
#当储备列表的数目为4时退出
#当所求点为上一个输入点时
next = Point(-1,-1)
while( (len(dataSet)) == 4 or):
#当前点取点集倒数第二个
current = dataSet[-2]











###点的定义###
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return  "point x,y : %f \t %f"%(self.x,self.y)
############

###边（线段）的定义###
class Edge():
    def __init__(self,A,B):
        a = B.y - A.y
        b = A.x - B.x
        c = B.x * A.y - A.x * B.y
        #第一个点
        self.p1 = A
        #第二个点
        self.p2 = B
        #线段的直线方程参数
        self.constant = [a,b,c]
############

###矩形的定义###
class Area():
    def __init__(self,x,y,w,h):
    #左下角基准点
        self.x = x
        self.y = y
    #宽与高
        self.w = w
        self.h = h     
        
        
        
