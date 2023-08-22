# Desafio Caracter Repetido
# Encontrar el primer caracter no repetido en un string.
# Pautas de evaluacion:
# +No utilizar ciclos for o while anidados (obligatorio)
# +Unicamente se puede utilizar la funcion input(), la funcion print() y la funcion len() (obligatorio)
# +Que el programa finalice sin errores (obligatorio)
# Ejemplo:
# Ingrese una cadena: abbcssadd
# La primera letra que no se repite es: c

def primer_catacter_no_repetido(cadenaCaracteres, index=0):
    if (index>=len(cadenaCaracteres)):
        return None
    else:
        caracter=cadenaCaracteres[index]
        if cadenaCaracteres.count(caracter) == 1:
            return caracter
        return primer_catacter_no_repetido(cadenaCaracteres, index + 1)

frase=input("Ingrese una cadena:\n")

resultado=primer_catacter_no_repetido(frase)
if (resultado==None):
    print("No hay letras que no se repitan.")
else:
    print("La primera letra que no se repite es:", resultado)

