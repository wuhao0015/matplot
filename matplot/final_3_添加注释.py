import matplotlib.pylab as plt
import final_0_data

fig = plt.figure()

ax = fig.add_subplot(111)

import matplotlib.dates as mdate
ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))

import matplotlib.ticker as mtick
ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

X = []
Y = []

for (time, cpu) in final_0_data.R1_CPU_TIME:
    X.append(time)
    Y.append(cpu)

fig.autofmt_xdate() #自动调整X轴格式

#########################注释1#########################
#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.title('路由器CPU使用率')
#plt.xlabel('采集时间')
#plt.ylabel('CPU使用率')
#########################注释1#########################


plt.plot(X, Y) #制图
plt.show() #显示图
