from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def encolar(self, item):
        self.elementos.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.popleft()
        raise IndexError("desencolar de cola vacía")
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def size(self):
        return len(self.elementos)

def demostracion():
    print("Creando una cola vacía.")
    cola = Cola()
    
    print("Encolando elementos: 'a', 'b', 'c'")
    cola.encolar('a')
    cola.encolar('b')
    cola.encolar('c')
    
    print("Desencolando un elemento:", cola.desencolar())
    print("Tamaño actual de la cola:", cola.size())
