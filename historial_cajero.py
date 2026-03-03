print("---historial de cajero---")
print("1. depositos")
print("2. retiros")
print("que deseas ver?")
opcion = input("digite numero o nombre: ")
if opcion == "1" or opcion == "depositos":
    print("\n---depositos---")
    print("--$100.00 dia 03/mar/2026--\n--50.00 dia 28/feb/2026")
elif opcion =="2" or opcion == "retiros":
    print("\n---retiros---")
    print("--retiro de $80.00 dia 05/feb/2026--\n--retiro de $10.00 dia 01/mar/2026")
else:
    print("opcion no valida. intente de nuevo")