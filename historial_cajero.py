def mostrar_historial(historial):
    print("---historial de cajero---")
    if len(historial) == 0:
        print("historial vacio")
    for movimientos in range(historial):
        print(movimientos)
