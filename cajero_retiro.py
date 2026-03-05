def realizar_retiro(retiro,historial,saldo):
    saldo -= retiro
    historial.append(f'Saldo: {saldo}')
    print('')
    print(f'Retiro exitoso. Nuevo saldo: ${saldo}')
    return saldo
