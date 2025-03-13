# # Algoritmia
# ## Práctica 4

# El objetivo de esta práctica es trabajar con grafos.
# Se pide la implementación de las funciones que aparecen a continuación. 

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.

# El grafo se puede representar como un diccionario de diccionarios o como una matriz de adyacencia.
# Para esta práctica se usará la representación de diccionario de diccionarios.

# NOTA: Los grafos son dirigidos y pesados.

grafo_de_ejemplo = {
    'a': {'b': 1, 'c': 2},
    'b': {'a': 3, 'd': 6},
    'c': {'a': 5, 'b': 2},
    'd': {}
}

# Funciones genéricas de grafos
def numero_nodos(grafo):
    """Número de nodos en el grafo"""
    return len(grafo)


def numero_arcos(grafo):
    """Número de arcos en el grafo"""
    return sum(len(adyacentes) for adyacentes in grafo.values())


def peso_total(grafo):
    """Suma de los pesos de los arcos del grafo"""
    return sum(sum(adyacentes.values()) for adyacentes in grafo.values())


def arco(grafo, origen, destino):
    """
    Si hay un arco de origen a destino, devuelve su peso. 
    Si no hay, devuelve None.
    """
    if origen in grafo and destino in grafo[origen]:
        return grafo[origen][destino]
    return None


# Operaciones de modificación

def inserta_nodo(grafo, nodo):
    """
    Inserta el nodo en el grafo.
    Si ya estaba, no se modifica.
    Devuelve el propio grafo.
    """
    if nodo not in grafo:
        grafo[nodo] = {}
    return grafo


def inserta_arco(grafo, origen, destino, peso=1):
    """
    Inserta el arco en el grafo.
    Si ya estaba se actualiza el peso.
    Devuelve el propio grafo.
    """
    inserta_nodo(grafo, origen)
    inserta_nodo(grafo, destino)
    grafo[origen][destino] = peso
    return grafo


# Operaciones de consulta
def grado(grafo, nodo, salida=True):
    """
    Devuelve el grado de salida o entrada de un nodo del grafo.
    Estos grados son el número de arcos que salen o llegan al nodo.
    """
    if salida:
        return len(grafo.get(nodo, {}))
    else:
        return sum(1 for origen in grafo if nodo in grafo[origen])

 
def pesos_adyacentes(grafo, nodo, salida=True):
    """
    Devuelve la suma de los pesos de los arcos adyacentes al nodo, 
    de salida o entrada.
    """
    if salida:
        return sum(grafo.get(nodo, {}).values())
    else:
        total = 0
        for origen in grafo:
            if nodo in grafo[origen]:
                total += grafo[origen][nodo]
        return total


def coste_camino(grafo, camino):
    """
    Devuelve el coste del camino en el grafo.
    El camino viene dado como una secuencia de nodos.
    Si esa secuencia no forma un camino, devuelve None.
    """
    if not camino:
        return 0
    total = 0
    for i in range(len(camino) - 1):
        peso = arco(grafo, camino[i], camino[i + 1])
        if peso is None:
            return None
        total += peso
    return total

    
###################
# Habiendo creado las funciones anteriores, se pide implementar los siguientes métodos:

