#Mi funcion

def pedirNumero ():
    try:
        numero = float(input())
        return numero
    except ValueError:
        print("Por favor, ingrese un número válido.")
        numero = 0
        return numero