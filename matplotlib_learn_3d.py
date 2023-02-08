import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig,auto_add_to_figure = False) #直接Axes3D(fig)会报错 老的写法 这是新的不会报错
fig.add_axes(ax)

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow') #rs...和cs...是行跨和列跨 可认为是密度
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow') #zdir=zdirection 即投影方向 offset为投影面位置
ax.set_zlim3d(-2,2)

plt.show()