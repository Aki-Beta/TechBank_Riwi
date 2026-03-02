def pedirNumero ():
    try:
        monto = int(input())
        return monto
    except ValueError:
        print("Por favor, ingrese un número válido.")
        retirar_saldo()
        monto = 0
        return monto




saldo_inicial = 1000
def retirar_saldo ():

    monto = pedirNumero()

    if monto <= 1000 and monto > 0:
        retiro = saldo_inicial - monto
        print("""
Haz retirado """,monto,""" de tu cuenta 
                """)
        print("Han quedado en tu cuenta: ",retiro)
    elif monto > 1000 :
        print("""
Saldo insuficiente
                """)
        print("Coloque un monto a retirar")
        monto = 0
        retirar_saldo()
    elif monto < 0 or monto == 0:
        print("""
Coloque un valor valido""")
        monto = 0
        retirar_saldo()

retirar_saldo()