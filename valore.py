import numpy as np
import funciones as fn
AN = 78900
AV = 240000
initFlag = True
listaAsientos = np.arange(1,43,1, dtype=object)
listaAsientos = listaAsientos.reshape(7,6)
listaAsientos = np.insert(listaAsientos, (5,5), '_', axis=0)
listaAsientos = np.insert(listaAsientos, (3,3), '', axis=1)
listaAsientos = np.insert(listaAsientos, (0,8), '|', axis=1)

print("-"*30)
print("   Bienvenide a Vuelos Duoc")
print("-"*30)
while initFlag == True:
    try:
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular vuelo")
        print("4. Modificar datos de pasajero")
        print("5. Salir")
        opmenu = int(input("Seleccione la acción a realizar: "))

        while opmenu < 1 or opmenu > 5:
            print("Opción seleccionada no válida")
            opmenu = int(input("Vuelva a ingresar una opción: "))

        if opmenu == 1:
            fn.verAsientos(listaAsientos)
            opVer = int(input(""))
            if opVer == 1:
                reservaVuelo = fn.comprarAsiento(listaAsientos)
                if reservaVuelo[0] >= 1 and reservaVuelo[0]<31:
                    precio=AN
                else:
                    precio=AV
                datos = fn.validarDatos()
                if datos[3] == 3:
                    precioFinal = fn.dsctoDuoc(precio,15)
                else:
                    precioFinal = precio
                print(f"Sub total: ${precio}")
                print(f"Dscto Banco Duoc: 15%")
                print(f"Total a pagar: ${precioFinal}")
            if opVer == 2:
                initFlag == True

        if opmenu == 2:
            print("Asientos con X ya se encuentran reservados.")
            print(listaAsientos)
            reservaVuelo = fn.comprarAsiento(listaAsientos)
            if reservaVuelo[0] >= 1 and reservaVuelo[0]<31:
                precio=AN
            else:
                precio=AV
            datos = fn.validarDatos()
            if datos[3] == 3:
                precioFinal = fn.dsctoDuoc(precio,15)
            else:
                precioFinal = precio
            print(f"Total a pagar: ${precioFinal}")

        if opmenu == 3:
            fn.anularVuelo(reservaVuelo,listaAsientos)

        if opmenu == 4:
            fn.modificarPasajero(datos,reservaVuelo)

        if opmenu == 5:
            initFlag == False
            break
    except:
        print("Error de datos. Regresando al menú principal.")