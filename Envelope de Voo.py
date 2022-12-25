# -*- coding: utf-8 -*-
"""
13x4 OS e 10600 RPM

"""
import matplotlib.pyplot as plt  # plotar os graficos
import math

# vetores
rc = []
tr = []  # tração requerida
v0 = []  # velocidade em 0 metros de altitude
v100 = []  # velocidade em 100 metros de altitude

vestol = [] # velocidade de estol para o envelope
vmanobra = [] #velocidade de manobra para o envelope
vcru = [] # velocidade de cruzeiro para o envelope

vh=[] # velocidade horizontal para planeio
rd=[] # Razão de descida
vdecol=0 # velocidade de decolagem

lsus=[]

cd = []  # coeficiente de arrasto
td = []  # tração disponivel
pd = []  # potencia disponivel
pr = []  # potencia requerida
cd100 = []
td100 = []
tr100 = []
pr100 = []
pd100 = []

vmin = []  # velocidade zero
vmax = []  # velocidade maxima

p = [1.225,		1.219043466,	1.208153728,	1.197330582,	1.186573824,	1.17588325,	1.165258656,	1.154699838,	1.144206592,	1.133778714,	1.123416,	1.113118246,	1.102885248,	1.092716802,	1.082612704,	1.07257275,	1.062596736,	1.052684458,	1.042835712,	1.033050294,	1.023328,	1.013668626,	1.004071968,	0.994537822,	0.985065984,	0.97565625,	0.966308416,	0.957022278,	0.947797632,	0.938634274,	0.929532,	0.920490606,	0.911509888,	0.902589642,	0.893729664,	0.88492975,	0.876189696,	0.867509298,	0.858888352,	0.850326654,	0.841824,	0.833380186,	0.824995008,	0.816668262,	0.808399744,	0.80018925,	0.792036576,	0.783941518,	0.775903872,	0.767923434,	0.76,	0.752133366,	0.744323328,	0.736569682,	0.728872224,	0.72123075,	0.713645056,	0.706114938,	0.698640192,	0.691220614,	0.683856,	0.676546146,	0.669290848,	0.662089902,	0.654943104,	0.64785025,	0.640811136,	0.633825558,	0.626893312,	0.620014194,	0.613188,	0.606414526,	0.599693568,	0.593024922,	0.586408384,	0.57984375,	0.573330816,	0.566869378,	0.560459232,	0.554100174,	0.547792,	0.541534506,	0.535327488,	0.529170742,	0.523064064,	0.51700725,	0.511000096,	0.505042398,	0.499133952,	0.493274554,	0.487464,	0.481702086,	0.475988608,	0.470323362,	0.464706144,	0.45913675,	0.453614976,	0.448140618,	0.442713472,	0.437333334,	0.432,	0.426713266,	0.421472928,	0.416278782,	0.411130624,	0.40602825,	0.400971456,	0.395960038,	0.390993792,	0.386072514,	0.381196,	0.376364046,	0.371576448,	0.366833002,	0.362133504,	0.35747775,	0.352865536,	0.348296658,	0.343770912,	0.339288094,	0.334848,	0.330450426,	0.326095168,	0.321782022,	0.317510784,	0.31328125,	0.309093216,	0.304946478,	0.300840832,	0.296776074,	0.292752,	0.288768406,	0.284825088,	0.280921842,	0.277058464,	0.27323475,	0.269450496,	0.265705498,	0.261999552,	0.258332454,	0.254704,	0.251113986,	0.247562208

     ]

# densidades do ar

n = []  # fator de carga
nmax = 0  # fator de carga máximo

# constantes
p0 = 1.225  # densidade do ar em kg/m³
s = 0.454  # área
cd0 = 0.01511  # coeficiente de arrasto inicial
pi = math.pi  # pi
arw = 11.35  # razão de aspecto
w = 47.82  # Peso

alpha = 8  # angulo de estol

alphah = -8  # MUDAR

sh = 0.0332
sw = 0.454

e0 = 0.89285714  # pegar com a aerodinamica
clmax = 1.775279  # coeficiente máximo de  sustentação
cl = 0

iw = 0
cl0h = -0.203  # Coeficiente de sustentação inicial do EH
cl0w = 0.561495  # Coeficiente de sustentação inicial da asa
clalphah = 0.0651
clalphaw = 0.0769


cl0 = 0.6708  # coeficiente inicial de sustentação
clh_decolagem = -0.203
g = 9.80665  # gravidade m/s²

