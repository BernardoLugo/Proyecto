'''
Importación de la librería random
'''

import random

'''
Listas anidadas de alimentos
'''

#Lista de frutas
frutas=['sandia','melon','fresas','piña','manzana',
            'pera','arandanos','mango','tamarindo','uvas','platano',
            'naranja','mandarina','toronja','frambuesa']
#Lista de cereales
cereales=['avena','arroz','tortilla de maiz','tortilla de harina',
        'pan de caja','galletas maría','amaranto','quinoa']
#Lista de carnes
carnes=['bistec de res','jamon','chuleta','pollo',
        'costilla','atun','salmon','camaron','pulpo',
        'huevo','chorizo']
#Lista de grasas
grasas=['pistaches','almendra','cacahuate','avellana',
        'nueces', 'aguacate', 'queso',]

#Lista anidada de alimentos
alimentos=[frutas,cereales,carnes,grasas]


'''
Creación de funciones
'''

#Función para calcular calorias de mantenimiento
def calorias_de_mantenimiento(sexo,edad,peso,estatura):

    #Crea la variable de calorias de mantenimiento
    c_mantenimiento=0.0

    #Decide que variante de la formula de Harris-Benedict usar segun el sexo
    if sexo=='h': #Condicional para sexo masculino
        c_mantenimiento=(10.0*peso)
        c_mantenimiento=c_mantenimiento+(6.25*estatura)
        c_mantenimiento=c_mantenimiento-(5.0*edad)
        c_mantenimiento=c_mantenimiento+5.0
    
        #Devuelve el valor de calorias de mantenimiento
        return c_mantenimiento

    elif sexo=='m': #Condicional para sexo femenino
        c_mantenimiento=(10.0*peso)
        c_mantenimiento=c_mantenimiento+(6.25*estatura)
        c_mantenimiento=c_mantenimiento-(5.0*edad)
        c_mantenimiento=c_mantenimiento-161.0

        #Devuelve el valor de las calorias de mantenimiento
        return c_mantenimiento


#Función para calcular calorias resultantes
def calorias_resultantes(c_consumidas,sexo,edad,peso,estatura):

    #Crea la variable de calorias resultantes
    c_resultantes=0.0

    #Llama a la función de 'calorias de mantenimiento' para crear 
    #la variable de 'mantenimiento'
    mantenimiento=calorias_de_mantenimiento(sexo,edad,peso,estatura)

    #Decide si faltan o sobran calorias
    if c_consumidas<mantenimiento: #Condicional si faltan calorias
        c_resultantes=mantenimiento-c_consumidas

        #Imprime las calorias que faltan
        print('Faltan '+str(c_resultantes)+' calorias')

    elif c_consumidas>mantenimiento:#Condicional si sobran calorias
        c_resultantes=c_consumidas-mantenimiento

        #Imprime las calorias sobrantes
        print('Te has pasado por '+str(c_resultantes)+' calorias')

#Función que calcula proteina segun la actividad fisica
def proteina_actividad_fisica(actividad):
    if actividad == 1:#Condicional para opción 1
        proteina=2.0
    elif actividad == 2:#Condicional para opción 2
        proteina=1.5
    elif actividad == 3:#Condicional para opción 3
        proteina=1.0

    #Regresa el valor de proteina segun la actividad fisica del usuario 
    return proteina

#Función que da las calorías que debe de comer el usuario según su peso
def objetivo_proteina(peso,actividad):

    #Llama a la función de actividad_fisica
    proteina=proteina_actividad_fisica(actividad)
    #Multiplica el peso por lo que regresa la función anterior
    proteina_necesaria=proteina*peso

    #Imprime los gramos de proteina que debe de consumir el usuario
    print('Los gramos de proteina que debes consumir son '+str(proteina_necesaria))

#Función que pregunta al usuario si quiere una recomendación
def recomendacion():

    #Crea la variable respuesta a través de un input
    respuesta=input('Quieres una recomendacion de comida? si/no ')
    if respuesta=='si':#Condicional si respuesta es 'si'
        return True#Regresa el valor True
    elif respuesta == 'no':#Condicional si la respuesta es 'no'
        return False#Regresa el valor False

