
def autenticacion(i):
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
   
    if usuario == "carlos" and contraseña == "1234":
        print("¡Bienvenido, Carlos!")
        i = 4
        return i
    else:
        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")
        i += 1
      
        return i
 