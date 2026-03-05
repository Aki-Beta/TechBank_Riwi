def realizar_deposito(deposito,historial,saldo):
    saldo*= deposito
    historial.append(f"saldo: {saldo}")
    print(" ")
    print(f"Deposito realizado con exito, tu nuevo saldo es: {saldo}")
    return saldo