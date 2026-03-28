from matplotlib import pyplot as plt

y = [1,4,9,16,25]

plt.title("Grafico de Linha.")
plt.xlabel("Índice")
plt.ylabel("Valor")

plt.plot(y, color="green")

plt.show()