import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    #算高度 不用在意 造数据而已
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2,-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

X,Y = np.meshgrid(x,y) #构建等高线的网格 256*256

plt.contourf(X,Y,f(X,Y),4,alpha = 0.75,cmap='hot')#contour是等高线 contourf是等高线的填充fill

C = plt.contour(X,Y,f(X,Y),8,colors="black",linewidths=0.5)#画等高线图的线  8是等高线分多少层

plt.clabel(C,inline=True,fontsize=10)#线的数值标签

plt.xticks(())
plt.yticks(())
plt.show()