# Interrumpiendo ciclos

from operator import le

from pyparsing import line


def run():

# Interrumpiendo ciclos con

    ## Con continue

    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    ## Con break

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)


# Reto de la clase de ciclos con break y continue

    ## Este ciclo while permite escribir varias lineas
        ## mientras estas no superen los 50 carateres

    while True:
        linea = input('Escribe una frase \U0001f58b\uFE0F: ')
        num_caracter = len(linea)
        if num_caracter >= 50:
            break
        print(linea)
    print('¡Terminado! Superaste los 50 caracteres \U0001f523')

if __name__ == '__main__':
    run()