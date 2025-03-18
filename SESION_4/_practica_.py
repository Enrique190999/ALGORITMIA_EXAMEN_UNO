# # Algoritmia
# ## Práctica 4

# El objetivo de esta práctica es trabajar con grafos.
# Se pide la implementación de las funciones que aparecen a continuación. 

# NOTA: Los grafos son dirigidos y pesados.

grafo_de_ejemplo = {
    'a': {'b': 1, 'c': 2},
    'b': {'a': 3, 'd': 6},
    'c': {'a': 5, 'b': 2},
    'd': {}
}


def numero_nodos(grafo):
    pass

# Prueba
print(numero_nodos(grafo_de_ejemplo))  # Debería imprimir 4

def numero_arcos(grafo):
    pass

# Prueba
print(numero_arcos(grafo_de_ejemplo))  # Debería imprimir 4

def peso_total(grafo):
   pass


# Prueba
print(peso_total(grafo_de_ejemplo))  # Debería imprimir 14

def inserta_nodo(grafo, nodo):
   pass
    
# Prueba
print(inserta_nodo(grafo_de_ejemplo, 'e'))  # Debería añadir 'e' como nodo sin conexiones


def arco(grafo, origen, destino):
   pass

def inserta_arco(grafo, origen, destino, peso=1):
    pass

# Prueba
print(inserta_arco(grafo_de_ejemplo, 'a', 'd', 4))  # Debería añadir arco 'a'->'d' con peso 4

def grado(grafo, nodo, salida=True):
    pass

# Prueba
print(grado(grafo_de_ejemplo, 'a'))  # Debería imprimir 2 (salida)
print(grado(grafo_de_ejemplo, 'b', salida=False))  # Debería imprimir 2 (entrada)

def pesos_adyacentes(grafo, nodo, salida=True): 
    pass

# Prueba
print(pesos_adyacentes(grafo_de_ejemplo, 'a'))  # Debería imprimir 3 (1+2)
print(pesos_adyacentes(grafo_de_ejemplo, 'b', salida=False))  # Debería imprimir 7 (3+4)

def coste_camino(grafo, camino):
    pass

# Prueba
print(coste_camino(grafo_de_ejemplo, ['a', 'b', 'd']))  # Debería imprimir 7
print(coste_camino(grafo_de_ejemplo, ['a', 'd']))  # Debería imprimir None



def prim(grafo, inicial=None):
    pass

# Prueba
print(prim(grafo_de_ejemplo))  # Debería devolver un árbol de expansión mínima
 
    
def dijkstra(grafo, nodo_inicial):
    pass       

# Prueba
print(dijkstra(grafo_de_ejemplo, 'a'))  # Debería devolver distancias y predecesores desde 'a'
       
def obten_camino_minimo(inicial, final, caminos_pre_calculados):
    pass

# Prueba
caminos = dijkstra(grafo_de_ejemplo, 'a')
print(obten_camino_minimo('a', 'd', caminos))  # Debería devolver ['a', 'b', 'd']
