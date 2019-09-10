import matplotlib.pyplot as plt
import numpy as np
import random
from point import Point
from area import Area
from obstacle import Obstacle
from section import Section
from subject import Subject
import mathTools
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
#able_area = Area(-20,0,40,50)
#AreaList.append(able_area)
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
print(num)

for i in range(0,num):
    tmpObs = Obstacle()
    
    obstacles.append(tmpObs)
#显示障碍物
for obs in obstacles:
    axes.add_patch(obs.rect)

#可行区域限制条件
EdgeSbj = []
#添加搜索区域
able_area = Obstacle()
able_area.createObs(-20,0,40,50)
for medge in able_area.edges:
    medge.getPointEdge(origin)
    tmpsbj = Subject(medge.constant)
    tmpsbj.setFlag(origin)
    tmpsbj.setCheck(True)
    EdgeSbj.append(tmpsbj)
    
#遍历障碍物
#障碍物与点的信息列表
v = []
for obs in obstacles:
    for edge in obs.edges:
        edge.getPointEdge(origin) 
        v.append(edge)
        print(edge)
#按照距离进行排序
def comp(edge1, edge2):
    if edge1.distance < edge2.distance:
        return 1
    elif edge1.distance > edge2.distance:
        return -1
    else:
        return 0
sorted_v = sorted(v,key = lambda edge:(float (edge.distance)),reverse = False)
print("........................................................................after sorted.......................................................................................")
for edge in sorted_v:
    print(edge)


'''
for mobs in obstacles[0:2]:
    for medge in mobs.edges:
        medge.getPointEdge(origin)
        tmpsbj = Subject(medge.constant)
        tmpsbj.setFlag(origin)
        tmpsbj.setCheck(True)
        EdgeSbj.append(tmpsbj)
'''
def isContinue(a):
    flag = False
    for i in range(0,len(a)):
        if a[i].canBeChosed:
            flag = True
            break
    return flag
    

#符合要求的边的角标
while(isContinue(sorted_v)):
    for edge in sorted_v:
        #检查是否处于可行域
        z = 0
        for sbj in EdgeSbj:
            z = np.sign(sbj.a * edge.crossPoint.x + sbj.b * edge.crossPoint.y + sbj.c) * sbj.flag
            if(z == -1):
                edge.canBeChosed = False
                #continue
                
    #选取最近的
    for i in range(0,len(sorted_v)):
        if sorted_v[i].canBeChosed:
            cons = mathTools.verticalEqua(sorted_v[i].crossPoint,sorted_v[i].cons) 
            tmpsbj = Subject(cons)
            tmpsbj.setFlag(origin)
            tmpsbj.setCheck(True)
            EdgeSbj.append(tmpsbj)
            plt.plot([0,sorted_v[i].crossPoint.x],[0,sorted_v[i].crossPoint.y],'m--')
            k = (int)((i+1)/4)
            for j in range(4*k,4*(k+1)):                
                sorted_v[j].canBeChosed = False #选中后该障碍物不必再选取
            break         



print("........................................................................after TASK.......................................................................................")
for edge in sorted_v:
    print(edge)


print('edges size is :',len(EdgeSbj))
for single in EdgeSbj:
    print(single)
#print(EdgeSbj[0])


axes.set_xlim([map.section_base.x,map.section_base.x + map.width])
axes.set_xbound([map.section_base.x,map.section_base.x + map.width])
axes.set_ylim([map.section_base.y,map.section_base.y + map.height])
axes.set_ybound([map.section_base.y,map.section_base.y + map.height])
plt.axis('equal')
plt.show()



