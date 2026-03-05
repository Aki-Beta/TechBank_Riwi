def menu_principal():
    saldo= 1000
    saldo = get_saldo_actual()

    # BIENVENIDA
    print("🎉 === Bienvenido a TechBanck Riwi Digital ===")
    input("Presiona Enter para continuar...")

    # BUCLE PRINCIPAL
    continuar = True
    while continuar:
        opcion = menu_principal(saldo)
        
        if opcion == 1:
            # Función de compañero 1
            pass  # print(f"Saldo actual: ${saldo:.2f}")
            
        elif opcion == 2:
            # Función de compañero 2  
            pass  # retirar_dinero(saldo)
            
        elif opcion == 3:
            # Función de compañero 3
            pass  # depositar_dinero(saldo)
            
        elif opcion == 4:
            # Función de compañero 4
            pass  # mostrar_historial()
            
        elif opcion == 5:
            print("\n👋 ¡Gracias por usar TechBanck Riwi Digital!")
            continuar = False