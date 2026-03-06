from validacion_numeros import pedirNumero
def menu_menuprincipal():
    print("")
    print("Elija una opción")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Mostrar historial")
    print("5. Salir")
    opcion = pedirNumero()
    return opcion