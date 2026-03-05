def consultar_saldo(saldo, historial):
    historial.append(f"Saldo: +{saldo}")
    print(f"Tu saldo actual es: {saldo}")
    return saldo 
