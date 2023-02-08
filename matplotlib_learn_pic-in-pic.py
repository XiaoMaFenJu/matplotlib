import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

left,bottom,width,height = 0.1,0.1,0.8,0.8  #整个figure百分比
ax1 = fig.add_axes([left,bottom,width,height]) #左下点及图片长宽
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left,bottom,width,height = 0.2,0.6,0.25,0.25  #整个figure百分比
ax2 = fig.add_axes([left,bottom,width,height]) #左下点及图片长宽
ax2.plot(x,y,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title_inside1')

left,bottom,width,height = 0.2,0.6,0.25,0.25  #整个figure百分比
ax2 = fig.add_axes([left,bottom,width,height]) #左下点及图片长宽
ax2.plot(x,y,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title_inside1')

plt.axes([0.6,0.2,0.25,0.25])  #只画一个图可以用这个
plt.plot(y,x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title_inside2')

plt.show()