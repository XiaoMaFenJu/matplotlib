'''
这是规范绘图，批量绘图的第一步！
更是XiaoMaFenJu的一大步！LMAO~
主体思路：准备数据、图像设置、Plot、保存/show
'''
###### 所需库 ######
import numpy as np
import matplotlib.pyplot as plt

import xarray as xr
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.colors as mcolors
import cmaps
###### 示例数据 ######
max_path = r'D:\data\time\max_time_tl_month.npy'
min_path = r'D:\data\time\min_time_tl_month.npy'
min = np.load(min_path)
max = np.load(max_path)
min_year = min.reshape([44,12]).mean(axis=1)
max_year = max.reshape([44,12]).mean(axis=1)
latlon_path = r"D:\data\ERA5_process_2\era5_2m_mean_temperature_timemean.nc"
ds = xr.open_dataset(latlon_path)
lat = ds.lat.data
lon = ds.lon.data
ds.close()
path_max = r'D:\data\time\max_time_10.npy'
max_all = np.load(path_max)
###########################################################################################

###### 图像设置 ######
# fig, axes = plt.subplots(2, 2, figsize=(5,5), dpi=150, sharex="none", sharey="none")
####注意，如果要绘制等值线地图
target_proj = ccrs.PlateCarree(central_longitude=180) # ERA5的配置
data_proj = ccrs.PlateCarree(central_longitude=0)     # ERA5的配置
fig, axes = plt.subplots(1, 1, subplot_kw={'projection': target_proj}, figsize=(5,5), dpi=50, sharex="none", sharey="none")

# sharex/y:all col row none 共享x/y轴[注意大小写]; 调用ax:axes[1,0]
fig.subplots_adjust(top=0.9, bottom=0.1, right=0.9, left=0.1, hspace=0.2, wspace=0.2)
# top,bottom,left,right 可以认为是所有图像的分布范围,1,0,1,0设置表示完全不留白 hspace:列子图间距 wspace:行子图间距

### 保存 ###
def Plt_save(save_path, file_name, file_format, pic_bbox=None, pad_inches=0.1):
    '''
    save_path:最后不加/或\  (如果是\需要写成'\\')
    file_name:最后不加文件格式,
    file_format:图片格式，前面不需要加. ;支持eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
    '''
    save_all = save_path + r"\\" + file_name + r'.' + file_format
    plt.savefig(save_all, bbox_inches=pic_bbox, pad_inches=pad_inches)
    # tight:紧凑/无白(但会使dpi设置失效); pad_inches为留白量
    pass
############

'''# 可选设置
fig.set_facecolor('green') # fig背景色

plt.margins(0,0) # 轴内图像距离轴的距离,值范围[0,1],第一参数表示x轴向，二表示y

ax = plt.subplot2grid((2,2),(1,0),colspan=2,rowspan=1) # 合并子图[放在Plot函数前]
# 几行几列 起始行列 colspan列 rowspan行:即图像占的区域（默认1x1）

####如果要实现单独设置每一张图
fig = plt.figure(figsize=(5,5), dpi=50)
ax = fig.add_axes([left, bottom, width, height], projection=target_proj) #添加任意位置及大小[放在Plot函数前]
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  #左下点坐标及图像长宽，数值为figure百分比
chartBox = ax.get_position()
x, y, w, h = chartBox.x0, chartBox.y0, chartBox.width, chartBox.height
print(x,y,w,h) # 通过chartbox查看ax的位置参数，从而便于设置不同ax大小相同
'''

