class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False
    
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False
    
    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual.valor
            actual = actual.siguiente

def demostracion():
    print("Creando una lista enlazada vacía.")
    lista = ListaEnlazada()
    
    print("Insertando elementos (10, 20, 30, 40):")
    for num in [10, 20, 30, 40]:
        lista.agregar(num)
    
    print("Elementos de la lista:")
    for valor in lista:
        print(valor, end=" ")
    print()
    
    print("Buscando el valor 30:", "Encontrado" if lista.buscar(30) else "No encontrado")
    
    print("Eliminando el valor 20.")
    lista.eliminar(20)
    
    print("Elementos de la lista tras la eliminación:")
    for valor in lista:
        print(valor, end=" ")
    print()
