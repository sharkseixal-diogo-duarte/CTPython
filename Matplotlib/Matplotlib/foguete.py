from matplotlib import pyplot as plt
import numpy

# tempo_s,velocidade_ms,aceleracao_ms2,altitude_m,combustivel_pct


    open("foguete.txt","r",encoding="utf-8") as file:


variaveis = numpy.array([(0,2,9,0,100),(1,12,10,5,99.7),(2,25,11,18,99.3),(3,40,13,40,98.8),(4,58,15,72,98.2)])

plt.subplot(1,2,1)
plt.scatter([variaveis[0][0],variaveis[1][0],variaveis[2][0],variaveis[3][0],variaveis[4][0]],[variaveis[0][1],variaveis[0][2],variaveis[0][3],variaveis[0][4]])


plt.show()