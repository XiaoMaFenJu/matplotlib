import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def f(i):
    line.set_ydata(np.sin(x+i/100))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,


ani = animation.FuncAnimation(fig=fig,func=f,frames=100,init_func=init,interval=20,blit=True)  #产生动画 还有其他种
#frames 动画帧数 func 方程 init_func 方程初始状态 interval 动画更新间隔 blit 更新整张图/变化点

plt.show()