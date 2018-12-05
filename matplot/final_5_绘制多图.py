import matplotlib.pylab as plt
import final_0_data

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

import matplotlib.dates as mdate
ax1.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))
ax2.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))

import matplotlib.ticker as mtick
ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))
ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

X1 = []
Y1 = []

for (time, cpu) in final_0_data.R1_CPU_TIME:
    X1.append(time)
    Y1.append(cpu)

X2 = []
Y2 = []

for (time, cpu) in final_0_data.R2_CPU_TIME:
    X2.append(time)
    Y2.append(cpu)

R1, = ax1.plot(X1, Y1, linestyle='solid', color='r', label='R1')
R2, = ax2.plot(X2, Y2, linestyle='dashed', color='b', label='R2')


ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

#########################注释#########################
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.suptitle('路由器CPU使用率')

#########################注释小图#########################
ax1.set_title('R1路由器')
ax1.set_xlabel('采集时间')
ax1.set_ylabel('CPU使用率')

ax2.set_title('R2路由器')
ax2.set_xlabel('采集时间')
ax2.set_ylabel('CPU使用率')

fig.autofmt_xdate() #自动调整X轴格式
plt.show() #显示图