#Función que limpia cadenas
def limpia_cadena(cadena):

    #Se eliminan '[]' y comillas
    cadena_n1=cadena.replace("[",'')
    cadena_n2=cadena_n1.replace("]",'')
    cadena_n3=cadena_n2.replace("'",'')

    #Regresa la cadena limpia
    return cadena_n3

#Función que da recomendaciones de comida    
def comida():

    #Llama a la función 'recomendacion'
    res=recomendacion()

    comida=[]#Crea la lista 'comida'

    #Ciclo que se cumple mientras 'res' sea True
    while res==True:

        #Ciclo que recorre los elemento en la lista 'alimentos'
        for i in alimentos:
            #Escoge un elemento aleatorio de las listas anidadas
            alimento=random.choice(i)
            #Agrega el elemento anterior a la lista 'comida'
            comida.append(alimento)

        comida_s=str(comida)#Convierte la lista a string
        comida_n=limpia_cadena(comida_s)#Llama a la función 'limpia_cadena'

        #Imprime la recomendación de comida
        print('Prueba una comida con ',comida_n,' !')
      
        comida=[]#Vacía la lista 'comida'

        #Vuelve a llamar a la funcion 'recomendacion'
        res=recomendacion()
    
    #Condicional para cuando 'res' es False
    if res==False:
        print('Provecho!')

#Funcion que pregunta si se quiere elegir otra opcion
def respuesta_opcion():

    #Crea la variable respuesta a través de un input
    respuesta=input('Quieres elegir otra opcion inicial? si/no ')
    if respuesta=='si':#Condicional si respuesta es 'si'
        return True#Regresa el valor True
    elif respuesta == 'no':#Condicional si la respuesta es 'no'
        return False#Regresa el valor False



def main():
    res=True
    while res==True:
        #Crea la variable opcion para comenzar un menu de opciones
        opcion=(input('Ingresa \n 1 para saber tus calorias ' 
                        'de mantenimiento \n 2 para conocer las calorías ' 
                        'resultantes \n 3 para conocer la proteina que '
                        'debes ingerir \n 4 para obtener recomendaciones de comida '))
        opcion=int(opcion)

        #Condicional para la opción 1
        if opcion==1:
            #Pide las variables de sexo, edad, peso y estatura al usuario
            sexo=(input('Ingresa tu sexo como h para hombre y m para mujer. '))
            edad=float(input('Ingresa tu edad en años. '))
            peso=float(input('Ingresa tu peso en kg. '))
            estatura=float(input('Ingresa tu estatura en cm. '))

            #Llama a la función de 'calorias_de_mantenimiento'
            print('Tus calorias de mantenimiento son',
                  calorias_de_mantenimiento(sexo,edad,peso,estatura))

        #Condicional para la opción 2
        elif opcion==2:

            #Pide ingresar las calorias consumidas hasta el momento
            c_consumidas=float(input('Ingresa la cantidad de calorias'
                                    ' ingeridas hasta el momento. '))

            #Pide las variables de sexo, edad, peso y estatura al usuario
            sexo=(input('Ingresa tu sexo como h para hombre y m para mujer. '))
            edad=float(input('Ingresa tu edad en años. '))
            peso=float(input('Ingresa tu peso en kg. '))
            estatura=float(input('Ingresa tu estatura en cm. '))

            #Llama a la función de 'resultado'
            calorias_resultantes(c_consumidas,sexo,edad,peso,estatura)

        #Condicional para la opción 3
        elif opcion==3:

            #Pide ingresar el peso
            peso=float(input('Ingresa tu peso en kg '))

            #Pide ingresar un valor correspondiente a la actividad física
            print('Entrenamiento de fuerza: 1  Entrenamiento aeróbico: 2  Sin entrenamiento: 3')
            actividad=int(input('Ingresa el numero correspondiente a tu actividad fisica '))

            objetivo_proteina(peso,actividad)

        #Condicional para la opción 4
        elif opcion==4:

            #Llama a la función 'comida'
            comida()
        res=respuesta_opcion()
    if res==False:
        print('Gracias por usar el programa!')
main()    