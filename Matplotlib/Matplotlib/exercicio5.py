from matplotlib import pyplot as plt
import numpy

numeros = numpy.random.normal(2,1,500)

plt.subplot(1,3,1)
plt.hist(numeros,10,color="teal",edgecolor="gray")
plt.title("Histograma Normal")

x_barras = []
for i in range(1,11):
    a=2**i
    x_barras.append(a)

plt.subplot(1,3,2)
plt.bar(x_barras,10,color="blue")
plt.title("Potências de 2")

x = numpy.random.rand(150)
y = numpy.random.rand(150)
print(x,y)


plt.subplot(1,3,3)
plt.scatter(x,y,color="green")
plt.title("Scatter Aleatório")
plt.show()