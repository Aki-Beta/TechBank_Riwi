
print("BIENVENIDO") 


saldo = 1000 
print("¿CUÁNTAS OPERACIONES DESEA REALIZAR?: ")
operaciones = pedirNumero()


historial = []

for i in range(operaciones):
    mostrarmenu()
    print("DIGITE EL NUMERO DE LA OPERACION: ")
    operacion = pedirNumero()
    if operacion == "1":
        saldo = consultar_saldo(saldo, historial)

    elif operacion == "2":
        saldo = depositar(saldo, historial)
    
    elif operacion == "3":
        saldo = retirar(saldo, historial)

    elif operacion =="4":
        mostrar_historial(historial)
    
    else:
        print("Opcion invalida")
