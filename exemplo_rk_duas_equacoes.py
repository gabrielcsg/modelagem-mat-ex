# METODO DE RUNGE KUTTA DUAS EQUACOES
import matplotlib.pyplot as plt


def funcao1(t, x, y):
    # Essa funcao deve ser dada na questao.
    return (-0.16*x) + (0.08*x*y)


def funcao2(t,x,y):
    return (4.5 * y) - (0.9 * x * y)


# Entradas
t_n = float(input())
x_n = float(input())
y_n = float(input())
h = float(input())
m = int(input())

# Armazenando as primeiras informacoes: x0 e y0
linha_t = []
linha_x = []
linha_y = []

linha_t.append(t_n)
linha_x.append(x_n)
linha_y.append(y_n)

# A partir das entradas recebidas, utilizando o metodo de euler para obter as proximas informacoes.
n = 0
while n < m:
    t_n1 = t_n + h

    kn1_1 = funcao1(t_n, x_n, y_n)
    kn2_1 = funcao2(t_n, x_n, y_n)

    kn1_2 = funcao1(t_n + (0.5*h), x_n + ((0.5 * h) * kn1_1), y_n + ((0.5 * h) * kn2_1))
    kn2_2 = funcao2(t_n + (0.5*h), x_n + ((0.5 * h) * kn1_1), y_n + ((0.5 * h) * kn2_1))

    kn1_3 = funcao1(t_n + (0.5*h), x_n + ((0.5 * h) * kn1_2), y_n + ((0.5 * h) * kn2_2))
    kn2_3 = funcao2(t_n + (0.5 * h), x_n + ((0.5 * h) * kn1_2), y_n + ((0.5 * h) * kn2_2))

    kn1_4 = funcao1(t_n + h, x_n + (h * kn1_3), y_n + (h * kn2_3))
    kn2_4 = funcao2(t_n + h, x_n + (h * kn1_3), y_n + (h * kn2_3))

    x_n1 = x_n + ((h/6)*(kn1_1 + (2*kn1_2) + (2*kn1_3) + kn1_4))
    y_n1 = y_n + ((h/6)*(kn2_1 + (2*kn2_2) + (2*kn2_3) + kn2_4))

    linha_t.append(t_n1)
    linha_x.append(x_n1)
    linha_y.append(y_n1)

    t_n = t_n1
    x_n = x_n1
    y_n = y_n1
    n += h

# Adicionando as informacoes no grafico.
plt.plot(linha_t, linha_x, linha_t, linha_y)
plt.show()
