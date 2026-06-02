from menu import mostrar_menu
from funcionalidades import (
    ingresar_usuario,
    validar_formato,
    tipo_caracter,
    buscar_caracter,
    usuario_espejado,
    reporte_estadistico,
    usuario_simetrico,
    ascendente_descendente,
)
print ("\n-----Bienvenido al sistema de procesamiento de nombres de usuario-----\n")

usuario = ""

opcion = mostrar_menu()

while opcion != 9: 
    match opcion:
        case 1:
            usuario = ingresar_usuario()

        case 2:
            usuario = validar_formato(usuario)

        case 3:
            usuario = tipo_caracter(usuario)
        
        case 4:
            usuario = buscar_caracter(usuario)
        
        case 5:
            usuario = usuario_espejado(usuario)

        case 6:
            usuario = reporte_estadistico(usuario)

        case 7:
            usuario = usuario_simetrico(usuario)

        case 8:
            usuario = ascendente_descendente(usuario)

        case _:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 9.\n")

    opcion = mostrar_menu()