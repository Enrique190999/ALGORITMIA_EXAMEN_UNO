'''
Fichero de practica de algoritmos
'''

class Particion:
    def __init__(self, iterable):
        pass
    
    def find(self, k):
        pass
    
    def __len__(self):
        pass
    
    def numero(self, k=None):
        pass
    
    def __getitem__(self, k):
        pass
    
    def __iter__(self):
        pass
    
    def une(self, a, b):
        pass
    
    def kruskal(grafo):
        pass

# Pruebas
p = Particion([1, 2, 3])
print(Particion([1, 2, 3]))  # Debería crear una partición con 3 subconjuntos
print(p.find(1))  # Debería devolver 1 inicialmente
print(len(p))  # Debería devolver 3
print(p.numero())  # Debería devolver el número total de elementos
print(p.numero(1))  # Debería devolver el tamaño del subconjunto de 1
print(p[1])  # Debería devolver el representante del subconjunto de 1
print(list(p))  # Debería devolver una lista con los representantes de los subconjuntos
p.une(1, 2)
print(p[1] == p[2])  # Debería devolver True

grafo_de_prueba = {
    (1, 2): 3,
    (1, 3): 1,
    (2, 3): 2,
    (2, 4): 4,
    (3, 4): 5
}
print(Particion.kruskal(grafo_de_prueba))  # Debería devolver un árbol de expansión mínima