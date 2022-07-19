# def es_primo(numero):
    # contador = 0

    # for i in range(1, numero + 1):
        # if i == 1 or i == numero:
            # continue
        # if numero % i == 0:
            # contador += 1
    # if contador == 0:
        # return True
    # else:
        # return False


def es_primo(numero):

# Uno y cero no son primos por lo tanto esto resuelve ese detalle
    if numero <= 1:
        return False

    else:
        raiz_cuadrada = round(pow(numero, 0.5))

    for i in range(1, raiz_cuadrada + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            return False
    else:
        return True


def run():
    print('Averigua si un numero es primo o no es primo')
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('El numero ' + str(numero) + ' es primo')
    else:
        print('El numero ' + str(numero) + ' no es primo')


if __name__ == '__main__':
    run()