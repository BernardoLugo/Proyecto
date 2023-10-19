# Contador y regulador de calorías
## Contexto: 
En México, un 74.1% de la población adulta tiene sobrepeso.
El sobrepeso en nuestro país se debe en gran parte a la mala alimentación.
Creo que programar un contador y regulador de calorías puede ser una buena
herramienta para las personas que quieran hacer un cambio en su dieta.

El objetivo de este programa es ser un contador de calorías. 
Según los alimentos y cantidades que ingrese el usuario, el programa calculará
la cantidad de calorías que se han consumido. Al anteriormente ingresar una meta diaria 
de calorías, el programa avisará cuando no se cumpla dicha meta, además de 
que dará alternativas alimentarias para el usuario.

## Primer avance
En este primer avance se muestran los cálculos que se van a utilizar
para lograr el objetivo del programa.

## Segundo avance
En este segundo avance se agregaron dos funciones que contienen los cálculos
del primer avance, además de algunos condicionales. Se agregó también la 
opción de que el usuario llame a las dos funciones dependiendo de la 
información que quiera saber. (contador_calorias_avance_3.py)

## Tercer avance
En el tercer avance se agregaron las funciones de 'actividad_fisica'
y 'objetivo_proteina', conteniendo 'actividad_fisica' condicionales.
(contador_calorias.py)

## Cuarto avance
Se agregó la función 'comida', que contiene un ciclo while. 
Esta función calcula las calorias de una comida según el alimento y los gramos
consumidos.

## Quinto avance
Se agregó la función 'sugerencia_comida', la cual usa listas para generar una
recomendación de comida. 

## Entrega final
Se creó la lista 'alimentos' la cual contiene listas de diferentes tipos de alimentos.
Se eliminaron las funciones de 'comida' y 'sugerencia de comida'. En su lugar, 
se agregaron las siguientes funciones: 'recomendacion', 'limpia_cadena'y 'comida'. 
Estas 3 funciones trabajan juntas; la función 'recomendacion' se usa en la función 'comida' 
para generar una variable que abra el ciclo en esta última función. La función 'comida' también 
manda a llamar a la función 'limpia cadena'. Finalmente, la función 'comida' 
da una recomendación de comida usando las listas creadas en esta entrega.
También se creó la función 'main', la cual contiene el menú para elegir las opciones 
del programa, utilizando un ciclo para que el programa corra hasta que el usuario desee lo contrario.

# API
Durante el proyecto se utilizó una librería de python: Random

## Implementación de Random en el código
Se utilizó 'random.choice' en la función 'comida', sirviendo esta función de la librería Random para 
tomar elementos de una manera casi aleatoria de las listas creadas.

# Correcciones
Sub-Competencia: 
El proyecto no contiene código que no se usa en comentarios, ni archivos extra en el repositorio (Revisón y Final)

Error original: 
Archivo extra con nombre 'contador_calorias_avance_3'.

Cambio realizado:
Se eliminó del repositorio.

=============================
Sub-Competencia: 
Usa herramientas de control de veriosnes, de tal forma que se puedan observar los avances en los commits (Revisión y Final)

Error original: 
No se había realizado la entrega

Cambio realizado: 
No hubo cambios

=============================
Sub-Competencia: 
Incorpora y explica nuevas funciones en su progra e incluya su referencias al API de pythoon. (Revisión y Final)

Error original:
No hubo entrega

Cambio realizado:
Se eactualizó el readme con el API. Se agregaron 4 funciones nuevas.

Líneas de código donde se ve la corrección: Líneas 107-230

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

==================================================================
