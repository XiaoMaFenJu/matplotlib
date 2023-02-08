import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2 * x + 1
y2 = x ** 2

# plt.figure()
# plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5)) #size单位为 inches  num代表编号  #多个figure代表多个窗口
l1, = plt.plot(x,y2,label='line1')#label为标识名、标签
l2, = plt.plot(x,y1,color='red',linewidth = 2.0,linestyle = '--',label='line2')#同张图绘制第二条线
#plt.plot的返回值是object，所以可以给一个对象，如果要在legend的handles使用比如加, 如   l1,

plt.legend(handles = [l1,l2],labels = ['aaa','bbb'],loc='best') #添加图例
#labels如果给出则使用给出的，未给出则使用原label  loc表示图例位置，可选，best为择优选
#使用handles可以指定要哪些线的图例以及顺序


plt.show()

###############################part 1###### 坐标轴 ##################################################
# plt.xlim((-1,2))#x,y坐标轴数值范围限定
# plt.ylim((-2,3))
# plt.xlabel("i am x")#x,y坐标轴标题
# plt.ylabel("i am y")
#
# new_ticks = np.linspace(-1,3,5)
# # print(new_ticks)
# plt.xticks(new_ticks) #x坐标轴数值
# y_ticks_num = [-2,-1.8,-1,1.22,3]
# y_ticks_str = ["really bad","bad","$normal$","$good \alpha$",r"$very\ good \alpha$"]#类似latex
# plt.yticks(y_ticks_num,y_ticks_str)
#
# #gca = 'get current axis'获取轴
# ax = plt.gca()
# ax.spines['right'].set_color('none')  #spines 脊柱、脊梁，可认为图片的四边框
# ax.spines['top'].set_color('none')    #该两行使上、右边框消失 目的是想要实现 x和y轴
# ax.xaxis.set_ticks_position('bottom') #但并未清楚x轴是上边框还是下边框，y同理，故本行设置默认x轴
# ax.yaxis.set_ticks_position('left')   #同理
# ax.spines['bottom'].set_position(('data',0)) #设置坐标原点 y0 = 0  除了data还有outward和axes两种选择
# ax.spines['left'].set_position(('data',0)) #设置坐标原点 x0 = 0    axes是百分比 0.1表示10% outward暂未知

#####################################################################################################
