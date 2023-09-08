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

#Crea una función que pide la actividad del usuario y regresa un valor 
# correspondiente a la proteína que deberá de consumir
def actividad_fisica(actividad):
    if actividad == 1:#Condicional para opción 1
        proteina=2.0
    elif actividad == 2:#Condicional para opción 2
        proteina=1.5
    elif actividad == 3:#Condicional para opción 3
        proteina=1.0
    return proteina

#Crea una función que da las calorías que debe de comer el usuario según su peso
def objetivo_proteina(peso):
    proteina=actividad_fisica(actividad)#Llama a la función de actividad_fisica
    proteina_necesaria=proteina*peso#Multiplica el peso por lo que regresa la función anterior

    #Imprime los gramos de proteina que debe de consumir el usuario
    print('Los gramos de proteina que debes consumir son '+str(proteina_necesaria))


#Da al usuario la opción de elegir qué quiere saber
opcion=int(input('Ingresa \n 1 para saber tus calorias de mantenimiento \n 2 para conocer las calorías resultantes \n 3 para conocer la proteina que debes ingerir'))

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

#Condicional para la opción 3
elif opcion==3:

    #Pide ingresar un valor correspondiente a la actividad física
    print('Entrenamiento de fuerza: 1  Entrenamiento aeróbico: 2  Sin entrenamiento: 3')
    actividad=int(input('Ingresa el numero correspondiente a tu actividad fisica '))

    #Pide ingresar el peso
    peso=float(input('Ingresa tu peso en kg '))
    objetivo_proteina(peso)