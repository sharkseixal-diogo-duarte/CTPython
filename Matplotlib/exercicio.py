from matplotlib import pyplot as plt
import numpy
x = numpy.random.randint(0,51,100)
y = numpy.random.randint(0,51,100)
z = numpy.random.randint(0,51,100)

plt.subplot(2,1,1)
plt.hist(x,bins=10, color="red",edgecolor="black")
plt.title("histograma")

plt.subplot(2,1,2)
plt.scatter(x,y, color="green",label="seri1")
plt.title("grafico de disperção")

plt.show()