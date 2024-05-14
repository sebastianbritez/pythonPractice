'''definir una funcion que tome un caracter y devuelva true si dicho caracter es una vocal'''


def vocales(n):
    lista__vocales= ['a', 'e', 'i', 'o', 'u']

    if n  in lista__vocales:
        return True
    else:
        return False

print(vocales('a'))