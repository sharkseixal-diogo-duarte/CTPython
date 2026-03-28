from matplotlib import pyplot as plt
x=[]
for i in range(-20,21):
    x.append(i)
y=[]
for j in x:
    if j<0:
        y.append(abs(j)**2)
    else:
        y.append(j**3)

y.sort()
plt.subplot(1,3,1)
plt.plot(x,y, color="#00008B",marker="d")
plt.title("Quadrados(Negativos) e Cubos(Positivos)")
plt.ylabel("Valor Calculado")
plt.xlabel("Numero Original")
plt.grid(True)

y_barras = []
for h in range(len(x)):
    if x[h]<0:
        y_barras.append(-y[h])
    else:
        y_barras.append(y[h])

plt.subplot(1,3,2)
plt.bar(x,y_barras,color="#FF00FF")
plt.title("Quadrados(Negativos) e Cubos(Positivos)")
plt.ylabel("Valor Calculado")
plt.xlabel("Numero Original")

for i in range(len(x)):
    if x[i]<0:
        cor = "red"
    elif x[i]>0:
        cor = "green"
    else:
        cor = "black"
    plt.subplot(1, 3, 3)
    plt.scatter(x[i],y[i],color=cor)
    plt.title("Quadrados(Negativos) e Cubos(Positivos)")
    plt.ylabel("Valor Calculado")
    plt.xlabel("Numero Original")
plt.show()