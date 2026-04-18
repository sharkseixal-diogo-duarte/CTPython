import matplotlib.pyplot as plot
import numpy as np
import time
plot.ion() # modo interativo

x_vals = []
y_vals = []

pontos = 100

for i in range(1000):
    x = i*0.05
    y = np.sin(x) + np.random.normal(0, 0.2)

    x_vals.append(x)
    y_vals.append(y)

    if len(x_vals) > pontos:
        x_vals = x_vals[-pontos:]
        y_vals = y_vals[-pontos:]

    plot.clf()
    plot.plot(x_vals, y_vals, color="blue")
    plot.title("Sinal sinusoidal")
    plot.xlabel("tempo")
    plot.ylabel("ampitude")
    plot.pause(0.05)

plot.ioff()
plot.show()
