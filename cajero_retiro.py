def realizar_retiro(retiro,historial,saldo):
    saldo -= retiro
    historial.append(f'Ha retirado {retiro}')
    print('')
    print(f'Retiro exitoso. Nuevo saldo: ${saldo}')
    return saldo
