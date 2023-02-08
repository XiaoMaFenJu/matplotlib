import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

################method 1#####################
# #直接subplot

# plt.figure()
#
# plt.subplot(2,1,1)
# plt.plot([0,1],[0,1])
#
# plt.subplot(2,3,4)
# plt.plot([0,1],[0,2])
#
# plt.subplot(2,3,5)
# plt.plot([0,1],[0,3])
#
# plt.subplot(2,3,6)
# plt.plot([0,1],[0,4])
#
# plt.show()

################method 2#####################
#subplot2grid

# plt.figure()
# ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# #几行几列 起始行列 colspan列 rowspan行:即图像占的区域（默认1x1）
# ax1.plot([1,2],[1,2])
# ax1.set_title('one') #和plt.title('one')差不多 这个可以单独设置每个ax
#
# ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
# ax3 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
# ax4 = plt.subplot2grid((3,3),(2,0))
# ax5 = plt.subplot2grid((3,3),(2,1))
# plt.show()

################method 3#####################
#gridspec

# plt.figure()
# gs = gridspec.GridSpec(3,3)
# ax1 = plt.subplot(gs[0,:])
# ax2 = plt.subplot(gs[1,:2])
# ax3 = plt.subplot(gs[1,2])
# ax4 = plt.subplot(gs[2,0])
# ax5 = plt.subplot(gs[-1,-2:])
#
# plt.show()

################method 4#####################
#subplots                 ssssss


f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)#共享x、y轴
#f是figure，后面的ax11表示第一行第一列的图像  共享表示整张图用同一个轴
ax11.scatter([1,2],[1,2])

plt.show()