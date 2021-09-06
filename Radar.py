import numpy as np

u = lambda t: np.piecewise(t,t>=0,[1,0])


T0=20
dutty=0.05 #5% 

t = np.linspace(-10, 10, 1000)
Vsignal = u(t-0)-u(t-T0*dutty)


import matplotlib.pyplot as plt
plt.figure()

plt.plot(t,Vsignal)

plt.xlabel('time')
plt.title('Señal radar')

plt.grid()
plt.show()

# punto 6
Vatenuate=Vsignal*0.5 #señal atenuada 50%
Vroll=np.roll(Vatenuate,200)
plt.figure()
plt.plot(t,Vroll)
plt.grid()
plt.xlabel('time')
plt.title('Señal retorno sin ruido')
plt.show()


#punto 7
noise = np.random.normal(0,0.3,1000)
Sretorno=Vatenuate+noise
plt.figure()
plt.plot(t,Sretorno)
plt.xlabel('time')
plt.title('Señal retornoc  DS=0.3')
plt.grid()
plt.show()
  
#punto 8
amplitud1=(np.max(Sretorno))
s=Sretorno/amplitud1
amplitud2=(np.max(Vsignal))
p=Vsignal/amplitud2
cor=np.correlate(p,s, mode='same')
plt.figure()
plt.title("Correlacion", fontsize = 20)
plt.plot (t, cor)
plt.grid()
plt.show()
amplitudCorrelacion=(np.max(cor))
print('La amplitd max de la señal es: ',amplitudCorrelacion)

#coordenadas del pico max (0, 24.9970)
#Energia de la señal
import scipy.integrate as integrate

energia = integrate.simps(cor,t)
print('La energía de la señal es: ',energia)


#8.C

noise = np.random.normal(0,0.7 ,1000) #desviación estandar de 0.7
Sretorno=Vatenuate+noise
plt.figure()
plt.plot(t,Sretorno)
plt.xlabel('time')
plt.title('Señal retorno DS= 0.7')
plt.grid()
plt.show()
  
#punto 8
amplitud1=(np.max(Sretorno))
s=Sretorno/amplitud1
amplitud2=(np.max(Vsignal))
p=Vsignal/amplitud2
cor=np.correlate(p,s, mode='same')
plt.figure()
plt.title("Correlacion", fontsize = 20)
plt.plot (t, cor)
plt.grid()
plt.show()
amplitudCorrelacion2=(np.max(cor))
print('Con desviacion estandar de 0.7: \n')
print('La amplitd max de la señal es: ',amplitudCorrelacion2)

#coordenadas del pico max (0, 11.9404)
#Energia de la señal
import scipy.integrate as integrate

energia2 = integrate.simps(cor,t)
print('La energía de la señal : ',energia2)
 # se concluye que a mayor desviacion estandar, se introduce mayor ruido a la la reñal que retorna
 #la amplitud maxima de la correlacion disminuye, es decir, aumenta la dificultad para reconocer las señal de retorno
