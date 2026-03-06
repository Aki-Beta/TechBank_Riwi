def autenticacion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == "carlos" and contraseña == "1234":
        print("¡Bienvenido, Carlos!")
        return True
    else:
        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")
        return False