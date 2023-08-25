'''
Este programa sirve para, 
segun las calorias
ingeridas, infromar al usuario
de cuantas calorias
le faltan para conseguir las 
calorias de mantenimiento 
(o en su defecto, por cuantas
calorias sobrepaso esta cantidad)
'''
'''
En esta parte estan los calculos
matematicos que se van a usar para 
el programa
'''
#Pide las variables de sexo, edad, peso y estatura al usuario
sexo=(input('Ingresa tu sexo como h para hombre y m para mujer. '))
edad=float(input('Ingresa tu edad en años. '))
peso=float(input('Ingresa tu peso en kg. '))
estatura=float(input('Ingresa tu estatura en cm. '))

#Crea la variable de calorias de mantenimiento
c_mantenimiento=0.0

#Decide que variante de la formula de Harris-Benedict usar segun el sexo
if sexo=='h': #Condicional para sexo masculino
    c_mantenimiento=(10.0*peso)
    c_mantenimiento=c_mantenimiento+(6.25*estatura)
    c_mantenimiento=c_mantenimiento-(5.0*edad)
    c_mantenimiento=c_mantenimiento+5.0
    print('Tus calorias de mantenimiento son '+str(c_mantenimiento))#Imprime las calorias de mantenimiento

elif sexo=='m': #Condicional para sexo femenino
    c_mantenimiento=(10.0*peso)
    c_mantenimiento=c_mantenimiento+(6.25*estatura)
    c_mantenimiento=c_mantenimiento-(5.0*edad)
    c_mantenimiento=c_mantenimiento-161.0
    print('Tus calorias de mantenimiento son '+str(c_mantenimiento))

#Pide ingresar las calorias consumidas hasta el momento
c_consumidas=float(input('Ingresa la cantidad de calorias ingeridas hasta el momento. '))

#Crea la variable de calorias resultantes
c_resultantes=0.0

#Decide si faltan o sobran calorias
if c_consumidas<c_mantenimiento: #Condicional si faltan calorias
    c_resultantes=c_mantenimiento-c_consumidas
    print('Faltan '+str(c_resultantes)+' calorias')#Imprime las calorias que faltan

elif c_consumidas>c_mantenimiento:#Condicional si sobran calorias
    c_resultantes=c_consumidas-c_mantenimiento
    print('Te has pasado por '+str(c_resultantes)+' calorias')#Imprime las calorías sobrantes