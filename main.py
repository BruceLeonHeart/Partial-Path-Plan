import matplotlib.pyplot as plt
import numpy as np
import random
from point import Point
from area import Area
from obstacle import Obstacle
from section import Section
from subject import Subject
import mathTools
from cvxopt import matrix,solvers
#区域表，第一个为可行区域，后续为障碍物
#AreaList = []
#地图初始化
map = Section()

plt.figure()
axes = plt.gca()
#起点与终点
origin = Point(0,0)
remote = Point(0,50)
result = [origin,remote]

#路沿
obstacles = []
road_left_obs = Obstacle()
road_left_obs.createObs(-20,0,15,50)
road_right_obs = Obstacle()
road_right_obs.createObs(5,0,15,50)
obstacles.append(road_left_obs)
obstacles.append(road_right_obs)
road_left_obs_area = Area(road_left_obs.obstacle_x,road_left_obs.obstacle_x,road_left_obs.obstacle_width,road_left_obs.obstacle_height)
road_right_obs_area = Area(road_right_obs.obstacle_x,road_right_obs.obstacle_x,road_right_obs.obstacle_width,road_right_obs.obstacle_height)

'''
plt.Rectangle((-20,0),15,50)
axes.add_patch(road_left_obs)
road_right_obs = plt.Rectangle((5,0),15,50)
axes.add_patch(road_right_obs)
'''
#随机障碍物
num = random.randint(0,7)
print('随机障碍物的个数: ',num)

for i in range(0,num):
    tmpObs = Obstacle()    
    obstacles.append(tmpObs)
#显示障碍物
for obs in obstacles:
    axes.add_patch(obs.rect)


#---------------------------------------------------------------------
'''
    循环退出条件：
    1.当储备列表的数目为4时退出
    2.当所求点为上一个输入点时
'''
next = Point(-1,-1)
while True:
    current = result[-2]
    #初始化可行域
    subjectList = []
    able_area = Obstacle()
    able_area.createObs(-20,0,40,50)
    for medge in able_area.edges:
        medge.getPointEdge(current)
        tmp = Subject(medge.constant)
        tmp.setFlag(current)
        subjectList.append(tmp)  
    #遍历障碍物
    #对于每个障碍物来说，四个边与current都有交点，需要
    #1.检验交点是否处于可行域
    #2.若有多个边的交点均处于可行域，则返回最短距离的那个交点即可，且该障碍物不再被考虑直到current被改变
    able_obstacle = []#存储所有障碍物边的容器
    for obs in obstacles:
        v = []#每个障碍物存储边的容器
        for edge in obs.edges:
            edge.getPointEdge(current)
            z = True
            for subject in subjectList:
                z = z and (np.sign(subject.a * edge.crossPoint.x + subject.b * edge.crossPoint.y + subject.c) * subject.flag !=-1)
            if(z):
                v.append(edge)
        if(len(v)==0):
            break
        else:
            sorted_v = sorted(v,key = lambda edge:(float (edge.distance)),reverse = False)
            able_obstacle.append(sorted_v[0])
    
    #对所有障碍物进行排序
    able_obstacle = sorted(able_obstacle,key = lambda edge:(float (edge.distance)),reverse = False)
    
    #从所有障碍物边列表中获取，直到所有障碍物的标志都不可选
    while True:
        choose = []
        for edge in able_obstacle:
            if edge.canBeChosed:#该条边可选并且处于可行域
                z = True
                for subject in subjectList:
                    z = z and (np.sign(subject.a * edge.crossPoint.x + subject.b * edge.crossPoint.y + subject.c) * subject.flag !=-1)
                if(z):                        
                    edge.canBeChosed = False
                    choose.append(edge)
                    break
        
        if(len(choose)==0):
            break
        else:         
            plt.plot([current.x,choose[0].crossPoint.x],[current.y,choose[0].crossPoint.y],'m--')
            #垂直线的直线表达式
            cons = mathTools.verticalEqua(current,choose[0].cons)
            #新增约束
            tmpSubject = Subject(cons)
            tmpSubject.setFlag(current)
            subjectList.append(tmpSubject)
            
    #从约束条件中求取距离remote最近的点
    p = matrix([[2.0,0.0],[0.0,2.0]])
    q = matrix([-2*remote.x,-2*remote.y])
    G = np.array([[]])
    H = np.array([[]])
    for subject in subjectList:
        cons_g = [subject.a,subject.b]
        cons_h = [subject.c]
        
        if (subject.flag == -1):#标准型，直接添加 
            #print(cons_g)
            #print(cons_h)
            #print(G)
            #print(H)
            #np.append(G,values=cons_g,axis=0)          
            #np.append(H,values=-cons_h,axis=0)
            G = np.append(G,values = cons_g)          
            H = np.append(H,values = -1*cons_h)

        elif (subject.flag == 1):#取反
            #print(cons_g)
            #print(cons_h)
            #print(G)
            #print(H)
            G = np.append(G,values = -1*cons_g)          
            H = np.append(H,values = cons_h)
            #np.append(G,values=-cons_g,axis=0)          
            #np.append(H,values=cons_h,axis=0)

        else:
            continue
    g = matrix(G,(2,len(G)/2))
    h = matrix(H) 
    print('g',g)
    print('\n')
    print('h',h)
      
    res = solvers.qp(p,q,g,h)
    next.x = res[0]
    next.y = res[1]
    if(next==result[-2]):
        break
    elif(len(result)==4):
        break
    else:
        result.insert(-2,next)
#对数据集里面的点做贝赛尔曲线
for p in result:
    print(p)
    
    



axes.set_xlim([map.section_base.x,map.section_base.x + map.width])
axes.set_xbound([map.section_base.x,map.section_base.x + map.width])
axes.set_ylim([map.section_base.y,map.section_base.y + map.height])
axes.set_ybound([map.section_base.y,map.section_base.y + map.height])
plt.axis('equal')
plt.show()



