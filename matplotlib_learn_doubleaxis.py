import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y1 = 0.05*x**2
y2 = -2*y1

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()  #共享x轴  twiny即y轴
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b--')

ax1.set_xlabel('X dada')
ax1.set_ylabel('Y1',color = 'g')
ax2.set_ylabel('Y2',color = 'b')
ax2.set_ylim(-20,0)

plt.show()