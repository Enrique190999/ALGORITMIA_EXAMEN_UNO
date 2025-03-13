def numero_nodos(grafo):
    return len(grafo)

def numero_arcos(grafo):
    total = 0
    for item in grafo:
        total += len(item)
    return total

def inserta_nodo(nodo,grafo):
    if not nodo in grafo:
        grafo[nodo] = {}
    return grafo

def grado(grafo,nodo, salida = True):
    if not nodo in grafo:
        return None

    if salida:
        return len(grafo[nodo])
    
    total = 0
    for item in grafo:
        if nodo in grafo[item]:
            total+=1
    return total

def peso_adyacentes(grafo, nodo,salida=True):
    if not nodo in grafo:
        return None

    if salida:
        return sum(grafo[nodo])
    
    total = 0
    for item in grafo:
        if nodo in grafo[item]:
            total += grafo[item][nodo]
    
    return total


def inserta_arco(origen, destino, grafo,peso):
    if origen in grafo and destino in grafo[origen]:
        grafo[origen][destino] = peso
    return grafo

def arco(origen, destino, grafo):
    if origen in grafo and destino in grafo[origen]:
        return grafo[origen][destino]

def coste_camino (grafo, camino):
    if camino is None:
        return None

    peso = 0
    for i in range(len(camino) - 1):
        origen = camino[i]
        destino = camino[i+1]
        pArco = arco(origen,destino,grafo)
        if pArco is None:
            return None
        peso += pArco
    
    return peso

def algoritmo_prim(grafo, inicial = None):
    if grafo is None:
        return {}
    
    if inicial is None:
        inicial = next(iter(grafo))
    
    import heapq
    cola_prioridad = []
    
    nodos_visitados = set([inicial])
    arbol_minima_expresion = {Nodo: {} for Nodo in grafo}
    
    for peso, nodo in grafo[inicial].items():
        heapq.heappush(cola_prioridad,(peso,inicial,nodo))
    
    while cola_prioridad and len(nodos_visitados) < len(grafo):
        peso, origen, destino = heapq.heappop(cola_prioridad)
        
        if destino in nodos_visitados:
            continue
        
        nodos_visitados.add(destino)
        arbol_minima_expresion[origen][destino] = peso
        arbol_minima_expresion[destino][origen] = peso
        
        for peso_vecino, nodo_vecino in grafo[destino].items():
            if not nodo_vecino in nodos_visitados:
                heapq.heappush(cola_prioridad,(peso_vecino,destino,nodo_vecino))
    
    return arbol_minima_expresion

def algoritmo_dijkstra(grafo, nodo_inicial):
    if grafo is None:
        return None
    
    from math import inf
    distancia_minima = {n:float(inf) for n in grafo}
    predecesores = {n:None for n in grafo}
    
    import heapq
    cola_prioridad = [(0,nodo_inicial)]
    
    while cola_prioridad:
        distancia, nodo = heapq.heappop()
        
        if distancia > distancia_minima[nodo]:
            continue
        
        for distancia_vecino, nodo_vecino in grafo[nodo].items():
            distancia_actual = distancia_minima[nodo] + distancia_vecino
            
            if distancia_actual < distancia_minima[nodo_vecino]:
                distancia_minima[nodo_vecino] = distancia_actual
                predecesores[nodo_vecino] = nodo
                heapq.heappush(cola_prioridad,(distancia_actual,nodo_vecino))
            
    resultado = {}
    for nodo in grafo:
        resultado[nodo] = {predecesores[nodo] if nodo != nodo_inicial else None, distancia_minima[nodo]}

    return resultado


def camino_mas_corto(inicial, final,camino_preestablecido):
    if inicial not in camino_preestablecido or camino_preestablecido[inicial] != (None,0):
        raise Exception("Error")
    
    from math import inf    
    if final not in camino_preestablecido or camino_preestablecido[final][1] == float(inf):
        return None
    
    actual = inicial
    camino = []
    
    while actual is not None:
        camino.append(actual)
        if actual == inicial:
            break
        actual = camino_preestablecido[actual][0]
    
    if camino[-1] != inicial:
        return None
    
    camino.reverse()
    return camino
                    
                
    