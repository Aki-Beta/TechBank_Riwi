intentos = 3 
while intentos> 0:
    usuario = input("introduce el usuario ")
    password = input("introduce la contraseña ")

    if usuario == "tyler" and password == "user1234":
        print("has entrado al sistema")
        break
    else:
        intentos -=1
        print (f"incorrecto. te queda {intentos} intentos. \n")
    if intentos == 0:
        print ("cuenta bloqueada")

