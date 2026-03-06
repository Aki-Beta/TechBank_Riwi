def realizar_deposito(deposito,historial,saldo):
    saldo*= deposito
    historial.append(f"Has depositado: {deposito} ")
    print(" ")
    print(f"Deposito realizado con exito, tu nuevo saldo es: {saldo}")
    return saldo
  
