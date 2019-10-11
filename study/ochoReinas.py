'''
Problema de las 8 Reinas
Erick Colin Cruz
Coding Challenge Cuenca
'''
no_reinas = 0
tablero = []
position_first_queen = [0,0]
soluciones = 0
arregloSoluciones = []

def reinaEnFila(fila):
    print ("Numero de fila: "+ str(fila))
    return True in tablero[fila];

def reinaEnColumna(columna, n):
    tiene = False;
    for fila in range(len(tablero)):
        if(tablero[fila][columna]):
            tiene = True;
    
    return tiene;

def reinaEnDiag45(columna, fila):
    tiene = False
    diagonal = columna +  fila
    for x in range(len(tablero)):
            for y in range(len(tablero[x])):
                if((x + y) == diagonal and tablero[x][y]):
                    tiene = True

    return tiene

def reinaEnDiag135(columna, fila):
    tiene = False
    diagonal = columna -  fila
    for x in range(len(tablero)):
            for y in range(len(tablero[x])):
                if((x - y) == diagonal and tablero[x][y]):
                    tiene = True

    return tiene

def main(n):
    global no_reinas
    global tablero
    global soluciones
    allSolutions = [] # este campo es nuevo
    no_reinas = n; #Inicializo numero de reinas
    tablero = [[False for i in xrange(n)] for i in xrange(n)] #Inicializamos tablero
    for casillax in range(len(tablero)):
                for casillay in range(len(tablero[casillax])):
                    sumi = [] # este campo es nuevo
                    reinas_que_cumplen = 0
                    tablero[casillax][casillay] = True
                    no_reinas = no_reinas - 1; 
                    reinas_que_cumplen = reinas_que_cumplen + 1
                    casillaInicial = [casillax,casillay]
                    while no_reinas >= 1:
                        
                        for fila in range(len(tablero)):
                            for columna in range(len(tablero[fila])):
                                if casillax == fila and casillay == columna:
                                    sumi.append(casillaInicial)
                                    
                                if(not reinaEnFila(fila) and not reinaEnColumna(columna,n) and not reinaEnDiag135(fila, columna) and not reinaEnDiag45(fila,columna)):
                                    print("Jala la reina")
                                    tablero[fila][columna] = True
                                    reinas_que_cumplen = reinas_que_cumplen + 1
                                    no_reinas = no_reinas - 1
                                    sumi.append([fila,columna])
                                print(tablero[fila][columna])
                            print()
                        no_reinas = no_reinas - 1; 

                    if reinas_que_cumplen == n:
                        soluciones = soluciones + 1
                        if not (sumi in allSolutions):
                            allSolutions.append(sumi)
                            
                        
                    tablero = [[False for i in xrange(n)] for i in xrange(n)]
                    no_reinas = n    


    print("Numero de soluciones---->>> " + str(len(allSolutions)))
    #print("Numero de soluciones---->>> " + str(soluciones))


print "Problema de las N reinas"
print "Introduce el numero de reinas:"
n = input();
print ("Elegiste "+ str(n) + " reinas");
main(n);