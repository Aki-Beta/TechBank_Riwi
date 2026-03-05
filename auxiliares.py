
limite_diario = 20000

def limite_retiro (monto_retiro, tope_diario, total_retirado):
    if total_retirado + monto_retiro <= tope_diario:
        print("El monto excede el límite diario permitido para retiros")
        return False
    else: 
        print ("Retiro permitido")
        return True
    


def operaciones_exitosas(contador_operaciones, historial):
    contador_operaciones += 1
    historial.append("Operación exitosa")
    return contador_operaciones

def mostrar_historial(saldo, contador_operaciones, historial):
    print(f"Operaciones exitosas: {contador_operaciones}")
    print("Historial de operaciones:")
    print (f"Saldo final: {saldo}")
    for operacion in historial:
        print(operacion)
