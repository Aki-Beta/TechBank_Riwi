def validacion():
     intentos = []
     intentoscontra = []
     intentosfallidos = 0
     usuarioreal = "user"
     passwordreal = "1234"

     while len(intentos) <= 2:

          usuario = input("introduce el usuario ")
          password = input("introduce la contraseña ")

          if usuario != usuarioreal:

               intentos.append(usuario)
               intentosfallidos = +1

          if password != passwordreal:

               intentoscontra.append(usuario)
               print (" contraseña incorrecta")

          elif usuario == usuarioreal:

               intentos.append(usuario)
               if password == passwordreal:
                    print("Correcto")
               
     if intentosfallidos == 3:
          print(" usuario bloqueado")  
