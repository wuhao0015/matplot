import matplotlib.pyplot as plt
import random
x = [i for i in range(20)]
y = [random.randint(0, 100) for i in range(20)]

plt.plot(x, y)
plt.savefig('d:/result1.png')
plt.show()
