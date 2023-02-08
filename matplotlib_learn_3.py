import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 0.1 * x

plt.figure() #size单位为 inches  num代表编号  #多个figure代表多个窗口
plt.plot(x,y,lw = 10,zorder = 1)
ax = plt.gca()
ax.spines['right'].set_color('none')  #spines 脊柱、脊梁，可认为图片的四边框
ax.spines['top'].set_color('none')    #该两行使上、右边框消失 目的是想要实现 x和y轴
ax.xaxis.set_ticks_position('bottom') #但并未清楚x轴是上边框还是下边框，y同理，故本行设置默认x轴
ax.yaxis.set_ticks_position('left')   #同理
ax.spines['bottom'].set_position(('data',0)) #设置坐标原点 y0 = 0  除了data还有outward和axes两种选择
ax.spines['left'].set_position(('data',0)) #设置坐标原点 x0 = 0    axes是百分比 0.1表示10% outward暂未知

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_zorder(2)    #zorder表示绘图先后顺序
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.7))   #背景箱对象 alpha表示透明度_plot等也可以用

plt.show()