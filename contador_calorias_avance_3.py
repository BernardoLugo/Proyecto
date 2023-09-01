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

#Crea una función devolverá el valor de las calorias de mantenimiento
def formula(sexo,edad,peso,estatura):

    #Crea la variable de calorias de mantenimiento
    c_mantenimiento=0.0

    #Decide que variante de la formula de Harris-Benedict usar segun el sexo
    if sexo=='h': #Condicional para sexo masculino
        c_mantenimiento=(10.0*peso)
        c_mantenimiento=c_mantenimiento+(6.25*estatura)
        c_mantenimiento=c_mantenimiento-(5.0*edad)
        c_mantenimiento=c_mantenimiento+5.0
        print('Tus calorias de mantenimiento son '+str(c_mantenimiento))#Imprime las calorias de mantenimiento
        return c_mantenimiento#Devuelve el valor de las calorias de mantenimiento

    elif sexo=='m': #Condicional para sexo femenino
        c_mantenimiento=(10.0*peso)
        c_mantenimiento=c_mantenimiento+(6.25*estatura)
        c_mantenimiento=c_mantenimiento-(5.0*edad)
        c_mantenimiento=c_mantenimiento-161.0
        print('Tus calorias de mantenimiento son '+str(c_mantenimiento))#Imprime las calorias de mantenimiento
        return c_mantenimiento#Devuelve el valor de las calorias de mantenimiento

#Crea una función que dará las calorías faltantes o sobrantes
def resultado(c_consumidas,sexo,edad,peso,estatura):

    #Crea la variable de calorias resultantes
    c_resultantes=0.0

    #Llama a la función de 'formula' para crear la variable de 'mantenimiento'
    mantenimiento=formula(sexo,edad,peso,estatura)

    #Decide si faltan o sobran calorias
    if c_consumidas<mantenimiento: #Condicional si faltan calorias
        c_resultantes=mantenimiento-c_consumidas
        print('Faltan '+str(c_resultantes)+' calorias')#Imprime las calorias que faltan

    elif c_consumidas>mantenimiento:#Condicional si sobran calorias
        c_resultantes=c_consumidas-mantenimiento
        print('Te has pasado por '+str(c_resultantes)+' calorias')#Imprime las calorías sobrantes

#Da al usuario la opción de elegir qué quiere saber
opcion=int(input('Ingresa 1 para saber tus calorias de mantenimiento o 2 para conocer las calorías resultantes'))

#Condicional para la opción 1
if opcion==1:
    #Pide las variables de sexo, edad, peso y estatura al usuario
    sexo=(input('Ingresa tu sexo como h para hombre y m para mujer. '))
    edad=float(input('Ingresa tu edad en años. '))
    peso=float(input('Ingresa tu peso en kg. '))
    estatura=float(input('Ingresa tu estatura en cm. '))

    formula(sexo,edad,peso,estatura)#Llama a la función de 'formula'

#Condicional para la opción 2
elif opcion==2:

    #Pide ingresar las calorias consumidas hasta el momento
    c_consumidas=float(input('Ingresa la cantidad de calorias ingeridas hasta el momento. '))

    #Pide las variables de sexo, edad, peso y estatura al usuario
    sexo=(input('Ingresa tu sexo como h para hombre y m para mujer. '))
    edad=float(input('Ingresa tu edad en años. '))
    peso=float(input('Ingresa tu peso en kg. '))
    estatura=float(input('Ingresa tu estatura en cm. '))

    resultado(c_consumidas,sexo,edad,peso,estatura)#Llama a la función de 'resultado'