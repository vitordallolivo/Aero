import matplotlib.pyplot as plt  # plotar os graficos
import math


sl01 = []  # SL0 para helice 12x8 RIMFIRE
sl02 = []  # SL0 para helice 13x6.5 RIMFIRE
sl03 = []  # SL0 para helice 13x4 RIMFIRE

sl04 = []  # SL0 para helice 12x8 OS
sl05 = []  # SL0 para helice 13x6.5 OS
sl06 = []  # SL0 para helice 13x4 OS

w = []  # array da força peso
v=[] # velocidade

r12x8 = []  # 12x8  RIMFIRE
r13x65 = []  # 13x6.5 RIMFIRE
r13x4 = []  # 13x4  RIMFIRE

os12x8 = []  # 13x4  OS
os13x65 = []  # 13x6.5  OS
os13x4 = []  # 13x4  OS

g = 9.80665  # gravidade m/s²
p = 1.225  # densidade do ar em kg/m³

zw = 0.185  # Altura do CA
b = 2.27
efeitosolo = ((16*zw/b)**2)/(1+(16*zw/b)**2)  # efeito solo

e0 = 0.89285714  # valor não repassado
cd0 =0.01511  # coeficiente de arrasto inicial
v0 = 0  # velocidade a ser mudada
cd = 0  # coeficiente de arrasto
s = 0.454  # área
clmax = 1.775279
u = 0.03  # coeficiente de atrito da pista
arw = 11.35  # razão de aspecto

cl = 0
d = 0.5*p*(v0*v0)*s*cd0  # ARRASTO
l = 0.5*p*(v0*v0)*s*clmax  # SUSTENTAÇÃO

k = 1/(3.1415*e0*arw)

# variaveis do polinomio
p00 = 0
p10 = 0
p01 = 0
p20 = 0
p11 = 0
p02 = 0
p30 = 0
p21 = 0
p12 = 0
p03 = 0
p40 = 0
p31 = 0
p22 = 0
p13 = 0
p04 = 0
p50 = 0
p41 = 0
p32 = 0
p23 = 0
p14 = 0
p05 = 0


def arrasto():
    d = 0.5*p*(0.7*v0)*(0.7*v0)*s*(cd0+efeitosolo*k*cl*cl)
    return d


def sustentacao():
    l = 0.5*p*(0.7*v0)*(0.7*v0)*s*cl
    return l


def decolagem(w1, t):  # COMPRIMENTO DE PISTA DE DECOLAGEM
    temp = ((1.44*w1*w1)/(g*p*s*clmax*(t-(d+u*(w1-l)))))
    return(temp)


def vdecolagem(wi): # VELOCIDADE DE DECOLAGEM
    vest = math.sqrt((2*wi)/(p*s*clmax))  # calcula velocidade estol
    return(1.2*vest)  # retorna velocidade de manobra que é 1.2*vestol


def cllo():  # Coefieciente de sustentação ideal
    csi = (3.14156*e0*arw*u)/2*efeitosolo
    return csi


def kgfton(kgf):  # transforma kgf para N
    N = kgf*9.80665
    return N


# usa o polinomio para conseguir a tração estimada
def polinomio(x, y,p00,p10,p01,p20,p11,p02,p30,p21,p12,p03,p40,p31,p22,p13,p04,p50,p41,p32,p23,p14,p05):

    f = p00 + p10*x + p01*y + p20*x*x + p11*x*y + p02*y*y + p30*x*x*x + p21*x*x*y + p12*x*y*y + p03*y*y*y + p40*x*x*x*x + p31*x*x*x * \
        y + p22*x*x*y*y + p13*x*y*y*y + p04*y*y*y*y + p50*x*x*x*x*x + p41*x*x*x*x * \
        y + p32*x*x*x*y*y + p23*x*x*y*y*y + p14*x*y*y*y*y + p05*y*y*y*y*y

    f = kgfton(f)  # resultado do pol é em kgf
    return(f)


