import matplotlib.pylab as plt
import final_0_data

fig = plt.figure(figsize=(10, 5), dpi=80)
#figsize为英寸
#dpi为分辨率

ax = fig.add_subplot(211) #两排，每排一张图，第一张图

import matplotlib.dates as mdate
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))
#ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))

import matplotlib.ticker as mtick
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f%%'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%')) #最前和最后的%为固定格式

X = []
Y = []

for (time, cpu) in final_0_data.R1_CPU_TIME:
    X.append(time)
    Y.append(cpu)

fig.autofmt_xdate() #自动调整X轴格式
plt.plot(X, Y) #制图
plt.show() #显示图
