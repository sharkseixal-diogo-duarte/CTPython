from matplotlib import pyplot as plt

plt.subplot(2,1,1)
plt.plot([1,2,3],[9,5,1])
plt.title("1")

plt.subplot(2,1,2)
plt.plot([3,21,1],[1,4,9])
plt.title("2")

#plt.savefig("grafico_linas.png")
plt.show()