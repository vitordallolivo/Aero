import matplotlib.pyplot as plt  # plotar os graficos

#
# COISAS IMPORTANTES A MUDAR:
#   O RPM PARA CADA HELICE VAI MUDAR POR CONTA QUE NÃO FOI FEITO O ENSAIO ESTATICO
#   É BEM PROVAVEL QUE O CODIGO ESTEJA ERRADO
#

sl01 = []  # SL0 para helice 12x8
sl02 = []  # SL0 para helice 13x6.5
sl03 = []  # SL0 para helice 13x4
w = []  # array da força peso
t = [] #


g = 9.80665  # gravidade m/s²
p = 1.225 # densidade do ar em kg/m³
s = 0.454  # área
clmax = 0.561495
cd = 0.01511
u = 0.03  # coeficiente de atrito
arw = 11.35  # razão de aspecto
x = v0 = 10  # VELOCIDADE INICIAL
d = 0.5*p*(v0*v0)*s*cd  # ARRASTO
l = 0.5*p*(v0*v0)*s*clmax  # SUSTENTAÇÃO

y=0 # RPM  

#variaveis do polinomio
p00	=0
p10	=0
p01	=0
p20	=0
p11	=0
p02	=0
p30	=0
p21	=0
p12	=0
p03	=0
p40	=0
p31 =0
p22	=0
p13	=0
p04	=0
p50 =0
p41	=0
p32 =0
p23 =0
p14 =0
p05 =0

def kgfton(kgf):# transforma kgf para N
    N = kgf*9.80665
    return N


def polinomio(): # usa o polinomio para conseguir a tração estimada
    f = p00 + p10*x + p01*y + p20*x*x + p11*x*y + p02*y*y + p30*x*x*x + p21*x*x*y + p12*x*y*y + p03*y*y*y + p40*x*x*x*x + p31*x*x*x * \
         y + p22*x*x*y*y + p13*x*y*y*y + p04*y*y*y*y + p50*x*x*x*x*x + p41*x*x*x*x * \
             y + p32*x*x*x*y*y + p23*x*x*y*y*y + p14*x*y*y*y*y + p05*y*y*y*y*y


    f=kgfton(f) # resultado do pol é em kgf
    return(f)

for i in range(0, 3): # Quantidade helices
    if(i == 0): # 12X8 e suas constantes
        y=8800 # esse numero é de acordo com os testes na bandaca
        p00	=	-0.05604
        p10	=	-0.01264
        p01	=	0.000109
        p20	=	-0.001797
        p11	=	9.06E-06
        p02	=	-1.79E-08
        p30	=	2.21E-05
        p21	=	-2.25E-07
        p12	=	-8.50E-10
        p03	=	8.36E-12
        p40	=	2.25E-07
        p31	=	3.03E-10
        p22	=	6.34E-12
        p13	=	2.72E-14
        p04	=	-4.77E-16
        p50	=	-2.45E-08
        p41	=	3.35E-10
        p32	=	-1.86E-12
        p23	=	3.95E-15
        p14	=	-1.96E-18
        p05	=	8.46E-21
        t.append(polinomio())
        
    if(i == 1):  # 13X6.5 e suas constantes
       y = 8800  # RPM
       p00 = -0.04286
       p10 = -0.004896
       p01 = 7.054e-05
       p20 = 0.001271
       p11 = -1.214e-05
       p02 = 1.372e-08
       p30 = 0.0001768
       p21 = -2.129e-06
       p12 = 5.302e-09
       p03 = 2.404e-12
       p40 = -7.498e-08
       p31 = -2.942e-08
       p22 = 3.041e-10
       p13 = -7.452e-13
       p04 = 8.064e-18
       p50 = -2.449e-08
       p41 = 1.99e-10
       p32 = 8.88e-13
       p23 = -1.266e-14
       p14 = 3.072e-17
       p05 = -4.023e-21
       t.append(polinomio()) # colocar no array o valor retirado do polinomio
       

    if(i == 2):  # 13X4 e suas constantes
       y = 8800  # RPM
       p00 = -0.02418
       p10 = -0.01194
       p01 = 5.135e-05
       p20 = -0.002071
       p11 = 3.627e-06
       p02 = 8.776e-10
       p30 = 2.723e-05
       p21 = 7.005e-08
       p12 = -2.334e-09
       p03 = 5.688e-12
       p40 = 7.73e-07
       p31 = -6.481e-09
       p22 = -2.464e-12
       p13 = 2.113e-13
       p04 = -4.804e-16
       p50 = -3.806e-09
       p41 = -4.713e-11
       p32 = 3.673e-13
       p23 = -1.531e-16
       p14 = -6.916e-18
       p05 = 1.563e-20
       t.append(polinomio())



# tração máximas para cada helices
helice=[t[0],t[1],t[2]] #12x8 , 13x6.5 , 13x4 RIMFIRE


def calculo(w1,t): # calculo do Sl0
	temp=((1.44*w1*w1)/(g*p*s*clmax*(t-(d+u*(w1-l)))))
	return(temp)
    
for i in range(10,100):
	w.append(i) # de 10N ate 50N	

for j in range(0,3): # diz qual helice 
	for i in range(0,90):
		if j == 0:
			sl01.append(calculo(w[i],helice[j]))
		if j == 1:
			sl02.append(calculo(w[i],helice[j]))
		if j == 2:
 			sl03.append(calculo(w[i],helice[j]))
             
    
 			
ax = plt.subplot(111)
# plt.title('Rimfire, 70% tração máxima')
plt.title('Rimfire, 100% tração máxima')
plt.ylim(0,58); # limitando o grafico até 58m
plt.xlim(10,60)
plt.plot(w,sl01,label='Helice: 12x8, v0=10m/s,RPM=8800')
plt.plot(w,sl02,label='Helice: 13x6.5, v0=10m/s,RPM=8800')
plt.plot(w,sl03,label='Helice: 13x4, v0=10m/s,RPM=8800')
plt.grid()

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)