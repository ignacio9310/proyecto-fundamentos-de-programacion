"""
2.	Poseer un menú que permita al usuario seleccionar entre al menos 4 opciones (algunas restricciones). 
a.	Presentar los datos por rango (ej: de fecha, edad, etc. ), ingresado por el usuario.
b.	Desplegar los datos, por alguna característica del dataset (edad, región, provincia, distrito, comuna, etc.)
c.	Desplegar una o más visualizaciones. 
d.	Exportar un subconjunto de datos en formato(s) seleccionado(s) por el usuario (xls, csv, txt, etc.)
3.	Desarrollar implementación en al menos 3 funciones, de las cuales, al menos una de ella debe recibir argumentos y/o retornar un resultado.
4.	Ejecutarse mientras el usuario así lo estime.
"""
import matplotlib.pyplot as plt


def lectura_archivo(nombre):
    x = open(nombre+".csv", "r")                                 
    x = x.readlines()
    lista = []
    for i in x:
        aux = []
        i = i.strip()
        i = i.split(";")
        lista.append(i)
    return lista
def imprime_como_lista(lista):
    for i in lista:
        print(i)
def opcion1_funcion(archivoLista, archivo):
    placas = []
    año1 = int(input("¿Desde que año quieres que parta tu busqueda?: "))
    año2 = int(input("¿Desde que año quieres que finalice tu busqueda?: "))
    indice = archivo[0].index("A¤o_Fabricacion")
    for i in archivoLista:
        if año1 <= i[indice] <= año2 and i[indice] != 'NULL':
            m = (i[indice], i[0])
            placas.append(m)
    placas.sort()
    imprime_como_lista(placas)
    return placas
    
def opcion2_funcion (archivoLista, archivo):
    marca = indice = archivo[0].index("Marca") 
    marcas = []
    for i in archivoSininfo:
        if not(i[marca] in marcas):
            marcas.append(i[marca])
    print("Marcas disponibles:\n")
    imprime_como_lista(marcas)
    escoje = input("Escoje una marca: ")
    patentes = []
    for i in archivoSininfo:
        if i[marca] == escoje.upper():
            dato = (i[marca], i[0])
            patentes.append(dato)
    patentes.sort()
    imprime_como_lista(patentes)
    return patentes


nom = "permiso-electronico-2021-14-12-2021"
archivo  = lectura_archivo(nom)

archivoSininfo = archivo.copy()
archivoSininfo.pop(0)
for i in archivoSininfo:
    if i[11] != "NULL":
        i[11] = int(i[11])

    elif i[11] == 'NULL':
        i[11] = 0
print(f"Lectura archivo de nombre: {nom}.csv")
while True:
    print(f"1. Filtado de placas por rango de años de fabricacion\n2. Filtrado por marca\n3. Mostrar grafico por comunas\n4. Exportar sub conjunto.\n5. Salir")

    opcion = int(input("Selecciona una opccion: "))
    if 0 < opcion <6:
        
        if opcion == 1:
            opcion1_funcion(archivoSininfo, archivo)
        elif opcion == 2:
            opcion2_funcion(archivoSininfo, archivo)
        elif opcion == 3:
            comunas = []
            datosxcomuna = []
            indice = archivo[0].index("Comuna_Propietario")
            for i in archivoSininfo:
                if not(i[indice] in comunas):
                    comunas.append(i[indice])
                    datosxcomuna.append(0)
                else:
                    indice2 = comunas.index(i[indice])
                    datosxcomuna[indice2] += 1
            plt.plot(comunas, datosxcomuna)
            plt.show()
        elif opcion == 4:
            print("¿Desea exportar el sub conjunto 1 o 2?")
            eleccion = int(input("Eleccion: "))
            if eleccion != 1 and eleccion != 2:
                print("Eleccion no valida.")
            else:
                if eleccion == 1:
                    nombre = input("Ingresa el nombre de tu nuevo archivo: ") +".csv"
                    archivo2 = open(nombre, "w")
                    fun = opcion1_funcion(archivoSininfo, archivo)
                    for i in fun:
                        for n in i:
                            archivo2.write(str(n))
                            archivo2.write(";")
                        archivo2.write("\n")
                else:
                    nombre = input("Ingresa el nombre de tu nuevo archivo: ") +".csv"
                    archivo2 = open(nombre, "w")
                    fun = opcion2_funcion(archivoSininfo, archivo)
                    for i in fun:
                        for n in i:
                            archivo2.write(str(n))
                            archivo2.write(";")
                        archivo2.write("\n")
        elif opcion == 5:
            exit()
    else:           

        print("Opcion invalida, elija otra")