x = []  # altura
x1 = []

zw = 0.185  # Altura do CA
b = 2.27

efeitosolo = ((16*zw/b)**2)/(1+(16*zw/b)**2)  # efeito solo
print('Efeito solo: ', efeitosolo)

k = 1/(3.1415*e0*arw)  # constante de oswald

temp = 0  # memoria temporaria

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


def vcruzeiro(td, rho):
    clw = cl0w + clalphaw*(iw+alpha)
    clh = -cl0h+clalphah*(alphah)
    vcru = math.sqrt(abs((2*(w-math.sin(alpha)))/(rho*(sw*clw + sh*clh))))
    return (vcru)

def eficientedinamica(cl):
    cd=cd0 + (cl*cl)/(pi*e0*arw)
    e = cl/cd
    delta = math.atan(1/e)
    return delta,cl
    
def velocidadeplaneio(delta,cl):
    v = math.sqrt((2*w*delta)/(p0*s*cl))
    vh = v*math.cos(delta)
    rd = -v*math.sin(delta)
    return(v,vh,rd)

def nmax(rho):
    n=math.sqrt((rho*14*14*sw*clmax)/(2*w))
    return n

def fvmano(nmax,ve):
    vmano = ve*math.sqrt(nmax)
    return(vmano)

def fvestol(rho, td,v0):
    ve = math.sqrt((2*w)/(rho*(sw*clmax+sh*clmax)))
    return (ve)

def kgfton(kgf):  # transforma kgf para N
    N = kgf*9.80665
    return N


def polinomio(x):  # usa o polinomio para conseguir a tração estimada
    y = 10600

    f = p00 + p10*x + p01*y + p20*x*x + p11*x*y + p02*y*y + p30*x*x*x + p21*x*x*y + p12*x*y*y + p03*y*y*y + p40*x*x*x*x + p31*x*x*x * \
        y + p22*x*x*y*y + p13*x*y*y*y + p04*y*y*y*y + p50*x*x*x*x*x + p41*x*x*x*x * \
        y + p32*x*x*x*y*y + p23*x*x*y*y*y + p14*x*y*y*y*y + p05*y*y*y*y*y

    f = kgfton(f)  # resultado do pol é em kgf

    return(f)


def calcd(vel, p):  # CALCULA O COEFICIENTE DE ATRITO
    cl = 2*w/(p*vel*vel*s)
    temp = cd0 + (cl*cl)/(pi*e0*arw)
    return temp


def arrasto(v0,efeitosolo,cl):
    d = 0.5*p0*(0.7*v0)*(0.7*v0)*s*(cd0+efeitosolo*k*cl*cl)
    return d


def sustentacao(v0,cl):
    l = 0.5*p0*(0.7*v0)*(0.7*v0)*s*cl
    return l

for i in range(1, 350):
    v0.append(i/10)  # cria a velocidade
    td.append(polinomio(v0[i-1]))  # retorna a tração disponivel
    cd.append(calcd(v0[i-1], p0))  # retorna o cd

    pd.append(td[i-1]*v0[i-1])  # retorna a potência disponivel
    temp = 0.5*p0*v0[i-1]*v0[i-1]*s*cd[i-1]
    
    n.append((p0*v0[i-1]*v0[i-1]*s*clmax)/(2*w))

    tr.append(temp)  # tração requisitada
    pr.append(temp*v0[i-1])  # potencia requisitada

for i in range(len(v0)):
    cl = 2*w/(p0*v0[i]*v0[i]*sw)
    lsus.append(sustentacao(v0[i], clmax))
    if(lsus[i]>=w and vdecol==0):
        vdecol = v0[i]


for i in range(1, 350):
    v100.append(i/10)  # cria a velocidade
    td100.append(polinomio(v0[i-1]))  # retorna a tração disponivel
    cd100.append(calcd(v0[i-1], p[21]))  # retorna o cd

    pd100.append(td100[i-1]*v0[i-1])  # retorna a potência disponivel
    temp = 0.5*p[11]*v0[i-1]*v0[i-1]*s*calcd(v0[i-1], p[21])

    tr100.append(temp)  # tração requisitada
    pr100.append(temp*v0[i-1])  # potencia requisitada


n=[]
for i in range(len(p)):
    n.append(nmax(p[i]))
nmax=max(n)
nmax=2
    
print('Tamanho do vetor do rhos: ',len(p)+1)

