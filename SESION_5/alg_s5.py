class Particion:
    """
    Clase que implementa una partición de un conjunto en subconjuntos disjuntos.
    Una partición se corresponde con una estructura Unión-Pertenencia.
    """
    
    '''
    Contiene parent, size, total_elements y num_subsets
    Este tipo de estructura se llama particion y cada agrupacion de elementos interna se llama
    subconjuntos
    '''
    def __init__(self, iterable):
        """
        Crea una partición con los elementos del iterable.
        Inicialmente cada elemento forma un subconjunto.
        """
        
        # parent -> Diccionario donde cada elemento es inicialmente su propio representante
        self.parent = {}
        
        # size -> Diccionario que almacena el tamaño de cada subconjunto (inicia en 1)
        self.size = {}
        
        # Almacenamos el total de elementos para nunero (None)
        for x in iterable:
            self.parent[x] = x
            self.size[x] = 1 
            '''
                El tamaño es uno debido a que solo es un conjunto independiente, cuando  
                se hagan union o similar se ampliara este tamaño.
            '''
        
        '''
        Se almacena el numero total de elementos indiferentemente de los subconjuntos que haya
        Este nunca cambia
        '''
        self.total_elements = len(self.parent)
        
        # Cuenta el numero de subconjuntos que tienen
        self.num_subsets = len(self.parent)
        
        '''
        Ambos parametros se igualan a len(self.parent) esto es debido a que inicialmente cada elementos
        se representa como un unico subconjunto, por ello habrá inicialmente el mismo numero de subconjuntos
        que de elementos
        '''

    def find(self, k):
        """Método auxiliar: encuentra el representante del conjunto al que pertenece k
        aplicando compresión de caminos."""
        '''
        Esta funcion comprueba si el elemento es representante de si mismo, si no lo es
        se llamara de forma recursiva hasta encontrarse.
        
        Retorna el representante de un elemento pasado por parametros
        '''
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def __len__(self):
        """Devuelve el número de subconjuntos en la partición."""
        return self.num_subsets

    def numero(self, k=None):
        """
        Devuelve el número de elementos del subconjunto al que pertenece el 
        elemento k. 
        Si k es None devuelve el número total de elementos.
        """
        
        '''
        Si k no existe retornara el numero total de elementos de la particion
        en caso de si existir, encontraremos el padre de este y retornaremos el tamaño de este
        '''
        if k is None:
            return self.total_elements
        root = self.find(k)
        return self.size[root]

    def __getitem__(self, k):
        """
        Devuelve el subconjunto (representado por su representante) al que pertenece 
        el elemento k.
        """
        return self.find(k)

    def __iter__(self):
        """
        Devuelve un iterador sobre los representantes de los subconjuntos.
        Cada subconjunto se identifica mediante uno de sus elementos (su representante).
        """
        
        '''
        Crea un set (Estructura de datos que no permite la duplicidad)
        Recorre cada subconjunto buscando su padre, si este no se encuentra en el set lo agregara y continuara
        devuelve el elemento como parte del iterador (yield)
        '''
        seen = set()
        for x in self.parent:
            rep = self.find(x)
            if rep not in seen:
                seen.add(rep)
                yield rep 
                ''' 
                La diferencia de yield con return es que yield devuelve el valor pero la funcion no rompe
                es decir, que da valores hasta terminar de recorrer el valor, rellena una lista entera, return
                solo daria un valor
                '''
    def une(self, a, b):
        """Une los subconjuntos a los que pertenecen a y b."""
        
        # Busca los representantes de ambos elementos
        rootA = self.find(a)
        rootB = self.find(b)
        
        # Si el representante de a es el mismo que de b rompe
        if rootA == rootB:
            return
        
        # Unión por tamaño: se une el árbol más pequeño al más grande.
        if self.size[rootA] < self.size[rootB]:
            self.parent[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        else:
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        self.num_subsets -= 1
        
        '''
        Lo que hace es buscar el subconjunto que tenga menos elementos para fusionarse a el, una vez lo tenga
        modifica el representante de este (parent) al nuevo y aumenta el numero de elementos (size)
        sumando ambos tamaños.
        
        Una vez terminado esto eliminará una unidad del total de numero de subconjunots debido a que se ha fusionado
        uno en
        '''


import heapq

def kruskal(grafo):
    """
    Dado un grafo representado como un diccionario, devuelve el Árbol de Expansión Mínimo (MST)
    utilizando el algoritmo de Kruskal y una cola de prioridad.
    
    - El grafo es un diccionario donde:
      - Las claves son aristas (pares de nodos).
      - Los valores son los pesos de esas aristas.
      
    Ejemplo: 
      grafo = {
        (1, 2): 3,
        (1, 3): 1,
        (2, 3): 2,
        (2, 4): 4,
        (3, 4): 5
      }
    
    - El resultado es otro diccionario con las aristas seleccionadas en el MST.
    """
    
    # Extraer todos los nodos del grafo
    conjunto_nodos = set()
    for (nodo1, nodo2) in grafo.keys():
        conjunto_nodos.add(nodo1)
        conjunto_nodos.add(nodo2)
    
    # Instanciar la estructura de partición (Union-Find)
    estructura_union = Particion(conjunto_nodos)
    
    # Crear una cola de prioridad (heap) para las aristas
    cola_prioridad = []
    for (nodo1, nodo2), peso in grafo.items():
        heapq.heappush(cola_prioridad, (peso, nodo1, nodo2))
    
    # Diccionario para almacenar el Árbol de Expansión Mínimo
    arbol_minimo = {}
    
    # Extraer las aristas en orden de menor a mayor peso
    while cola_prioridad and len(arbol_minimo) < len(conjunto_nodos) - 1:
        peso, nodo1, nodo2 = heapq.heappop(cola_prioridad)
        # Si los nodos pertenecen a conjuntos diferentes, agregamos la arista al MST
        # if estructura_union[nodo1] != estructura_union[nodo2]:
        if estructura_union.find(nodo1) != estructura_union.find(nodo2):
            arbol_minimo[(nodo1, nodo2)] = peso
            estructura_union.une(nodo1, nodo2)  # Unir los conjuntos
    
    return arbol_minimo

def kruskal_from_matrix(matrix):
    """
    Dado un grafo representado como matriz de adyacencia (lista de listas),
    donde:
      - Los nodos se identifican por índices: 0, 1, ..., n-1.
      - La matriz es simétrica (grafo no dirigido).
      - Se asume que si no hay arista, el valor es 0 o None.
    Devuelve un diccionario que representa el árbol de expansión mínima (MST),
    donde las claves son las aristas (tuplas (i, j)) y los valores son los pesos.
    """
    n = len(matrix)
    # Extraer aristas (solo la parte superior de la matriz para evitar duplicados)
    arcos = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] not in (0, None):
                arcos.append(((i, j), matrix[i][j]))
                
    # Ordenar las aristas por peso (de menor a mayor)
    arcos.sort(key=lambda x: x[1])
    
    # Inicializar la estructura Unión-Pertenencia con todos los nodos
    p = Particion(range(n))
    
    # Inicializar el MST como un diccionario vacío
    arbol = {}
    
    # Iterar sobre las aristas ordenadas y agregar las que no formen ciclo
    for (c1, c2), peso in arcos:
        if p[c1] != p[c2]:
            p.une(c1, c2)
            arbol[(c1, c2)] = peso
    return arbol


