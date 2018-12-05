import matplotlib.pyplot as plt

app = ['HTTP', 'FTP', 'RDP', 'QQ']
data = [30, 53, 12, 45]

color_list = ['r', 'b', '0.5', '#FF00FF']

plt.barh(app, data, height=0.5, color=color_list)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('协议与带宽分布')
plt.xlabel('带宽（M/s）')
plt.ylabel('协议')

plt.show()
