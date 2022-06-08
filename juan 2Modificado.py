import os
from pickle import FALSE

sw  = 0

num = 0


lista     = []
lista2 = []
suscripcion = []

ingreso_opciones_menu1 = 0
errorIngresoSTR = "INGRESE SOLO NUMEROS"
errorIngreso123 = "escoja la opcion de 1 al 4"

rutTexto = 0
rut = 0
valida_rut = False
nombre = 0
direccion = 0
comuna = 0
correo = 0
edad_texto = 0
edad = 0
genero = 0
celu_texto = 0
celu = 0
tipo_cuenta = 0
fecha_suscripcion = 0
contador = 0
suscrito = False
existe_usuario = False
contador2 = 0


caracteresPermitidosRut = ["0'","1","2","3","4","5","6","7","8","9",]

menu1 = ['Juan Maestro APP','    (1) Registrar Cliente','    (2) Suscripción', '    (3) Consultar Datos Cliente','    (4) Salir']

while sw == 0:
    for i in menu1:
        print (i)
        sw = 1
    
    try:
        ingreso_opciones_menu1 = int (input("ingrese la opción: "))
        os.system("clear")
        
        if ingreso_opciones_menu1 == 1:
            print ("----------------------------------------------")
            print ("          opcion 1 -  Registrar Cliente       ")
            print ("----------------------------------------------")
            while True:    
                    try:    
                        rutTexto = input("registre su Rut, sin dígito verificador ni puntos: ")
                        
                        for caracter in rutTexto:
                            if caracter not in caracteresPermitidosRut:
                                raise AssertionError('Ha ingresado un caracter invalido') 

                        rut = int(rutTexto)
                        if rut >= 4000000 and rut <= 999999999:
                            break
                        else:
                            os.system("clear")
                            print ("----------------------------------------------")
                            print ("           NO ES UN RUT VALIDO")
                            print ("----------------------------------------------")
                            sw2 = 0 
                    except AssertionError as ae:
                        os.system("clear")
                        print ("----------------------------------------------")
                        print ("   ", ae, "   ")
                        print ("----------------------------------------------")        
                        sw = 0    
                    except ValueError:
                        os.system("clear")
                        print ("----------------------------------------------")
                        print ("   INGRESE SIN PUNTOS NI LETRAS NI GUIONES")
                        print ("----------------------------------------------")        
                        sw = 0
                        

            sw = 0
            nombre    = (input("registre su nombre    : "))
            direccion = (input("registre su Dirección : "))
            comuna    = (input("registre su Comuna    : "))

            while True:    
                mail = (input ("ingrese mail          : "))
                if "@" in mail:
                    break
                else:
                    print ("----------------------------------------------")
                    print ("  NO ES UN MAIL VALIDO, NO OLVIDE INGRESAR @  ")
                    print ("----------------------------------------------")
                    
            sw = 0
            while True:
                    try:
                        edad_texto = (input("registre su Edad    : "))
                        for caracter in rutTexto:
                            if caracter not in caracteresPermitidosRut:
                                raise AssertionError('Ha ingresado un caracter invalido') 

                        edad = int(edad_texto)
                        if edad >= 1 and edad <= 110:
                            break
                        else:
                            print ("----------------------------------------------")
                            print ("    NO ES EDAD CORRECTA, IGRESE NUEVAMENTE    ")
                            print ("----------------------------------------------")
                    except AssertionError as ae:
                            os.system("clear")
                            print ("----------------------------------------------")
                            print ("   ", ae, "   ")
                            print ("----------------------------------------------")        
                            sw = 0    
                    except ValueError:
                        print ("----------------------------------------------")
                        print ("           INGRESE SOLO NUMEROS               ")
                        print ("----------------------------------------------")


            sw = 0        
            while True:
                genero = (input("ingrese su genero con f/m: "))
                if genero == "f" or genero == "m":
                    break
                else:
                    print ("----------------------------------------------")
                    print ("      OPCION NO VALIDA, IGRESE NUEVAMENTE     ")
                    print ("----------------------------------------------")

            sw = 0
            while True:
                try:
                    celu_texto = (input("registre su número de teléfono    : "))
                    for caracter in celu_texto:
                        if caracter not in caracteresPermitidosRut:
                            raise AssertionError('Ha ingresado un caracter invalido') 

                    celu = int(celu_texto)
                    if celu >= 90000000 and celu <= 99999999:
                        break
                    else:
                        print ("----------------------------------------------")
                        print ("      ERROR DE INGRESO, IGRESE NUEVAMENTE     ")
                        print ("----------------------------------------------")
                except AssertionError as ae:
                        os.system("clear")
                        print ("----------------------------------------------")
                        print ("   ", ae, "   ")
                        print ("----------------------------------------------")        
                        sw = 0    
                except ValueError:
                    print ("----------------------------------------------")
                    print ("           INGRESE SOLO NUMEROS               ")
                    print ("----------------------------------------------")       
                       

            sw = 0
            while True:
                tipo_cuenta = (input("ingrese Tipo de cuenta (a)Premium (b)Gold (c)Silver "))
                if tipo_cuenta ==  "a":
                    tipo_cuenta = "Premium"
                    break
                if tipo_cuenta == "b":
                    tipo_cuenta = "Gold"
                    break
                if tipo_cuenta == "c":
                    tipo_cuenta = "Silver"
                    break
                else:
                    print ("----------------------------------------------")
                    print ("      OPCION NO VALIDA, IGRESE NUEVAMENTE     ")
                    print ("----------------------------------------------")
            # concat = rut, nombre, direccion, comuna, mail, edad, genero,celu,tipo_cuenta
            # nuevo_usuario = []
            # nuevo_usuario.append (rutTexto)
            # nuevo_usuario.append (nombre)
            # nuevo_usuario.append (direccion)
            # nuevo_usuario.append (comuna)
            # nuevo_usuario.append (correo)
            # nuevo_usuario.append (edad_texto)
            # nuevo_usuario.append (genero)
            # nuevo_usuario.append (celu_texto)
            # nuevo_usuario.append (tipo_cuenta)
            # lista.append(nuevo_usuario)
            lista2 = [] 
            lista2.append (rutTexto)
            lista2.append (nombre)
            lista2.append (direccion)
            lista2.append (comuna)
            lista2.append (correo)
            lista2.append (edad_texto)
            lista2.append (genero)
            lista2.append (celu_texto)
            lista2.append (tipo_cuenta)
            lista.append(lista2)
            contador = contador + 1
            print("")
            print ("----------------------------------------------")
            print ("       El registro finalizó con éxito")
            print ("----------------------------------------------")
            print ("")
            print ("presione ENTER para continuar")
            input ("")
            os.system("clear")

                
            sw = 0            
