import pytest
'''
Proyecto de test para evaluar pruebas unitarias
'''

#Inicializamos nuestros valores para las pruebas
n=4
tablero = [[False for i in xrange(n)] for i in xrange(n)]
fila = 0
columna = 1

#Evalua que exista reina en fila
def test_reinaEnFila_true():
    tablero[0][0] = True
    print ("Numero de fila: "+ str(fila))
    assert True in tablero[fila]

#Evalua que no exista reina en fila
def test_reinaEnFila_false():
    print ("Numero de fila: "+ str(fila))
    assert not (True in tablero[fila])

#Evalua que exista reina en columna
def test_reinaEnColumna_true():
    tablero[0][1] = True
    tiene = False
    for fila in range(len(tablero)):
        if(tablero[fila][columna]):
            tiene = True

    assert tiene

#Evalua que no exista reina en columna
def test_reinaEnColumna_false():
    tiene = False
    for fila in range(len(tablero)):
        if(tablero[fila][columna]):
            tiene = True
    
    assert not tiene

#Evalua que existe reina en diagonal invertida
def test_reinaEnDiag45_true():
    tablero[1][0] = True
    tiene = False
    diagonal = columna +  fila
    for x in range(len(tablero)):
            for y in range(len(tablero[x])):
                if((x + y) == diagonal and tablero[x][y]):
                    tiene = True

    return tiene

#Evalua que no exista reina en diagonal invertida
def test_reinaEnDiag45_false():
    tiene = False
    diagonal = columna +  fila
    for x in range(len(tablero)):
            for y in range(len(tablero[x])):
                if((x + y) == diagonal and tablero[x][y]):
                    tiene = True

    return tiene

#Evalua que exista reina en diagonal
def test_reinaEnDiag135_true():
    filad=2
    columnad=3
    tablero[0][1] = True
    tiene = False
    tablero
    diagonal = columnad -  filad
    for x in range(len(tablero)):
            for y in range(len(tablero[x])):
                if((x - y) == diagonal and tablero[x][y]):
                    tiene = True

    assert tiene

#Evaua que no exista reina en diagonal
def test_reinaEnDiag135_false():
    tiene = False
    diagonal = columna -  fila
    for x in range(len(tablero)):
            for y in range(len(tablero[x])):
                if((x - y) == diagonal and tablero[x][y]):
                    tiene = True

    assert not tiene

soluciones = []
def intentos(reinasEnTablero, diag135, diag45, reinas):
    validas = len(reinasEnTablero)
    if (validas == reinas): 
        soluciones.append(reinasEnTablero)
    else:
        for actual in range(reinas):
            if (actual not in reinasEnTablero and validas-actual not in diag135 and validas+actual not in diag45):
                intentos(reinasEnTablero + [actual], diag135 + [validas-actual], diag45 + [validas + actual], reinas)

                
#Encuentra todas las posibles soluciones
def test_allSolutions():
    global soluciones
    reinasEnTablero = []
    diag135 = []
    diag45 = []
    reinas= 0
    while True:
        try:
            intentos(reinasEnTablero, diag135, diag45, reinas)
            reinas += 1
        except Exception
            break
    
    assert len(soluciones) > 0

