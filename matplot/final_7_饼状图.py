import matplotlib.pyplot as plt

app = ['HTTP', 'FTP', 'RDP', 'QQ']
data = [30, 53, 12, 45]
color_list = ['r', 'b', '0.5', '#FF00FF']
explode = (0.01, 0.01, 0.01, 0.01)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(6, 6))

patches, l_text, p_text = plt.pie(data, explode=explode, labels=app, colors=color_list,
                                labeldistance=1.1, autopct='%3.2f%%', shadow=False,
                                startangle=90, pctdistance=0.6)

for t in l_text:
    t.set_size = (30)
for t in p_text:
    t.set_size = (20)

plt.axis('equal')
plt.legend()
plt.show()
