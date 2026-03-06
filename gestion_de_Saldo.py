def consultar_saldo(saldo, historial):
    historial.append(f"Has consultado tu saldo: {saldo}")
    print(f"Tu saldo actual es: {saldo}")
    return saldo 
