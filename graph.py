import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")

# создаем массив значений x от -5 до 20 с шагом 0.1
x = np.arange(-5, 20)

# вычисляем значения функции для каждого x
y = x**2 + np.sin(x) - 12*x - 0.25

# строим график функции
plt.plot(x, y)

# добавляем заголовок и подписи к осям
plt.title('Графік функції y = x^2 + sin(x) - 12x - 0.25')
plt.xlabel('x')
plt.ylabel('y')

# оси
plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)

# отображаем график
plt.show()
