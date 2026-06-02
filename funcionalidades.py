def escaneo_manual(usuario = str, input_caracter = str):
    largo_usuario = len(usuario)

    cantidad = 0
    posiciones = []
    cantdad_letras = 0
    cantidad_numeros = 0
    cantidad_simbolos = 0
    cantidad_puntos = 0
    cantidad_gion_bajo = 0

    simbolos_permitidos = '_.'

    for i in usuario:
        if ("a" <= i <= "z") or ("A" <= i <= "Z"):
            cantdad_letras += 1
        elif "0" <= i <= "9":
            cantidad_numeros += 1
        else:
            for simbolo in simbolos_permitidos:
                if i == simbolo:
                    cantidad_simbolos += 1
                    if i == ".":
                        cantidad_puntos += 1
                    elif i == "_":
                        cantidad_gion_bajo += 1
                    break

    for i in range(largo_usuario):
        if usuario[i] == input_caracter:
            cantidad += 1
            posiciones.append(i)

    usuario_espejado = ""
    for i in usuario:
        usuario_espejado = i + usuario_espejado
    
    return largo_usuario, cantdad_letras, cantidad_numeros, cantidad_simbolos, cantidad, posiciones, usuario_espejado, cantidad_puntos, cantidad_gion_bajo   



def ingresar_usuario():
    """
    Ingresa y guarda nombre de usuario
    
    retorna:
    - usuario: str
    """
    usuario_valido = False
            
    while usuario_valido == False:
        usuario_temp = input("\nIngresa el nombre de usuario: ")
        largo = len(usuario_temp)
        usuario_valido = True
        
        if largo < 6 or largo > 15:
            print("El usuario debe tener entre 6 y 15 ies.")
            usuario_valido = False
        
        if usuario_valido:
            if "0" <= usuario_temp[0] <= "9":
                print("El usuario no puede comenzar con un número.")
                usuario_valido = False
        
        if usuario_valido:
            tiene_letra = False
            tiene_espacios = False
            tiene_caracter_invalido = False
            
            for i in usuario_temp:
                if i == " ":
                    tiene_espacios = True
                elif ("a" <= i <= "z") or ("A" <= i <= "Z"):
                    tiene_letra = True
                elif "0" <= i <= "9":
                    pass
                elif i == "_" or i == ".":
                    pass 
                else:
                    tiene_caracter_invalido = True
                    
            if tiene_espacios:
                print("El usuario no puede tener espacios.")
                usuario_valido = False
            elif tiene_caracter_invalido:
                print("Solo se permiten letras, números, guion bajo (_) y punto (.).")
                usuario_valido = False
            elif not tiene_letra:
                print("El usuario debe tener al menos una letra.")
                usuario_valido = False

    usuario = usuario_temp
    print("\n--------Nombre de usuario guardado correctamente!!!--------\n")

    
    return usuario
        
def validar_formato(usuario: str):
    """
    Valida el formato del usuario ingresado
    
    parametros:
    - usuario: str
    
    retorna:
    - usuario: str
    """
    if usuario == "":
        print("\n--------No se ha ingresado un nombre de usuario aún.--------\n")
    else:
        escaneo_manual(usuario)
        largo, _, cantidad_numeros, cantidad_simbolos, _, _, _, _, _= escaneo_manual(usuario)

        if cantidad_numeros > 0 and largo >= 12 and cantidad_simbolos > 0:
            print(f"\nEl usuario \"{usuario}\" es: AVANZADO \n")
        elif largo >= 8 and cantidad_numeros > 0 and cantidad_simbolos == 0:
            print(f"\nEl usuario \"{usuario}\" es: INTERMEDIO \n")
        elif largo >= 6 and largo <= 8 and cantidad_numeros == 0:
            print(f"\nEl usuario \"{usuario}\" es: BASICO \n")
        else:
            print(f"\nEl usuario \"{usuario}\" es: SIN CATEGORIA\n")

    return usuario

def tipo_caracter(usuario: str):
    """
    Cuenta la cantidad de letras, números y símbolos en el usuario ingresado
    
    parametros:
    - usuario: str
    
    retorna:
    - usuario: str
    """
    if usuario == "":
        print("\n--------No se ha ingresado un nombre de usuario aún.--------\n")
    else:
        _, cantdad_letras, cantidad_numeros, _, _, _, _, cantidad_puntos, cantidad_gion_bajo = escaneo_manual(usuario)
        print(f"\n  El usuario \"{usuario}\" tiene:\n   {cantdad_letras} letras\n   {cantidad_numeros} números\n   {cantidad_puntos} puntos\n   {cantidad_gion_bajo} guion bajos.\n")

    return usuario