###### 折线图 ######
def Plot_plot(ax, x, y1, y2):
    '''
    允许大家根据自己需求配置相应函数参数，几个y啦，对应的label啦，title啦....
    '''
    # 绘图数据
    ax.patch.set_facecolor('k') # ax的背景色
    ax.patch.set_alpha(0.5)  # ax的背景透明度，0是完全透明

    ax.spines['top'].set_visible(False) # 去掉ax边框 'top','bottom','left','right'
    ax.spines['right'].set_color('none') # ax边框颜色 'none'表示无色/透明
    ax.xaxis.set_ticks_position('bottom') # 带tick的x边框（或者说x轴）在上/下 'top'/'bottom';y轴改成yaxis
    ax.spines['left'].set_position(('data', -1)) # 边框位置在data处 'top','bottom','left','right'
    # set_position还可选'axes',表示百分比 0.1表示10%，如.set_position(('axes', 0.1))
    ax.spines['left'].set_linewidth(2)
    ax.spines['left'].set_linestyle('--')

    ax.grid(linestyle="--", linewidth=0.3, color='k', alpha=0.5) # 网格线
    # 可单独x/y进行设置:ax.xaxis.grid()

    ax.set_xlim([0,44]) # x轴范围
    ax.set_xticks(range(0, 44, 5))
    ax.set_xticklabels(np.arange(1979,2023,5))
    ax.set_xlabel(r'我是xlabel', font={'family': 'Microsoft YaHei', 'size': 9})

    ax.set_ylim([0, 24])  # y轴范围
    ax.set_yticks(range(0, 24, 6))
    ax.set_yticklabels(np.arange(0, 24, 6))
    ax.set_ylabel(r'我是ylabel',font = {'family': 'Microsoft YaHei', 'size': 9})

    ax.set_title(r'我是ax_title',font = {'family': 'Microsoft YaHei', 'size': 11})

    ### return 处也需要同步更改
    pl1, = ax.plot(x, y1, label = 'line1',color='red',linewidth = 1.0,linestyle = '--')
    pl2, = ax.plot(x, y2, label = 'line2',color='blue',linewidth = 2.0,linestyle = '--')

    ax.legend(handles=[pl1, pl2], fontsize=7, loc='best', ncol=2) # 图例设置
    '''
    'upper right', 'upper left', 'lower left', 'lower right', 'right',
    'center left', 'center right', 'lower center', 'upper center', 'center'
    2、borderpad：图例的内边距 ，None或者float。
    3、fontsize：int或float，用于设置字体大小。
    4、frameon： 是否显示图例边框，None或者bool。=False也可以
    6、framealpha：控制图例框的透明度，None或者float。
    7、ncol：图例列的数量，默认为1。
    8、title：图例的标题
    9、shadow： 是否为图例边框添加阴影，None或者bool。
    12、labelspacing：图例中条目之间的距离，None或者float。
    13、handlelength：图例中句柄的长度。
    '''

    return ax, pl1, pl2

###### 等值线填色图叠加地图投影 ######
def Plot_contourf(ax, lat, lon, data, data_proj,title='title',cmap='viridis'):
    cn = ax.contourf(lon, lat, data, transform=data_proj, extend='both', cmap=cmap)
    # cn = ax.contourf(lon, lat, data, transform=data_proj, extend='both', cmap=cmap, levels=level)
    # cn = ax.contourf(lon, lat, data, transform=data_proj, extend='both', cmap=cmap, levels=level,
    #                ,norm=mcolors.TwoSlopeNorm(vmin=level[0], vmax=level[-1], vcenter=0)) #设置以0为中心的非对称colorbar
    # 可选参数:alpha 透明度

    ax.coastlines(resolution='50m', lw=0.5)  # resolution='50m'、'110m'、'10m' # 添加海岸线
    ax.set_global()
    ax.set_title(title,font = {'family': 'Microsoft YaHei', 'size': 9})

    gl = ax.gridlines(draw_labels=True, linestyle="--", linewidth=0.3, color='k', alpha=0.5)
    gl.top_labels = False  # 关闭上部经纬标签
    gl.right_labels = False
    gl.xformatter = LONGITUDE_FORMATTER  # 使横坐标转化为经纬度格式
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlocator = mticker.FixedLocator(np.arange(-180, 180, 60)) # 经纬度范围
    gl.ylocator = mticker.FixedLocator(np.arange(-90, 90, 30))
    gl.xlabel_style = {'size': 9}  # 修改经纬度字体大小
    gl.ylabel_style = {'size': 9}
    # gl.xlines = False # 关闭经向网格线

    cb = plt.colorbar(cn, ax=ax, fraction=0.03, orientation='horizontal')#默认垂直,这个是水平
    cb.ax.tick_params(labelsize=15)
    # cb.set_ticks(level)
    # cb.set_ticklabels(level.astype(str).tolist())
    # cb.update_ticks() # 可能没用？
    return ax, cn, cb

# Plot_contourf(axes,lat,lon,max_all[0,0,:,:],data_proj)
plt.show()