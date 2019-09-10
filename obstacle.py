import random
from point import Point
from edge import Edge
#from area import Area
import matplotlib.pyplot as plt

class Obstacle():
    #随机型障碍物
    def __init__(self):
        #左下角基准点  
        self.obstacle_x = random.uniform(-20,16)
        self.obstacle_y = random.uniform(0,46)
        #长、宽
        self.obstacle_width = random.uniform(2,4)
        self.obstacle_height = random.uniform(2,4)
        #四个顶点
        apexs = []
        apex0 = Point(self.obstacle_x,self.obstacle_y)
        apex1 = Point(self.obstacle_x + self.obstacle_width,self.obstacle_y)
        apex2 = Point(self.obstacle_x + self.obstacle_width,self.obstacle_y + self.obstacle_height)
        apex3 = Point(self.obstacle_x,self.obstacle_y + self.obstacle_height)
        apexs.append(apex0)
        apexs.append(apex1)
        apexs.append(apex2)
        apexs.append(apex3)

        self.apexs = apexs
        #四条边
        edges = []
        edge0 = Edge(apexs[0],apexs[1])
        edge1 = Edge(apexs[1],apexs[2])
        edge2 = Edge(apexs[2],apexs[3])
        edge3 = Edge(apexs[3],apexs[0])
        edges.append(edge0)
        edges.append(edge1)
        edges.append(edge2)
        edges.append(edge3)
        self.edges = edges
        rect = plt.Rectangle((self.obstacle_x,self.obstacle_y),self.obstacle_width,self.obstacle_height,color='red')
        self.rect = rect
        
        #self.canBeChosed = True
        
    #使用定值来修改生成的障碍物属性
    def createObs(self,x,y,w,h):
        #左下角基准点  
        self.obstacle_x = x
        self.obstacle_y = y
        #长、宽
        self.obstacle_width = w
        self.obstacle_height = h
        #四个顶点
        apexs = []
        apex0 = Point(self.obstacle_x,self.obstacle_y)
        apex1 = Point(self.obstacle_x + self.obstacle_width,self.obstacle_y)
        apex2 = Point(self.obstacle_x + self.obstacle_width,self.obstacle_y + self.obstacle_height)
        apex3 = Point(self.obstacle_x,self.obstacle_y + self.obstacle_height)
        apexs.append(apex0)
        apexs.append(apex1)
        apexs.append(apex2)
        apexs.append(apex3)

        self.apexs = apexs
        #四条边
        edges = []
        edge0 = Edge(apexs[0],apexs[1])
        edge1 = Edge(apexs[1],apexs[2])
        edge2 = Edge(apexs[2],apexs[3])
        edge3 = Edge(apexs[3],apexs[0])
        edges.append(edge0)
        edges.append(edge1)
        edges.append(edge2)
        edges.append(edge3)
        self.edges = edges
        rect = plt.Rectangle((self.obstacle_x,self.obstacle_y),self.obstacle_width,self.obstacle_height,color='blue')
        self.rect = rect
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
        