#----------------------------------------------------------------- OPCION 2 ---------------------------------------------------------
        if ingreso_opciones_menu1 == 2:
            print ("----------------------------------------------")
            print ("          opcion 2 -  Suscripción             ")
            print ("----------------------------------------------")
            sw = 1
            while True:    
                    try:    
                        rutTexto = input("registre su Rut, sin dígito verificador ni puntos: ")
                        if contador == 0:
                            print ("")
                            print ("El usuario no existe, favor registrar usuario en opción (1)")
                            print ("")
                            print ("presione ENTER para continuar")
                            input ("")
                            os.system("clear")
                            
                            
                        for caracter in rutTexto:
                            if caracter not in caracteresPermitidosRut:
                                raise AssertionError('Ha ingresado un caracter invalido') 
                        for usuario in lista:
                            if usuario[0] == rutTexto:
                                existeUsuario = True
                                print ("si existe")
                                
                                fecha_suscripcion = input("ingrese fecha de solicitud")
                                suscripcion = []
                                suscripcion.append(fecha_suscripcion)
                                print("fecha de solicitud ingresada con éxito")
                                break
                            else:
                                print ("")
                                print ("El usuario no existe, favor registrar usuario en opción (1)")
                                print ("")
                                print ("presione ENTER para continuar")
                                input ("")
                                os.system("clear")
                                
                                
                        rut = int(rutTexto)
                        if rut >= 4000000 and rut <= 999999999:
                            break
                        else:
                            os.system("clear")
                            print ("----------------------------------------------")
                            print ("           NO ES UN RUT VALIDO")
                            print ("----------------------------------------------")
                            sw2 = 0 
                    except AssertionError as ae:
                        os.system("clear")
                        print ("----------------------------------------------")
                        print ("   ", ae, "   ")
                        print ("----------------------------------------------")        
                        sw = 0    
                    except ValueError:
                        os.system("clear")
                        print ("----------------------------------------------")
                        print ("   INGRESE SIN PUNTOS NI LETRAS NI GUIONES")
                        print ("----------------------------------------------")        
                        sw = 0

            sw = 0
            
            
    
                    
            
        #----------------------------------------------------------------- OPCION 3 ---------------------------------------------------------
    
            

        if ingreso_opciones_menu1 == 3:
            print ("----------------------------------------------")
            print ("     opcion 3 -  Consultar Datos Cliente      ")
            print ("----------------------------------------------")
            sw = 1
            while True:    
                    try:    
                        rutTexto = input("registre su Rut, sin dígito verificador ni puntos: ")
                        if contador == 0:
                            print ("")
                            print ("El usuario no existe, favor registrar usuario en opción (1)")
                            print ("")
                            print ("presione ENTER para continuar")
                            input ("")
                            os.system("clear")
                        for caracter in rutTexto:
                            if caracter not in caracteresPermitidosRut:
                                raise AssertionError('Ha ingresado un caracter invalido') 

                        rut = int(rutTexto)
                        if rut >= 4000000 and rut <= 999999999:
                            break
                        else:
                            os.system("clear")
                            print ("----------------------------------------------")
                            print ("           NO ES UN RUT VALIDO")
                            print ("----------------------------------------------")
                            sw2 = 0 
                    except AssertionError as ae:
                        os.system("clear")
                        print ("----------------------------------------------")
                        print ("   ", ae, "   ")
                        print ("----------------------------------------------")        
                        sw = 0    
                    except ValueError:
                        os.system("clear")
                        print ("----------------------------------------------")
                        print ("   INGRESE SIN PUNTOS NI LETRAS NI GUIONES")
                        print ("----------------------------------------------")        
                        sw = 0

            sw = 0
            existeUsuario = False

            for usuario in lista:
                if usuario[0] == rutTexto:
                    existeUsuario = True
                    print ("Rut       : ", usuario[0],
                         "\nNombre    : ", usuario[1],
                         "\nDirección : ", usuario[2],
                         "\nComuna    : ", usuario[3],
                         "\nCorreo    : ", usuario[4],
                         "\nEdad      : ", usuario[5],
                         "\nGénero    : ", usuario[6],
                         "\nCelular   : ", usuario[7],
                         "\nCuenta    : ", usuario[8])
                    
                   
            sw = 0
#----------------------------------------------------------------- OPCION 4 ---------------------------------------------------------

        if ingreso_opciones_menu1 == 4:
            print ("----------------------------------------------")
            print ("             opcion 4 -  Salir                ")
            print ("----------------------------------------------")
            print ("")
            print ("Gracias por suscribirse a la App de Juan Maestro…")
            print ("")
            print ("------------  FIN DEL PROGRAMA ---------------")
            sw = 1

        if ingreso_opciones_menu1 >= 5:
            print ("----------------------------------------------")
            print (errorIngreso123)
            print ("----------------------------------------------")
            sw = 0
    
    except ValueError:
        os.system("clear")
        print ("----------------------------------------------")
        print (errorIngresoSTR)
        print ("----------------------------------------------")
        sw = 0

