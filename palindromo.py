var = 1
while var < 6:
    palabraNormal = input("Introduce la palabra  : " + str(var))
    palabraInvertida = palabraNormal[::-1]

    if(palabraNormal == palabraInvertida):
        print("La palabra es igual al derecho y al revez.")
        var = var + 1
    else:
        print("Esto no es un Palindromo.")
        var = var + 1