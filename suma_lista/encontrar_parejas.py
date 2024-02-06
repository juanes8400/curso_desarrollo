def encontrar_parejas(lista, numero_objetivo):
    numeros_vistos = {}
    parejas = []

    for i, numero in enumerate(lista):
        complemento = numero_objetivo - numero
        if complemento in numeros_vistos and numeros_vistos[complemento] is not None:
            parejas.append((complemento, numero))
            numeros_vistos[complemento] = None
            numeros_vistos[numero] = None
        else:
            if numero not in numeros_vistos or numeros_vistos[numero] is not None:
                numeros_vistos[numero] = i

    return parejas

if __name__ == "__main__":
    import sys

    # Convertir la entrada del usuario en una lista de números
    lista_entrada = input("Ingrese la lista de números separados por coma: ")
    lista = list(map(int, lista_entrada.split(',')))
    
    numero_objetivo = int(input("Ingrese el número objetivo: "))

    parejas = encontrar_parejas(lista, numero_objetivo)
    print(f"Parejas encontradas: {parejas}")
