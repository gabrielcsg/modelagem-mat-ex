# METODO DE EULER
import matplotlib.pyplot as plt


def funcao(x, y):
    # 2.718281828 = e
    return 2.718281828 ** (-x) - (2 * y)


resultados = []

x_n = float(input())
y_n = float(input())
h = float(input())
m = int(input())

linha_x = []
linha_y = []
linha_x.append(x_n)
linha_y.append(y_n)

n = 0
while n < m:
    x_n1 = x_n + h
    y_n1 = y_n + (funcao(x_n, y_n) * h)

    linha_x.append(x_n)
    linha_y.append(y_n)
    x_n = x_n1
    y_n = y_n1
    n += 1

for k in range(len(resultados)):
    linha_x.append(resultados[k][0])
    linha_y.append(resultados[k][1])

plt.plot(linha_x, linha_y)
plt.show()
