from mathTools import bezier
from point import Point
import matplotlib.pyplot as plt
dataSet =[]
p1 = Point(0,3)
p2 = Point(3,7)
p3 = Point(7,2)
p4 = Point(9,6)
p5 = Point(13,3)
dataSet.append(p1)
dataSet.append(p2)
dataSet.append(p3)
dataSet.append(p4)
dataSet.append(p5)
xset,yset = bezier(dataSet)
print(len(xset))
print(xset)
plt.figure()
axes = plt.gca()
x_origin =[]
y_origin =[]
for data in dataSet:
    x_origin.append(data.x)
    y_origin.append(data.y)
axes.plot(x_origin,y_origin,color='red')
axes.plot(xset,yset)
plt.axis('equal')
plt.show()
