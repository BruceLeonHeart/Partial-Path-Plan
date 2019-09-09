from point import Point
import mathTools
#定义边(线段)
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
        self.canBeChosed = True
    def getPointEdge(self,p):
        distance,crossPoint = mathTools.pointToLine(self.p1,self.p2,p)
        self.p = p
        self.distance = distance
        self.crossPoint = crossPoint
       
    def __str__(self):
        return 'a,b,c : %f\t%f\t%f distance: %f \tcanBeChosed: %f'%(self.constant[0],self.constant[1],self.constant[2],self.distance,self.canBeChosed)
        

