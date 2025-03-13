class Particion:
    def __init__(self, elementos):
        self.padre = {x: x for x in elementos}
        self.tamano = {x: 1 for x in elementos}
    
    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]
    
    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        if raiz_x == raiz_y:
            return
        if self.tamano[raiz_x] < self.tamano[raiz_y]:
            self.padre[raiz_x] = raiz_y
            self.tamano[raiz_y] += self.tamano[raiz_x]
        else:
            self.padre[raiz_y] = raiz_x
            self.tamano[raiz_x] += self.tamano[raiz_y]

class Grafo:
    def __init__(self):
        self.aristas = {}  # Diccionario: {(u, v): peso}
        self.nodos = set()
    
    def agregar_arista(self, u, v, peso):
        self.aristas[(u, v)] = peso
        self.nodos.add(u)
        self.nodos.add(v)
    
    def kruskal(self):
        # Ordenar aristas por peso (de menor a mayor)
        aristas_ordenadas = sorted(self.aristas.items(), key=lambda x: x[1])
        particion = Particion(self.nodos)
        mst = {}
        for (u, v), peso in aristas_ordenadas:
            if particion.find(u) != particion.find(v):
                mst[(u, v)] = peso
                particion.union(u, v)
                if len(mst) == len(self.nodos) - 1:
                    break
        return mst

def demostracion():
    print("Creando un grafo con 6 nodos y 9 aristas.")
    g = Grafo()
    
    aristas = [
        ("a", "b", 13),
        ("a", "c", 8),
        ("a", "d", 1),
        ("b", "c", 15),
        ("c", "d", 5),
        ("c", "e", 3),
        ("d", "e", 4),
        ("d", "f", 5),
        ("e", "f", 2)
    ]
    
    for u, v, peso in aristas:
        g.agregar_arista(u, v, peso)
    
    print("Aristas del grafo:")
    for (u, v), peso in g.aristas.items():
        print(f"{u} - {v} : {peso}")
    
    print("\nEjecutando el algoritmo de Kruskal para obtener el árbol de expansión mínima:")
    mst = g.kruskal()
    print("Resultado (árbol de expansión mínima):")
    for (u, v), peso in mst.items():
        print(f"{u} - {v} : {peso}")
