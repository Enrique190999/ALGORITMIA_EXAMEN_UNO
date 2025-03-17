from SESION_5.alg_s5 import Particion

def dar_la_vuelta(cambio, valores_monedas):
    valores_monedas.sort(reverse=True)
    
    pass

def algoritmo_mochila_voraz(objetos, peso_soportado):
    pass

def algoritmo_mochila_voraz_partida(objetos, peso_soportado):
    pass

def prim(grafo, inicial=None):
    
    if grafo is None:
        return None
    
    if inicial is None:
        inicial = next(iter(grafo))
    
    import heapq
    
    arbol_minimo = {}
    visitados = set([inicial])
    cola_prioridad = []
    
    for nodo, peso in grafo.items():
        heapq.heappush(cola_prioridad,(peso,inicial,nodo))
    
    while cola_prioridad and len(visitados) < len(grafo):
        peso, origen, destino = heapq.heappop(cola_prioridad)
        if destino in visitados:
            continue
        
        visitados.add(destino)
        arbol_minimo[origen][destino] = peso
        arbol_minimo[destino][origen] = peso
        
        for peso_vecino, nodo_vecino in grafo[destino].items():
            if nodo_vecino not in visitados:
                heapq.heappush(cola_prioridad,(peso_vecino,destino,nodo_vecino))
    
    return arbol_minimo
    
def dijkstra(grafo, nodo_inicial):
    if grafo is None:
        return None
    
    if nodo_inicial not in grafo or nodo_inicial is None:
        return None
    
    from math import inf
    import heapq
    
    predecesores = {nodo:None for nodo in grafo}
    camino_minimo = {Nodo:float(inf) for Nodo in grafo}
    cola_prioridad = [(0,nodo_inicial)]
    camino_minimo[nodo_inicial] = 0
    
    while cola_prioridad:
        peso, nodo = heapq.heappop(cola_prioridad)
        
        if peso > camino_minimo[nodo_inicial]:
            continue
            
        for peso_vecino,nodo_vecino in grafo[nodo].items():
            peso_actual = peso + peso_vecino
            if peso_actual < camino_minimo[nodo_vecino]:
                heapq.heappush(cola_prioridad,(peso_actual,nodo_vecino))
                predecesores[nodo_vecino] = nodo
                camino_minimo[nodo_vecino] = peso
    
    resultado = {}
    for nodo in grafo:
        resultado[nodo] = {predecesores[nodo] if nodo != nodo_inicial else None, camino_minimo[nodo]}
    return resultado
                
        
def obten_camino_minimo(inicial, final, caminos_pre_calculados):

    from math import inf
    
    if inicial not in caminos_pre_calculados or caminos_pre_calculados[inicial] != (0,None):
        return None
    
    if final not in caminos_pre_calculados or caminos_pre_calculados[final] == float(inf):
        return None
    
    camino = []
    actual = inicial
    while actual is not None:
        camino.append(actual)
        if actual == inicial:
            break
        actual = caminos_pre_calculados[actual][0]
    
    if camino[-1] != inicial:
        return None
    
    camino.reverse()
    return camino

def kruskal(grafo):
    
    if grafo is None:
        return None

    conjunto_nodos = set()
    arbol_minimo = {}
    
    for nA, nB in grafo.keys():
        conjunto_nodos.add(nA)
        conjunto_nodos.add(nB)
    
    elemento_union = Particion(conjunto_nodos)
    
    import heapq  
    cola_prioridad = []
    arbol = {}
    for (nA,nB),peso in grafo.items():
        heapq.heappush(cola_prioridad,(peso,nA,nB))

    while cola_prioridad and len(arbol_minimo) < len(conjunto_nodos) - 1:
        peso, origen, destino = heapq.heappop(cola_prioridad)
        
        if (elemento_union.find(origen) != elemento_union.find(destino)):
            elemento_union.une(origen,destino)
            arbol[origen][destino] = peso
    
    return arbol