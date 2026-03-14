from matplotlib import pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x,y, color="red",linestyle="--",marker="o",label="seri1")

plt.title("exemplo")
plt.xlabel("x")
plt.ylabel("y")


plt.show()