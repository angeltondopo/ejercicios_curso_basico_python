def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

# Devuelve el valor del diccionario
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

# Devuelve el valor del diccionario
    # print(poblacion_paises['Argentina'])

# El metodo keys devuelve la llave del diccionario
    # for pais in poblacion_paises.keys():
        # print(pais)

# El metodo values devuelve el valor del diccionario
    # for pais in poblacion_paises.values():
        # print(pais)

# El metodo items devuelve la llave y el valor del diccionario
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()