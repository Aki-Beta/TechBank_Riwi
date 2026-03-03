from validacion_numeros import pedirNumero
saldo = 1000
opcion = input()
if opcion == "2":
    retiro = pedirNumero()
    if 0 < retiro <= saldo:
        saldo -= retiro
        print(f"Retiro exitoso. Nuevo saldo: {saldo}")
    else:
        print("Fondos insuficientes o monto no válido.")
