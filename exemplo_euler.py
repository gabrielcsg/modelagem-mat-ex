# METODO DE EULER
import matplotlib.pyplot as plt


def funcao(x, y):
    # Essa função deve ser dada na questão.
    # 2.718281828 = e
    return 2.718281828 ** (-x) - (2 * y)


# Entradas
x_n = float(input())
y_n = float(input())
h = float(input())
n, m = input().split(' ')

n = int(n)
m = int(m)

# Armazenando as primeiras informações: x0 e y0
linha_x = []
linha_y = []
linha_x.append(x_n)
linha_y.append(y_n)

# A partir das entradas recebidas, utilizando o metodo de euler para obter as proximas informações.
while n < m:
    x_n1 = x_n + h
    y_n1 = y_n + (funcao(x_n, y_n) * h)

    linha_x.append(x_n1)
    linha_y.append(y_n1)
    x_n = x_n1
    y_n = y_n1
    n += h

# Adicionando as informações no gráfico.
plt.plot(linha_x, linha_y)
plt.show()
