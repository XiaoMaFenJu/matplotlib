import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2 * x + 1

plt.figure(num=1,figsize=(8,5)) #size单位为 inches  num代表编号  #多个figure代表多个窗口
plt.plot(x,y)

ax = plt.gca()

ax.spines['right'].set_color('none')  #spines 脊柱、脊梁，可认为图片的四边框
ax.spines['top'].set_color('none')    #该两行使上、右边框消失 目的是想要实现 x和y轴
ax.xaxis.set_ticks_position('bottom') #但并未清楚x轴是上边框还是下边框，y同理，故本行设置默认x轴
ax.yaxis.set_ticks_position('left')   #同理
ax.spines['bottom'].set_position(('data',0)) #设置坐标原点 y0 = 0  除了data还有outward和axes两种选择
ax.spines['left'].set_position(('data',0)) #设置坐标原点 x0 = 0    axes是百分比 0.1表示10% outward暂未知

x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0,y0,s=50,color='b') #画一个点 散点图使用scatter s表示大小
plt.plot([x0,x0],[y0,0],'k--',lw = 2.5)#前两个列表表示x点和y点，即(x0,y0)和(x0,0)两点 k黑色--虚线 lw为linewidth

# annotation 标注
#method 1
###########################
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
             fontsize = 16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
#第一参数为标注内容，coordination为坐标之意 xy为标注坐标，xycoords为坐标系基于数据（line 16)，xytext为标注文本的坐标差
#textcoords为标注文本的坐标系基于标注点调整，arrowprops为箭头参数，弧度等（需要时自查）

#method 2
###########################
fontdict = {'size':16,'color':'r'}
plt.text(-3.7,3,r'$there\ are\ some\ texts.\ \mu\ \sigma_i\ \alpha^j   $',fontdict)#格式参考latex
#不算标准的标注，就是直接标text，但是效果差不多


plt.show()