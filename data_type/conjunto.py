class Conjunto:
    def __init__(self):
        self.elementos = set()
    
    def agregar(self, item):
        self.elementos.add(item)
    
    def eliminar(self, item):
        self.elementos.discard(item)
    
    def contiene(self, item):
        return item in self.elementos
    
    def size(self):
        return len(self.elementos)
    
    def __str__(self):
        return str(self.elementos)

def demostracion():
    print("Creando un conjunto vacío.")
    conj = Conjunto()
    
    print("Agregando elementos: 1, 2, 3, 4")
    for i in [1, 2, 3, 4]:
        conj.agregar(i)
    print("Contenido del conjunto:", conj)
    
    print("Eliminando el elemento 2.")
    conj.eliminar(2)
    
    print("Verificando si contiene el elemento 2:", conj.contiene(2))
    print("Tamaño actual del conjunto:", conj.size())
