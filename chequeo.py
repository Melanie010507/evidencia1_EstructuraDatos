import datetime

contactos = dict()
salasActivas = dict()
claveCliente = 1
claveSala = 1
reservaciones = dict()
numeroFolio = 1

while True:
    print("\n \t---Menu---\t")
    print("1. Registrar contacto")
    print("2. Registrar Sala")
    print("3. Registrar reservacion") 
    print("4. Modificar nombre de la reservacion")
    print("5. Consultar reservaciones")
    print("6. Salir del menu")
    opcion = input("Elige una opcion (1-6):")



    if opcion == "1":
        """Funcion que registra los datos del cliente"""
        while True:
            apellido = input("\nApellido(s): ")
            nombre = input("Nombre(s): ") 
            if not (apellido.replace (" ", "").isalpha() and nombre.replace(" ", "").isalpha()):
                print("Error al agregar cliente, solo se permiten letras. Introduzca nuevamente.")
                continue
            contactos[claveCliente] = (apellido, nombre)
            print("cliente registrado exitosamente.")
            print(f"Clave del cliente: {claveCliente}")
            claveCliente += 1
            continuar = input("Ingrese [s] para registrar otro cliente, o cualquier otra tecla para finalizar: "
            "\n").lower()
            if continuar != "s":
                    break



    elif opcion == "2":
        """Opcion que registra los datos del sala"""
        while True:
            salaNombre = input("\nEscribe el nombre de la sala: ")
            cupo = input("Capacidad de la sala (especificar con numeros): ")
            if not (salaNombre.replace (" ", "") and cupo.replace(" ", "").isdigit()):
                print("Error al agregar sala, el nombre no puede estar vacio y el cupo debe ser numerico.")
                continue
            codigoSala = f"S{claveSala:02d}"
            salasActivas[codigoSala] = (salaNombre, cupo)
            print("Sala registrada exitosamente.")
            print(f"Clave de la sala: {codigoSala}")
            claveSala += 1
            continuar = input("Ingrese [s] para registrar otro cliente, o cualquier otra tecla para finalizar: "
            "\n").lower()
            if continuar != "s":
                    break   




    elif opcion == "3":
        """Opcion que registra reservacion"""
        while True: #Aqui agregamos un bucle para que pueda ver las opciones y si pone una incorrecta no se vaya al menu principal
            print("\nSeleccion cliente para tu reservacion:")
            print("CLAVE\tNOMBRE\tAPELLIDO")
            for clave, (apellido, nombre) in sorted(contactos.items()): #sorted es para ordenar los contactos alfabeticamente
                print(f"{clave}. \t{apellido} \t{nombre}")
            try: 
                claveCliente = int(input("Ingresa la clave del cliente: "))
                if claveCliente not in contactos:
                    print("Cliente no encontrado.")
                    respuesta = input("Deseas cancelar la operacion? presiona [s] para si o " \
                    "cualquier otra tecla para no: " ).lower()
                    if respuesta == "s":
                        break  # Salir al menú principal para registrar un nuevo cliente
                    continue
                print("Selecciona la sala para tu reservacion:")
                print("CLAVE\tNOMBRE\tCUPO")
                for codigo, (salaNombre, cupo) in salasActivas.items():
                    print(f"{codigo}. \t{salaNombre} \t(Cupo: {cupo})")
                
                codigoSala = input("Ingresa la clave de la sala: ")
                if codigoSala not in salasActivas:
                    print("Sala no encontrada.")
                    continue
                fecha_str = input("Ingresa la fecha de la reservacion con 2 dias de anticipacion a la fecha de hoy (YYYY-MM-DD): ")
                try:
                    fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
                    fecha_actual = datetime.date.today()
                    diferencia = (fecha - fecha_actual).days
                    if diferencia < 2:
                        print("La fecha debe tener al menos 2 días de anticipación respecto a hoy.")
                        continue
                except ValueError:
                    print("Formato de fecha incorrecto.")
                    continue

                # Revisar si el turno ya está ocupado para la sala y fecha
                turno = input("Ingresa el turno (Matutino/Vespertino/Nocturno): ").lower()
                if turno == "matutino":
                    hora = datetime.time(9, 0)
                elif turno == "vespertino":
                    hora = datetime.time(15, 0)
                elif turno == "nocturno":
                    hora = datetime.time(19, 0)
                else:
                    print("Turno no válido.")
                    continue

                ocupado = False
                for id_res, (cliente_res, sala_res, fecha_res, turno_res, _) in reservaciones.items():
                    if sala_res == codigoSala and fecha_res == fecha and turno_res == turno:
                        ocupado = True
                        break
                if ocupado:
                    print("Ese turno ya está reservado para esta sala en esa fecha.")
                    continue

                while True: 
                    NombreReservacion = input("Como se llama el Evento: ").strip()
                    if not NombreReservacion:
                        print("El nombre del evento no puede estar vacio.")
                    else:
                        break
                reservacion_id = len(reservaciones) + 1
                reservaciones[reservacion_id] = (claveCliente, codigoSala, fecha, turno, NombreReservacion )
                print(f"Id de la reservacion: {reservacion_id}")
                print("Reservacion registrada exitosamente.")
                break            
            except ValueError:
                print("Entrada invalida. Intenta de nuevo.")
                continue
    
    elif opcion == "4":
        """Opcion que modifica el nombre de la reservacion"""

        print("\nReservaciones actuales:")
        print("Id\t\tCliente\t\tSala\t\tFecha\t\tturno\t\tEvento")
        for reservacion_id, (claveCliente, codigoSala, fecha, turno, NombreReservacion) in reservaciones.items():
            print(f"{reservacion_id} \t\t{claveCliente} \t{codigoSala} \t{fecha} \t{turno} \t\t{NombreReservacion}")
        FolioACambiar = input("Ingresa el id de la reservacion: ")
        try:
            FolioACambiar = int(FolioACambiar)
        except ValueError:
            print("Id de reservacion invalido.")
            continue
        if FolioACambiar not in reservaciones:
            print("Reservacion no encontrada")
        else:
            claveCliente, codigoSala, fecha, turno, NombreReservacion = reservaciones[FolioACambiar]
            print(f"Nombre actual del evento: {NombreReservacion}")
            nuevo_nombre = input("Ingresa el nuevo nombre del evento: ")
            if nuevo_nombre:
                reservaciones[reservacion_id] = (claveCliente, codigoSala, fecha, turno, nuevo_nombre)               
            print("Nombre del evento actualizado exitosamente.")
            print(f"{reservacion_id} \t\t{claveCliente} \t{codigoSala} t{fecha} \t{turno} \t\t{nuevo_nombre}")

    elif opcion == "5":
        while True:
            fecha_str = input("\nIngresa la fecha para el reporte (YYYY-MM-DD): ")
            try:
                fecha_reporte = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
            except ValueError:
                print("Formato de fecha incorrecto.")
                continue

            # Filtrar reservaciones por la fecha solicitada
            reservas_filtradas = [(reservacion_id, claveCliente, codigoSala, fecha, hora, NombreReservacion)
                for reservacion_id, (claveCliente, codigoSala, fecha, hora, NombreReservacion ) in reservaciones.items()
                    if fecha == fecha_reporte]

            if not reservas_filtradas:
                print("No hay reservaciones para esta fecha.")
            else:
                print("*"*95)
                print("**" "\t\tREPORTE DE RESERVACIONES PARA EL DÍA", fecha_str,  "\t\t**""")
                print("**SALA\t\tCLIENTE\t\t\tEVENTO\t\t\t\tTURNO**")
                print("*"*95)

                for reservacion_id, claveCliente, codigoSala, fecha, hora, NombreReservacion in reservas_filtradas:
                    cliente = contactos.get(claveCliente, "Cliente no encontrado.")
                    sala = salasActivas.get(codigoSala, "Sala no encontrada.")
                    evento = f"{NombreReservacion}"  
                    turno = "Matutino" if hora == datetime.time(9, 0) else "Vespertino" if hora == datetime.time(15, 0) else "Nocturno"

                    print(f"{codigoSala}\t\t{cliente[0]} {cliente[1]}\t\t{evento}\t\t\t\t{turno}")

                print(("*" * 40) + "FIN DEL REPORTE" + ("*" * 40))

                break

    elif opcion == "6":
        print("Saliendo del menu...")
        break
    else:
        print("Opcion no valida, intenta de nuevo")


