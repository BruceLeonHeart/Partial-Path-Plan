from point import Point
#from obstacle import Obstacle
from math import sqrt
from math import pow
from math import factorial
import matplotlib.pyplot as plt
import numpy as np
#数学工具
def point2point(A,B):
    a = B.y - A.y
    b = A.x - B.x
    c = B.x * A.y - A.x * B.y
    return [a,b,c]




##点P到线段AB距离以及交点坐标以及点P与交点直线方程
def pointToLine(A,B,P):
    ap_ab = (B.x - A.x)*(P.x - A.x)+(B.y - A.y)*(P.y - A.y)
    crossPoint = Point(0,0)
    if(ap_ab <= 0):
        distance =  sqrt( (P.x-A.x)*(P.x-A.x) + (P.y-A.y)*(P.y-A.y) )
        crossPoint = A
        z = point2point(P,crossPoint)
        return distance,crossPoint,z
 
    d2 = ( B.x - A.x ) * ( B.x - A.x ) + ( B.y-A.y ) * ( B.y-A.y ) 
    if (ap_ab >= d2):  
        distance = sqrt( (P.x - B.x )*( P.x - B.x ) + ( P.y - B.y )*( P.y - B.y ) ) 
        crossPoint = B
        z = point2point(P,crossPoint)
        return distance,crossPoint,z
    
    r = ap_ab / d2
    px = A.x + ( B.x - A.x ) *r
    py = A.y + ( B.y - A.y ) *r
    crossPoint.x = px
    crossPoint.y = py
    distance = sqrt( (P.x - px)*(P.x - px) + (P.y - py)*(P.y - py) )
    z = point2point(P,crossPoint)
    return distance,crossPoint,z
    
    
##过关键点的贝赛尔曲线
def bezier(vertices):
    NumPoint=len(vertices)-1
    t=[]
    x=[]
    y=[]
    w=[]
    for i in np.arange(0,1,0.001):
        t.append(i)
        tmp_x = pow((1-i),NumPoint)*vertices[0].x
        tmp_y = pow((1-i),NumPoint)*vertices[0].y
        x.append(tmp_x)
        y.append(tmp_y)
        w.append(0) 
    for j in range(1,len(vertices)):
        
        for k in range(0,len(t)):
            w[k]=factorial(NumPoint)/(factorial(j)*factorial(NumPoint-j))*pow((1-t[k]),NumPoint-j)*pow(t[k],j)
            x[k]=x[k]+w[k]*vertices[j].x
            y[k]=y[k]+w[k]*vertices[j].y  
    return x,y

##直线方程上过一点的垂直方程
def verticalEqua(p,constant):
    #原方程的参数表达式:ax + by +c = 0
    a = constant[0]
    b = constant[1]
    c = constant[2]
    #垂直线方程的表达式:
    A = -b
    B = a
    C = -A * p.x -B *p.y
    
    cons = [ A , B, C]
    return cons    

##定义结构体用来对 点到边的距离进行排序
class SortedDisStruct():
    def __init__(self,distance,crossPoint,edge,obs):
        self.distance = distance #距离
        self.crossPoint = crossPoint #交点
        self.edge = edge #边
        self.obs = obs #障碍物
        
        
        
    
    
##点到障碍物
def pointToObs(p,obs):
    obs_edges_point_dis = []
    for i in range (0,len(obs.edges)):        
        obs.edges[i].getPointEdge(p)
        tmp = SortedDisStruct(obs.edges[i].distance,obs.edges[i].crossPoint,obs.edges[i],obs)
        obs_edges_point_dis.append(tmp)
    return obs_edges_point_dis
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
