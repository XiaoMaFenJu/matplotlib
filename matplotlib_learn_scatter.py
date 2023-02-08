import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n) #高斯分布随机数
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)    #反正切函数 随便选一个颜色与点的对应关系而已

plt.scatter(X,Y,s=75,c=T,alpha=0.5,cmap='gist_rainbow')

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(()) #隐藏x轴数字
plt.yticks(()) #隐藏y轴数字

plt.show()