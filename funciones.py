## Forma de ejecutar algo varias veces sin funciones

# print('Mensaje especial: ')
# print('Estoy aprendiendo a usar funciones!')
# print('Mensaje especial: ')
# print('Estoy aprendiendo a usar funciones!')
# print('Mensaje especial: ')
# print('Estoy aprendiendo a usar funciones!')


## Forma de ejecutar algo varias veces con funciones

# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


## Forma de ejecutar algo varias veces

    ##Sin funciones y parametros

# opcion = int(input('Elige una opción (1 , 2 , 3): '))
# if opcion == 1:
#     print('Hola')
#     print('Cómo estas')
#     print('Elegiste la opción 1')
#     print('Adios')
# elif opcion == 2:
#     print('Hola')
#     print('Cómo estas')
#     print('Elegiste la opción 2')
#     print('Adios')
# elif opcion == 3:
#     print('Hola')
#     print('Cómo estas')
#     print('Elegiste la opción 3')
#     print('Adios')
# else:
#     print('Escribe la opción correcta')

    ##Con funciones y parametros

# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estas')
#     print(mensaje)
#     print('Adios')

# opcion = int(input('Elige una opción (1 , 2 , 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1')
# elif opcion == 2:
#     conversacion('Elegiste la opción 2')
# elif opcion == 3:
#     conversacion('Elegiste la opción 3')
# else:
#     print('Escribe la opción correcta')


## Guardar resultado de una función en una variable
def suma(a, b):
    print('Se suman dos numeros')
    resultado = a + b
    return resultado

sumatoria = suma(1, 4)
print(sumatoria)