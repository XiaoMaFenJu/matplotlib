import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)  #range()只能整数
Y1 = (1 - X / float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')#条形图颜色
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

#加标注
for x,y in zip(X,Y1):   #通过zip()使每一步同时输出两个值  用时详查
    plt.text(x ,y + 0.05,'%.2f'%y, ha='center',va='bottom')  #ha:horizontal alignment 横向对齐方式 va:纵向
for x,y in zip(X,Y2):   #通过zip()使每一步同时输出两个值  用时详查
    plt.text(x ,-y - 0.05,'-%.2f'%y, ha='center',va='top')  #ha:horizontal alignment 横向对齐方式 va:纵向

plt.xlim(-0.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()