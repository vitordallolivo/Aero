import matplotlib.pyplot as plt # plotar os graficos

sl01=[] # SL0 para helice 12x8
sl02=[] # SL0 para helice 13x6.5
sl03=[] # SL0 para helice 13x4

w=[] # array com varios pesos

# trações máximas para cada helices
helicer=[15.30818*0.7,28.14509*0.7,23.76151*0.7] #12x8 , 13x6.5 , 13x4 RIMFIRE

g=9.81 
p=1.225
s=0.454
clmax=0.561495
cd=0.01511
u=0.03
arw= 11.35 
v0=10 # VELOCIDADE INICIAL
d= 0.5*p*(v0*v0)*s*cd # ARRASTO
l= 0.5*p*(v0*v0)*s*clmax # SUSTENTAÇÃO

def calculo(w1,t): # calculo do Sl0
	temp=((1.44*w1*w1)/(g*p*s*clmax*(t-(d+u*(w1-l)))))
	return(temp)
    
for i in range(10,50):
	w.append(i) # de 100N ate 500N	

for j in range(0,3): # diz qual helice 
	for i in range(0,40):
		if j == 0:
			sl01.append(calculo(w[i],helicer[j]))
		if j == 1:
			sl02.append(calculo(w[i],helicer[j]))
		if j == 2:
 			sl03.append(calculo(w[i],helicer[j]))
 			
ax = plt.subplot(111)
plt.title('Rimfire, 70% tração máxima')
plt.ylim(0,58); # limitando o grafico até 58m

plt.plot(w,sl01,label='Helice: 12x8, v0=10m/s')
plt.plot(w,sl02,label='Helice: 13x6.5, v0=10m/s')
plt.plot(w,sl03,label='Helice: 13x4, v0=10m/s')
plt.grid()

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=5)