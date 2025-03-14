# Fichero de practica

def numero_nodos(grafo):
    return len(grafo)

def numero_arcos(grafo):
    total = 0
    for nodo in grafo.values():
        total += len(nodo)
    return total

def peso_total(grafo):
    total = 0
    for nodo in grafo.values():
        for arco in nodo.values():
            total += arco
    
    return total

def arco(grafo, origen, destino):
    if origen in grafo and destino in grafo[origen]:
        return grafo[origen][destino]
    return None

def inserta_nodo(grafo, nodo):
    if nodo not in grafo:
        grafo[nodo] = {}
    return grafo

def inserta_arco(grafo, origen, destino, peso=1):
    if origen in grafo and destino in grafo and grafo[origen][destino] == None:
        grafo[origen][destino] = peso
    return grafo
        

def grado(grafo, nodo, salida=True):
    if nodo not in grafo:
        return None

    if salida:
        return len(grafo[nodo])
    total = 0
    for x in grafo:
        if nodo in grafo[x]:
            total += 1
    return total
    

def pesos_adyacentes(grafo, nodo, salida=True):
    if nodo not in grafo:
        return None
    
    if salida:
        return sum(grafo[nodo].values())
            
    total = 0
    
    for x in grafo:
        if nodo in grafo[x]:
            total += grafo[x][nodo]
    return total

def coste_camino(grafo, camino):
    if camino is None:
        return 0
    
    total = 0
    for i in range(len(camino) - 1):
        peso = arco(grafo,grafo[i],grafo[i+1])
        if peso is None:
            return None
        total += peso
    return total
        

def prim(grafo, inicial=None):
    if grafo is None:
        return None
    
    if inicial is None:
        inicial = next(iter(grafo))
        
    arbol_minimo = {n:{} for n in grafo}
    nodos_visitados = set([inicial])
    
    import heapq
    cola_prioridad = []
    
    for nodo, peso in grafo[inicial]:
        heapq.heappush(cola_prioridad,(peso,inicial,nodo))
    
    while cola_prioridad and len(nodos_visitados) < len(grafo):
        peso,origen,destino = heapq.heappop(cola_prioridad)
        
        if destino in nodos_visitados:
            continue
        
        arbol_minimo[origen][destino] = peso
        arbol_minimo[destino][origen] = peso
        nodos_visitados.add(destino)
        
        for vecino, peso_vecino in grafo[destino].items():
            if vecino in nodos_visitados:
                continue
            heapq.heappush(cola_prioridad,(peso,destino,vecino))
    
    return arbol_minimo
    
def dijkstra(grafo, nodo_inicial):
    if grafo is None:
        return None
    
    if nodo_inicial not in grafo:
        return 0
    
    predecesores = {n:None for n in grafo}
    from math import inf
    distancia_minima = {n:float(inf) for n in grafo}
    import heapq
    cola_prioridad = [(0,nodo_inicial)]
    while cola_prioridad:
        distancia,nodo = heapq.heappop(cola_prioridad)
        if distancia > distancia_minima[nodo]:
            continue
        
        for nodo_vecino, peso_vecino in grafo[nodo]:
            distancia_actual = distancia_minima[nodo] + peso_vecino
            if distancia_actual < distancia_minima[nodo_vecino]:
                distancia_minima
                
        
    
def obten_camino_minimo(inicial, final, caminos_pre_calculados):
    pass