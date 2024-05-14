'''definir una funcion que tome tres numeros como argumento y devuelva el mayor de ellos tres'''

def max__de__tres(x,y,z):
    if x>y>z:
        return x
    elif y>x>z:
        return y
    else:
        return z
    

print(max__de__tres(3,2,1))
