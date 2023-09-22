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

#Crea una función que calcula las calorias consumidas en una comida según los alimentos
def comida():
    alimento=input('Ingresa si has comido. si/no ')#Crea la variable que iniciará el ciclo
    calorias_comida=0#Asigna el valor 0 a la variable que se regresará al final del ciclo
    while alimento=="si":#Empieza el ciclo while
        calorias_g=0#Crea la variable que almacenará las calorías según el alimento
        print('¿Qué tipo de alimento? ')
        tipo_a=input('fruta/verdura/cereal/carne/grasa ')#variable que almacena el tipo de alimento
        if tipo_a=='fruta':#Condicional para fruta
            print('¿Qué fruta ingeriste? ')
            t_alim=input('naranja/manzana/fresa/platano ')#variable que almacena el tipo de fruta
            if t_alim=='naranja':#condicional para naranja
               calorias_g=0.47
            elif t_alim=='manzana':#condicional para manzana
               calorias_g==0.52
            elif t_alim=='fresa':#condicional para fresa
               calorias_g==0.33
            elif t_alim=='platano':#condicional para platano
               calorias_g==0.89
        elif tipo_a=='verdura':#condicional para verdura
            print('¿Qué verdura ingeriste? ')
            t_alim=input('lechuga/pepino/apio/brocoli ')#variable que almacena el tipo de verdura
            if t_alim=='lechuga':#condicional para lechuga
               calorias_g=0.15
            elif t_alim=='pepino':#condicional para pepino
               calorias_g==0.15
            elif t_alim=='apio':#condicional para apio
               calorias_g==0.12
            elif t_alim=='brocoli':#condicional para brocoli
               calorias_g==0.34
        elif tipo_a=='cereal':#condicional para cereal
            print('¿Qué cereal ingeriste? ')
            t_alim=input('avena/arroz/pasta/tortilla ')#variable que almacena tipo de cereal
            if t_alim=='avena':#condicional avena
               calorias_g=0.68
            elif t_alim=='arroz':#condicional arroz
               calorias_g==1.3
            elif t_alim=='pasta':#condicional para pasta
               calorias_g==1.31
            elif t_alim=='tortilla':#condicional para tortilla
               calorias_g==2.37
        elif tipo_a=='carne':#condicional para carne
            print('¿Qué carne ingeriste? ')
            t_alim=input('pollo/res/cerdo/jamon ')#variable que almacena el tipo de carne
            if t_alim=='pollo':#condicional para pollo
               calorias_g=2.39
            elif t_alim=='res':#condicional para res
               calorias_g==2.5
            elif t_alim=='cerdo':#condicional para cerdo
               calorias_g==2.42
            elif t_alim=='jamon':#condicional para jamón
               calorias_g==1.45
        elif tipo_a=='grasa':#condicional para grasa
            print('¿Qué grasa ingeriste? ')
            t_alim=input('aguacate/almendra/cacahuate/nuez ')#variable que almacena tipo de grasa
            if t_alim=='aguacate':#condicional para aguacate
               calorias_g=1.41
            elif t_alim=='almendra':#condicional para almendra
               calorias_g==5.76
            elif t_alim=='cacahuate':#condicional para cacahuate
               calorias_g==5.67
            elif t_alim=='nuez':#condicional para nuez
               calorias_g==6.54
        gramos=float(input('¿Cuantos gramos fueron? '))#var para que el usuario ingrese la cantidad consumida en gramos
        calorias_alim=calorias_g*gramos#multiplicación de las calorías/g por los gramos consumidos
        calorias_comida=calorias_comida+calorias_alim#suma para las calorias totales de la comida
        #se vuelve a requerir la variable alimento para continuar el ciclo o cerrarlo
        alimento=input('La comida contuvo otro alimento? si/no ')

    #condicional si la respuesta es no, se imprimen las calorias de la comida
    if alimento=='no':
        print('Las calorias de la comida son '+str(calorias_comida))

#Da al usuario la opción de elegir qué quiere saber
opcion=int(input('Ingresa \n 1 para saber tus calorias de mantenimiento \n 2 para conocer las calorías resultantes \n 3 para conocer la proteina que debes ingerir \n 4 para conocer las calorias de una comida '))

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

#Condicional para la opción 4
elif opcion==4:

    #Llama a la función 'comida'
    comida()