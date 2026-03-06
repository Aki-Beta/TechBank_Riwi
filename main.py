from auxiliares import *
from cajero_retiro import *
from logica_de_deposito import *
from historial_cajero import *
from configuracion import * 
from gestion_de_Saldo import *
from intentos import *
from validacion_numeros import pedirNumero
from ValidacionDeReglas import permiso
from menunuevo import menu_principal

historial = []

saldo = configuracion_inicial()

continuar = True
while continuar:

    opcion = menu_principal()

    if opcion == 1:
        print("Consultando saldo...")
        consultar_saldo(saldo,historial)

    elif opcion == 2:
        print("Ingrese el monto a retirar:")
        retiro= pedirNumero()
        numValido = permiso(1,retiro,saldo)
        if numValido:
            saldo = realizar_retiro(retiro,historial,saldo)

    elif opcion == 3:
        print("Ingrese el monto a depositar:")
        deposito= pedirNumero()
        numValido = permiso(deposito,1,saldo)
        if numValido:
            saldo = realizar_deposito(deposito,historial,saldo)
        
    elif opcion == 4:
        mostrar_historial(historial)
        
    elif opcion == 5:
        print("\n👋 ¡Gracias por usar TechBanck Riwi Digital!")
        continuar = False