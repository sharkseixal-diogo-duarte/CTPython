import matplotlib.pyplot as plot
import numpy as np
import time
plot.ion()

vals = []
indx = []

for i in range(1000):
    valor = np.random.normal(0,1)

    if np.random.rand()< 0.05:
        valor += np.random.choice([-10,-80,8,10])

    vals.append(valor)
    indx.append(i)

    des =  np.std(vals)
    media = np.mean(vals)

    limit = (media -3*des, media +3*des)

    plot.clf()
    plot.title("Anomalie detection")
    plot.xlabel("tempo")
    plot.ylabel("valor")

    vals_array = np.array(vals)
    outliers = (vals_array < limit[0]) | (vals_array > limit[1])
    plot.plot(indx,vals, color="blue", label ="Normal")
    plot.scatter(np.array(indx)[outliers], vals_array[outliers],color="red",label="Weird")

    plot.pause(0.2)

plot.ioff()
plot.show()
