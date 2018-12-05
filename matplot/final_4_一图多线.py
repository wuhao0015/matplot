import matplotlib.pylab as plt
import final_0_data

fig = plt.figure()

ax = fig.add_subplot(111)

import matplotlib.dates as mdate
ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))

import matplotlib.ticker as mtick
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

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



#########################注释1#########################
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('路由器CPU使用率')
plt.xlabel('采集时间')
plt.ylabel('CPU使用率')
#########################注释1#########################

fig.autofmt_xdate() #自动调整X轴格式
#plt.plot(X1, Y1) #制图
#plt.plot(X2, Y2) #制图

R1, = ax.plot(X1, Y1, linestyle='solid', color='r', label='R1')
R2, = ax.plot(X2, Y2, linestyle='dashed', color='b', label='R2')

ax.legend(loc='upper left')
plt.show() #显示图