def helice(v0):

    p00 = -0.05604
    p10 = -0.01264
    p01 = 0.000109
    p20 = -0.001797
    p11 = 9.06E-06
    p02 = -1.79E-08
    p30 = 2.21E-05
    p21 = -2.25E-07
    p12 = -8.50E-10
    p03 = 8.36E-12
    p40 = 2.25E-07
    p31 = 3.03E-10
    p22 = 6.34E-12
    p13 = 2.72E-14
    p04 = -4.77E-16
    p50 = -2.45E-08
    p41 = 3.35E-10
    p32 = -1.86E-12
    p23 = 3.95E-15
    p14 = -1.96E-18
    p05 = 8.46E-21
    r12x8.append(polinomio(v0, 6630,p00,p10,p01,p20,p11,p02,p30,p21,p12,p03,p40,p31,p22,p13,p04,p50,p41,p32,p23,p14,p05))

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
    r13x65.append(polinomio(v0,8800,p00,p10,p01,p20,p11,p02,p30,p21,p12,p03,p40,p31,p22,p13,p04,p50,p41,p32,p23,p14,p05))

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
    r13x4.append(polinomio(v0, 7860,p00,p10,p01,p20,p11,p02,p30,p21,p12,p03,p40,p31,p22,p13,p04,p50,p41,p32,p23,p14,p05))

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
    os13x65.append(polinomio(v0, 9090,p00,p10,p01,p20,p11,p02,p30,p21,p12,p03,p40,p31,p22,p13,p04,p50,p41,p32,p23,p14,p05))

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
    os13x4.append(polinomio(v0, 10600,p00,p10,p01,p20,p11,p02,p30,p21,p12,p03,p40,p31,p22,p13,p04,p50,p41,p32,p23,p14,p05))


cl = cllo()

for i in range(10, 100):
    w.append(i)
    v0 = vdecolagem(w[i-10])  # velocidade de manobra
    l = sustentacao()
    d = arrasto()
    helice(v0)

for i in range(0, len(w)):
    temp=decolagem(w[i], r12x8[i])
    if(temp<=58):
        sl01.append(temp)
        valor1=i
    temp=decolagem(w[i], r13x65[i])
    if(temp<=58):
        sl02.append(temp)
        valor2=i
    temp=decolagem(w[i], r13x4[i])
    if(temp<=58):
        sl03.append(temp)
        valor3=i
    temp =decolagem(w[i], os13x65[i])
    if(temp<=58):
        sl05.append(temp)
        valor5=i
    temp=decolagem(w[i], os13x4[i])
    if(temp<=58):
        sl06.append(temp)
        valor6=i

w1=[]
w2=[]
w3=[]
w5=[]
w6=[]

for i in range(1,valor1+2):
    w1.append(i*0.6)
for i in range(1,valor2+2):
    w2.append(i*0.6)
for i in range(1,valor3+2):
    w3.append(i*0.6)
for i in range(1,valor5+2):
    w5.append(i*0.6)
for i in range(1,valor6+2):
    w6.append(i*0.6)


print('MTOW R12x8: ',max(w1))
print('MTOW R13x6.5: ',max(w2))
print('MTOW R13x4: ',max(w3))
print('MTOW OS13X4: ',max(w5))
print('MTOW OS13X6.5: ',max(w6))

    
r12x8=[]
r13x65=[]
r13x4=[]
os13x4=[]
os13x65=[]

for i in range(1,350):
    v.append(i/10)
    helice(v[i-1])



ax = plt.subplot(111)
plt.title('Rimfire - Tração por velocidade')
plt.xlabel('Velocidade(m/s)')
plt.ylabel('Tração')
plt.plot(v,r12x8 , label='Helice: 12x8,RPM=6630')
plt.plot(v,r13x65, label='Helice: 13x6.5,RPM=8800')
plt.plot(v,r13x4, label='Helice: 13x4,RPM=7860')
plt.grid()
plt.ylim(0,40)
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=7)
plt.show()

ax = plt.subplot(111)
plt.title('OS - Tração por velocidade')
plt.xlabel('Velocidade(m/s)')
plt.ylabel('Tração')
plt.plot(v,os13x4, label='Helice: 13x6.5,RPM=8800')
plt.plot(v,os13x65, label='Helice: 13x4,RPM=7860')
plt.ylim(0,40)
plt.grid()
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=7)
plt.show()


ax = plt.subplot(111)
plt.title('Rimfire - Comprimento de Pista decolagem')
plt.xlabel('Comprimento de pista(m)')
plt.ylabel('60% do MTOW(N)')
plt.plot(sl01, w1, label='Helice: 12x8,RPM=6630')
plt.plot(sl02, w2, label='Helice: 13x6.5,RPM=8800')
plt.plot(sl03, w3, label='Helice: 13x4,RPM=7860')
plt.xlim(0, 58)
plt.grid()
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=7)
plt.show()

ax = plt.subplot(111)
plt.title('OS - Comprimento de Pista decolagem')
plt.plot(sl05,w5, label='Helice: 13x6.5,RPM=9090')
plt.plot(sl06,w6, label='Helice: 13x4,RPM=10600')
plt.xlabel('Comprimento de pista(m)')
plt.ylabel('60% do MTOW(N)')
plt.xlim(0, 58)
plt.grid()
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.show()
