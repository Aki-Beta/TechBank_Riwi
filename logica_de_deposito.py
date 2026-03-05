def deposito(saldo, historial):
    while True:
        try:
            valor = float(input("Ingrese el monto a depositar: "))
            if valor <= 0:
                print("El monto debe ser mayor a cero. Intente nuevamente.")
            else:
                saldo += valor
                historial.append(f"Depósito: +${valor:.2f}")
                print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                return saldo, historial
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


saldo = 1000
historial = []

saldo, historial = deposito(saldo, historial)