for i in range(len(p)):
    intersec = []
    for j in range(0, len(v0)):

        tdh = td[j]*(p[i]/p0)

        temp = 0.5*p[i]*v0[j]*v0[j]*s*(calcd(v0[j], p[i]))
        tempve=fvestol(p[i], tdh,v0[j])
        tempvmano = fvmano(nmax,tempve)
        vestol.append(tempve)
        vmanobra.append(tempvmano)
        vcru.append(vcruzeiro(tdh, p[i]))
        
        if((tdh-temp) < 1 and (tdh-temp) > -1):
            intersec.append(j/10)

    if(intersec):
        vmin.append(min(intersec))
        vmax.append(max(intersec))

razaold=0
for i in range(1,8): 
    tempcl=i*0.2
    tempdelta, tempcd =eficientedinamica(tempcl)
    tempv,tempvh, temprd = velocidadeplaneio(tempdelta, tempcl)
    
    tempL = sustentacao(tempv,tempcl)
    tempD = arrasto(tempv,1,tempcl)
    
    vh.append(tempvh)
    rd.append(temprd)
    if (tempL/tempD > razaold):
        razaold=tempL/tempD

deltamin = math.atan(razaold)
print(deltamin)

for i in range(len(p)):
    x.append(i*100)

for i in range(len(vcru)):
    x1.append((i*100)/len(v0))

for i in range(0, 349):  # razão de subida
    temp = (pd[i]-pr[i])/w
    rc.append(temp)

for j in range(0, 349):
    if(rc[j] > temp):
        temp = rc[j]
        vmaxtorc = j/10  # velocidade máxima na razão de subida

teta = (math.asin(((max(rc))/(vmaxtorc)))*180)/pi
print(teta)
print('Velocidade Decolagem: ',vdecol)
print('Velocidade Cruzeiro(0m):',vcru[0])
print('Velocidade de Manobra(0m):',vmanobra[0])
print('Velocidade Minima(0m):',vmin[0])
print('Velocidade Máxima(0m):',vmax[0])
print('Velocidade de Estol(0m):',vestol[0])
print('Nmax:',nmax)

ax = plt.subplot(111)
plt.title('Sustentação')
plt.plot(v0, lsus,label='Velocidade de decolagem')
plt.xlabel('Velocidade(m/s)')
plt.ylim(0,w)
plt.xlim(0,vdecol)
plt.ylabel('Sustentação(N)')
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.grid()
plt.show()



ax = plt.subplot(111)
plt.title('Curvas de Tração')
plt.ylim(0, 60)
plt.plot(v0, td, label='Tração disponivel')
plt.plot(v0, tr, label='Tração requerida')
plt.plot(v100, tr100, '-.',label='Tração requerida a 100m')
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.grid()
plt.show()

ax = plt.subplot(111)
plt.title('Curvas de Potência')
plt.plot(v0, pd, label='Potência disponivel')
plt.ylim(0, 600)
plt.plot(v0, pr, label='Potência requerida')
plt.ylabel('Potência(Watts)')
plt.xlabel('Velocidade(m/s)')
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.grid()
plt.show()

ax = plt.subplot(111)
plt.title('Polar de velocidade subida')
plt.plot([0, vmaxtorc], [0, max(rc)], '-.',label='Ângulo: 21.52º Graus')
plt.plot(v0, rc, label='Razão de subida por m/s')
plt.xlabel('Velocidade(m/s')
plt.ylabel('Altura(m')
plt.ylim(0, 6)
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.grid()
plt.show()


#print(deltamin,min(vh))

ax = plt.subplot(111)
plt.xlabel('Velocidade(m/s)')
plt.ylabel('Razão de descida(m/s)')
plt.title('Polar de velocidade descida')
plt.plot(vh, rd, label='Razão de descida por m/s')
plt.plot([0,8],[0,-0.39],'-.',label='Ângulo: 1.52º Graus')
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.grid()
plt.show()

plt.plot()

ax = plt.subplot(111)
plt.title('Envelope de voô')
plt.ylabel('Altitude(m)')
plt.xlabel('Velocidade(m/s)')
plt.plot(vmin, x, label='Vmin')
plt.plot(vmax, x, label='Vmax')
plt.plot(vestol, x1, label='Vestol')
plt.plot(vmanobra, x1, label='Vmanobra')
plt.plot(vcru, x1, label='Vcru')
plt.grid()
ax.legend(loc='upper center', bbox_to_anchor=(
    0.5, -0.15), fancybox=True, shadow=True, ncol=5)
plt.show()
