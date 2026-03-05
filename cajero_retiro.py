def realizar_retiro(retiro,historial):
    historial.append(f"Saldo: {retiro}")
    saldo -= retiro
    print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
    return saldo
    
