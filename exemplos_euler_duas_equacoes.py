# METODO DE EULER
import matplotlib.pyplot as plt


def funcao1(t, x, y):
    # Essa função deve ser dada na questão.
    return (-0.16*x) + (0.08*x*y)


def funcao2(t, x, y):
    # Essa função deve ser dada na questão.
    return (4.5 * y) - (0.9 * x * y)


# Entradas
t_n = float(input())
x_n = float(input())
y_n = float(input())
h = float(input())
m = int(input())

# Armazenando as primeiras informações: x0 e y0
linha_t = []
linha_x = []
linha_y = []
linha_t.append(t_n)
linha_x.append(x_n)
linha_y.append(y_n)

# A partir das entradas recebidas, utilizando o metodo de euler para obter as proximas informações.
n = 0
while n < m:
    t_n1 = t_n + h
    x_n1 = x_n + (funcao1(t_n, x_n, y_n) * h)
    y_n1 = y_n + (funcao2(t_n, x_n, y_n) * h)

    linha_t.append(t_n)
    linha_x.append(x_n)
    linha_y.append(y_n)

    t_n = t_n1
    x_n = x_n1
    y_n = y_n1
    n += 1

# Adicionando as informações no gráfico.
plt.plot(linha_t, linha_x, linha_t, linha_y)
plt.show()
