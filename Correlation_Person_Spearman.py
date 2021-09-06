import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# A. Lectura del archivo y creacion de los vectores columnas de edad, nota de informatica, nota de calculo.

# Abrir el archivo xlsx.
excel_file = 'DatosCorrelacion.xlsx'
archivo = pd.read_excel(excel_file)

# Extraemos los datos y los guardamos en vectores.
edad=archivo['Edad'].values
ncal=archivo['Nota calculo'].values
ninf=archivo['Nota informatica'].values

# Imprimo los datos para verificar la lectura.
print("A. Columnas del documento de excel: \n")
print("Edad: {}".format(edad),"\n")
print("N. Calculo: {}".format(ncal),"\n")
print("N. Informatica: {}".format(ninf),"\n")

# B. Graficar vectores.
print("B. Graficas para los vectores: \n")

# Configuro paramatros para graficar Calculo Vs Informatica.
plt.ylabel("informatica", fontsize = 20)
plt.xlabel("Calculo", fontsize = 20)
plt.title("Calculo Vs Informatica", fontsize = 20)
plt.plot(ncal,ninf,'o',label='Calculo Vs Informatica')
plt.grid()
plt.legend()

# Configuro paramatros para graficar Edad Vs Calculo.
plt.figure()
plt.subplot(211)
plt.ylabel("Calculo", fontsize = 20)
plt.xlabel("Edad", fontsize = 20)
plt.title("Calculo Vs Edad", fontsize = 20)
plt.plot(edad,ncal,'o', color='r',label='Calculo Vs Edad')
plt.grid()
plt.legend()
plt.show()

# C. Calculo de coeficientes de Pearson y Sperarman.

print("Calculo de coeficientes de Pearson y Sperarman. \n")

# Hallar Coeficiente de correlacion de Pearson
print("Coeficiente de Pearson Calculos Vs Informatica: {}".format(archivo.corr(method="pearson")["Nota calculo"]["Nota informatica"]))
print("Coeficiente de Pearson Edad Vs Calculo: {}".format(archivo.corr(method="pearson")["Edad"]["Nota calculo"]),"\n")

# Hallar coeficiente de correlacion de spearman
print("Coeficiente de spearman Calculos Vs Informatica: {}".format(archivo.corr(method="spearman")["Nota calculo"]["Nota informatica"]))
print("Coeficiente de spearman Edad Vs Calculo: {}".format(archivo.corr(method="spearman")["Edad"]["Nota calculo"]),"\n")