def prim(grafo, inicial=None):
    """
    Implementa el algoritmo de Prim para obtener el árbol de expansión mínima de un grafo. Devuelve en el formato del grafo el árbol.

    Se recuerda que un árbol es un grafo sin bucles y conectado.

    El grafo que se va a recibir siempre será conexo y sin direcciones.
    """
    import heapq

    # Si no existe el grafo retorna un conjunto vacio
    if not grafo: 
        return {}
    
    # Si no se ha pasado un nodo por el que empezar, se comenzara la iteración
    # yendo al primer elemento del grafo
    if inicial is None:
        inicial = next(iter(grafo))
    
    # Inicializamos el árbol con todos los nodos y sin arcos.
    arbol = {nodo: {} for nodo in grafo}
    visitados = set([inicial])
    # Cola de prioridad: (peso, nodo_origen, nodo_destino)
    cola = []
    for destino, peso in grafo[inicial].items():
        heapq.heappush(cola, (peso, inicial, destino))
    
    # Mientras exista cola y no se hayan visitado todos los nodos continuamos
    while cola and len(visitados) < len(grafo):
        # Extrae el elemento con menos valor del grafo
        peso, origen, destino = heapq.heappop(cola)
        # Si se encuentra visitado continua a la siguiente iteración
        if destino in visitados:
            continue
        # Agregamos el arco al árbol (de forma simétrica) y agregamos el elemento a los visitados
        arbol[origen][destino] = peso
        arbol[destino][origen] = peso
        visitados.add(destino)
        # Recorremos los nodos del ultimo nodo visitado 
        for vecino, peso_v in grafo[destino].items():
            # Si uno de esos nodos de este nodo recorriendolo no esta visitado se agrega a la cola
            
            if vecino not in visitados:
                heapq.heappush(cola, (peso_v, destino, vecino))
    # Finalmente retornamos el arbol
    return arbol


import heapq

def dijkstra(grafo, nodo_inicial):
    """
    Implementa el algoritmo de Dijkstra para encontrar la distancia mínima desde un nodo inicial 
    a todos los demás nodos del grafo.

    Devuelve un diccionario con el formato:
        { nodo: (predecesor, distancia_mínima) }
    
    - Para el nodo inicial, el predecesor es None y la distancia es 0.
    - Para los nodos no alcanzables, la distancia es float("inf") y el predecesor es None.
    """

    # Si el nodo inicial no está en el grafo, retornamos un diccionario vacío
    if nodo_inicial not in grafo:
        return {}
    # Inicializamos distancias a infinito y predecesores a None
    distancia_minima = {nodo: float("inf") for nodo in grafo}
    predecesor = {nodo: None for nodo in grafo}


    # La distancia al nodo inicial es 0
    distancia_minima[nodo_inicial] = 0

    # Cola de prioridad (heap) con tuplas (distancia, nodo)
    cola_prioridad = [(0, nodo_inicial)]

    while cola_prioridad:
        # Extraemos el nodo con la menor distancia conocida
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si encontramos una distancia mayor que la registrada, la ignoramos
        if distancia_actual > distancia_minima[nodo_actual]:
            continue

        # Recorremos los nodos vecinos del nodo actual
        for nodo_vecino, peso_arco in grafo[nodo_actual].items():
            nueva_distancia = distancia_minima[nodo_actual] + peso_arco

            # Si encontramos un camino más corto hacia el nodo vecino, lo actualizamos
            if nueva_distancia < distancia_minima[nodo_vecino]:
                distancia_minima[nodo_vecino] = nueva_distancia
                predecesor[nodo_vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, nodo_vecino))

    # Construimos el resultado final
    resultado = {}
    for nodo in grafo:
        resultado[nodo] = (predecesor[nodo] if nodo != nodo_inicial else None, distancia_minima[nodo])

    return resultado



def obten_camino_minimo(inicial, final, caminos_pre_calculados):
    """
    Devuelve el camino mínimo entre dos nodos, a partir de la información obtenida con Dijkstra.
    Si no hay camino, devuelve None.
    
    Se espera que 'caminos_pre_calculados' sea el diccionario devuelto por dijkstra,
    de modo que para el nodo fuente se tenga (None, 0). Si no es así, se levanta una excepción.
    """
    # Verificar que los caminos pre calculados correspondan al nodo inicial
    if inicial not in caminos_pre_calculados or caminos_pre_calculados[inicial] != (None, 0):
        raise Exception("Los caminos pre calculados no corresponden al nodo inicial proporcionado.")
    
    if final not in caminos_pre_calculados or caminos_pre_calculados[final][1] == float("inf"):
        return None

    camino = []
    actual = final
    # Se reconstruye el camino siguiendo los predecesores
    while actual is not None:
        camino.append(actual)
        if actual == inicial:
            break
        actual = caminos_pre_calculados[actual][0]
    
    # Si el último nodo no es el inicial, el camino no es válido
    if camino[-1] != inicial:
        return None
    camino.reverse()
    return camino
