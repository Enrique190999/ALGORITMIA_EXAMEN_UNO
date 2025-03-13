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


def kruskal(grafo):
    """
    Dado un grafo devuelve otro grafo con el árbol expandido mínimo,
    utilizando el algoritmo de Kruskal.
    Los grafos son diccionario donde las claves son arcos (pares de nodos) y los
    valores son el peso de los arcos.
    """
    # Extraer todos los nodos presentes en el grafo
    nodes = set()
    for (u, v) in grafo.keys():
        nodes.add(u)
        nodes.add(v)

    # Crear la partición (estructura unión-pertenencia)
    particion = Particion(nodes)
    # Ordenar los arcos por peso (de menor a mayor)
    arcos_ordenados = sorted(grafo.items(), key=lambda item: item[1])
    mst = {}

    # Recorrer los arcos en orden creciente de peso
    for (u, v), peso in arcos_ordenados:
        # Si u y v están en conjuntos diferentes se añade el arco al árbol y se unen.
        if particion[u] != particion[v]:
            mst[(u, v)] = peso
            particion.une(u, v)
            # Si ya se han añadido n-1 arcos (donde n es el número de nodos), terminamos.
            if len(mst) == len(nodes) - 1:
                break

    return mst
