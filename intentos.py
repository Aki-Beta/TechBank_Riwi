from autenticacion import autenticacion
def validacion():
     i = 0
     while i <= 2:
      i = autenticacion(i)

     if i == 3:
          print(" usuario bloqueado")
          exit()
     elif i == 4:
          print("Acceso concedido")
          continuar = True
          return continuar