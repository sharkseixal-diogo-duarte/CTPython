from matplotlib import pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
plt.plot(x,y,linestyle="--",color="purple",marker="o")
plt.title("quadrados")
plt.xlabel("numeros")
plt.ylabel("quadrado dos numeros")
plt.grid(True)
plt.show()
