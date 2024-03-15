from getPrices import firstPrices, secondPrices
import math


def z_i(x, y):
    if x - y > 0:
        return 1
    else:
        return 0


x = []
y = []

for key, value in firstPrices.items():
    x.append(value)

for key, value in secondPrices.items():
    y.append(value)


n = len(x)
abs_diff_x_y = []

for i in range(n):
    abs_diff_x_y.append([abs(x[i] - y[i]), x[i], y[i]])

abs_diff_x_y.sort()
r = 1
for i in range(n):
    abs_diff_x_y[i].append(r)
    abs_diff_x_y[i].append(z_i(abs_diff_x_y[i][1], abs_diff_x_y[i][2]))
    r += 1

w = 0

for i in range(n):
    w += abs_diff_x_y[i][3] * abs_diff_x_y[i][4]

z = (w - n * (n + 1) / 4) / math.sqrt(n * (n + 1) * (2 * n + 1) / 24)  # статистика Уилкоксона
print("Если z больше 1.96 или меньше -1.96, то мы отменяем гипотезу H_0")
print("z = ", z)

