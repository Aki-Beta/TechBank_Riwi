limite_diario = 20000

def limite_retiro (monto_retiro, tope_diario):
    if total_retirado + monto_retiro <= tope_diario:
        print("El monto excede el límite diario permitido para retiros")
        return False
    else: 
        print ("Retiro permitido")
        return True
    