def buscar_caracter(usuario: str):
    """
    Solicita un caracter al usuario

    parametros:
    - usuario: str
    
    retorna:
    - input_caracter: str
    """
    if usuario == "":
        print("\n--------No se ha ingresado un nombre de usuario aún.--------\n")
    else:
        input_caracter = input("\nIngrese el caracter que quiera buscar: ")

        _, _, _, _, cantidad, posiciones, _, _, _ = escaneo_manual(usuario, input_caracter)

        print(f"El carácter '{input_caracter}' aparece: {cantidad} veces.\n")
        if cantidad > 0:
            print(f"Encontrado en las posiciones (índices): {posiciones}")
    return usuario

def usuario_espejado(usuario: str):
    """
    Muestra el usuario al revés
    
    parametros:
    - usuario: str
    
    retorna:
    - usuario_espejado: str
    """
    if usuario == "":
        print("\n--------No se ha ingresado un nombre de usuario aún.--------\n")      
    else:
        print(f"\nEl usuario es: \"{usuario}\" \n")
        _, _, _, _, _, _, usuario_espejado, _, _ = escaneo_manual(usuario)
        print(f"\nY el usuario espejado es: \"{usuario_espejado}\"\n")
    
    return usuario

def reporte_estadistico(usuario: str):
    """
    Muestra un reporte estadístico del usuario ingresado
    
    parametros:
    - usuario: str
    
    retorna:
    - usuario: str
    """
    if usuario == "":
        print("\n--------No se ha ingresado un nombre de usuario aún.--------\n")
    else:
        largo_usuario, cantdad_letras, cantidad_numeros, cantidad_simbolos, _, _, _, _, _= escaneo_manual(usuario)

        porcentaje_letras = (cantdad_letras * 100) / largo_usuario
        porcentaje_numeros = (cantidad_numeros * 100) / largo_usuario
        porcentaje_simbolos = (cantidad_simbolos * 100) / largo_usuario

        print(f"\nUsuario:\n \"{usuario}\" \n\nLongitud total: {largo_usuario} caracteres. \nPorcentaje de letras: {porcentaje_letras:.2f}% \nPorcentaje de números: {porcentaje_numeros:.2f}% \nPorcentaje de símbolos: {porcentaje_simbolos:.2f}%\n")

    return usuario

def usuario_simetrico(usuario: str):
    """
    verifica si la primera mitad del usuario es igual a la segunda

    parametros:
    - usuario: str

    retorna:
    - usuario: str
    """
    if usuario == "":
        print("\n--------No se ha ingresado un nombre de usuario aún.--------\n")
    else:
        largo, _, _, _, _, _, _, _, _ = escaneo_manual(usuario)
        mitad = largo // 2

        if largo % 2 == 0:
            primera_mitad = usuario[:mitad]
            segunda_mitad = usuario[mitad:]
        else:
            print(f"\nEl usuario \"{usuario}\" es impar por lo cual no tiene mitad.\n")

        if primera_mitad == segunda_mitad:
            print(f"\nEl usuario \"{usuario}\" es simétrico.\n")
        else:
            print(f"\nEl usuario \"{usuario}\" no es simétrico.\n")

    return usuario

def ascendente_descendente(usuario: str):
    """
    Ordena los caracteres del usuario de forma ascendente o descendente

    parametros:
    - usuario: str

    retorna:
    - usuario: str
    """
    if usuario == "":
        print("\n--------No se ha ingresado un nombre de usuario aún.--------\n")
    else:
        orden = input("\nEliga como quiere ordenar: \n1. Ascendente\n2. Descendente\n: ")
        
        if orden != "1" and orden != "2":
            print("Opción inválida.")
        else:
            largo = len(usuario)
        
            lista_caracteres = []
            i = 0
            while i < largo:
                lista_caracteres.append(usuario[i])
                i += 1
            
            i = 0
            while i < largo:
                j = 0
                while j < largo - i - 1:
                    
                    debe_intercambiar = False
                    
                    if orden == "1":
                        if lista_caracteres[j] > lista_caracteres[j + 1]:
                            debe_intercambiar = True
                    else:
                        if lista_caracteres[j] < lista_caracteres[j + 1]:
                            debe_intercambiar = True
                    
                    if debe_intercambiar:
                        temporal = lista_caracteres[j]
                        lista_caracteres[j] = lista_caracteres[j + 1]
                        lista_caracteres[j + 1] = temporal
                        
                    j += 1
                i += 1
            
            usuario_ordenado = ""
            k = 0
            while k < largo:
                usuario_ordenado += lista_caracteres[k]
                k += 1

            print(f"Usuario: {usuario}")
            
            if orden == "1":
                print(f"\nUsuario Ascendente:  {usuario_ordenado}\n")
            else:
                print(f"\nUsuario Descendente: {usuario_ordenado}\n")
            
    return usuario