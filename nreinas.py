'''
Problema de las 8 Reinas
Erick Colin Cruz
Coding Challenge Cuenca
'''
import sqlite3
from datetime import datetime
from sqlite3 import Error
soluciones = []

'''
Funcion recursiva que valua los valores de filas columnas y diagonales
Params: reinasEnTablero:reinas validas
        diag135:diagonal hacia la izquierda
        diag45: diagonal hacia la derecha
'''
def intentos(reinasEnTablero, diag135, diag45, reinas):
    validas = len(reinasEnTablero)
    if (validas == reinas): 
        soluciones.append(reinasEnTablero)
    else:
        for actual in range(reinas):
            if (actual not in reinasEnTablero and validas-actual not in diag135 and validas+actual not in diag45):
                intentos(reinasEnTablero + [actual], diag135 + [validas-actual], diag45 + [validas + actual], reinas)

'''
Funcion principal
Params: Numero de reinas
'''
def main(reinas):
        
    global soluciones
    reinasEnTablero = []
    diag135 = []
    diag45 = []


    intentos(reinasEnTablero, diag135, diag45, reinas)
    guardarResultadps(reinas,len(soluciones))
    return len(soluciones)

'''
Obtiene los resultados de la bd
'''
def verResultados():
    cursorObj = sqlConnection().cursor()
    sqlTabla(sqlConnection())
    cursorObj.execute('SELECT * FROM resultados')
    rows = cursorObj.fetchall()
    print("( Id, reinas, Soluciones, fecha)")
    for row in rows:
        print(row)
    
'''
Guarda los resultados en la bd
'''
def guardarResultadps(reinas, soluciones):
    con = sqlConnection()
    sqlTabla(con)
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO resultados VALUES(1, "+str(reinas)+", "+str(soluciones)+", '"+datetime.now().strftime('%b/%d/%Y')+"')")
    con.commit()
 
'''
Crea la conexion a la bd
'''
def sqlConnection():
    try:
        con = sqlite3.connect('reinas.db')
        return con
    except Error:
        print(Error)

'''
Gestiona la creacion de la tabla
'''
def sqlTabla(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE if not exists resultados(id integer PRIMARY KEY AUTOINCREMENT, reinas integer, soluciones integer, fecha text)")
    con.commit()
 


print "Problema de las N reinas"
print "Que quieres hacer?"
print "Introduce el numero segun la opcion deseada:"
print "Soluciones al Problema: 1"
print "Ver soluciones guardadas: 2"
eleccion = input()
if eleccion == 1:
    print "Introduce el numero de reinas:"
    reinas = input();
    print ("Elegiste "+ str(reinas) + " reinas");
    solucionesCount = main(reinas)
    print("Se encontraron un total de soluciones:----->> " + str(solucionesCount))
if eleccion == 2:
    verResultados()