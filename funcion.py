git push -u origin mainimport numpy as np 
AN = 78900
AV = 240000

def comprarAsiento(listaAsientos):
    print("Tarifas: ")
    print(f"Asiento Normal 1 al 30: ${AN}")
    print(f"Asiento VIP 31 al 42: ${AV}")
    asiento = int(input("Seleccione su asiento: "))
    while asiento < 1 or asiento > 42:
        print("Asiento no existente. Seleccione otro asiento:")
        asiento=int(input())
    print("Asiento reservado")
    reserva = np.where(listaAsientos == asiento)
    listaAsientos[reserva] = 'X'
    return asiento, reserva

def validarDatos():
    nom=input("Ingrese su nombre: ")
    rut=int(input("Ingrese su rut sin puntos ni guión, si su rut termina en K reemplazar por un 0: "))
    while rut < 50000000 or rut > 300000000:
        print("Rut no válido. Vuelva a ingresar su rut: ")
        rut=int(input())
    telefono=int(input("Ingrese su teléfono (formato 9 dígitos sin +56): "))
    while telefono < 199999999 or telefono > 999999999:
        print("Teléfono ingresado no válido. Vuelva a ingresar su teléfono (formato 9 dígitos sin +56): ")
        telefono=int(input())
    print("Ingrese su banco: ")
    print("1. Banco Santander")
    print("2. Banco Falabella")
    print("3. Banco Duoc")
    print("4. Otro banco")
    banco=int(input())
    while banco < 1 or banco > 4:
        print("Banco seleccionado no válido. Vuelva a ingresar su banco: ")
        banco=int(input())
    return np.array([nom, rut, telefono, banco],dtype=object)

def dsctoDuoc(precio,dscto):
    precio=precio-(precio*(dscto/100))
    return precio

def anularVuelo(reservaVuelo,listaAsientos):
    opAnul=input(f"El asiento que usted tiene reservado es el {reservaVuelo[0]}. ¿Desea anular su reserva? (y/n): ")
    while opAnul != 'y' and opAnul != 'n':
        print("Opción no válida. Vuelva a intentarlo.")
        opAnul=input(f"¿Desea anular la reserva de su asiento {reservaVuelo[0]}? (y/n): ")
    if opAnul == 'y':
        listaAsientos[reservaVuelo[1]]=reservaVuelo[0]
        
    else:
        pass

def verAsientos(listaAsientos):
    print("Asientos con X ya se encuentran reservados.")
    print(listaAsientos)
    print("Seleccione la acción que desee realizar:")
    print("1. Comprar asiento")
    print("2. Volver al menú")
    def modificarPasajero(datos, reservaVuelo):
    rutPasajero = int(input("Ingrese el rut del pasajero que desea modificar: "))
    asientoPasajero = int(input("Ingrese el asiento del pasajero que desea modificar: "))
    print(type(datos[1]))
    print(type(rutPasajero))
    if rutPasajero == datos[1] and asientoPasajero == reservaVuelo[0]:
        print("Pasajero válido.")
        print("¿Qué dato desea modificar?")
        print("1. Nombre del pasajero")
        print("2. Teléfono del pasajero")
        print("3. Cancelar acción")
        opMod = int(input())
        while opMod < 1 or opMod > 3:
            print("Opción no válida. Vuelva a ingresar una opción: ")
            opMod=int(input())
        if opMod == 1:
            print(f"Nombre del pasajero: {datos[0]}")
            nomPasajero=input("Ingrese nuevo nombre: ")
            datos[0] = nomPasajero
            print("Nombre de pasajero actualizado. Regresando al menú.")
        elif opMod == 2:
            print(f"Teléfono del pasajero: {datos[2]}")
            telPasajero=int(input("Ingrese nuevo teléfono (formato 9 dígitos sin +56): "))
            while telPasajero < 199999999 or telPasajero > 999999999:
                print("Teléfono ingresado no válido. Vuelva a ingresar su teléfono (formato 9 dígitos sin +56): ")
                telPasajero=int(input())
            datos[2] = telPasajero
            print("Teléfono de pasajero actualizado. Regresando al menú.")
        else:
            print("Regresando al menú")
    else:
        print("Datos ingresados no corresponden a ningún pasajero. Regresando al menú.")