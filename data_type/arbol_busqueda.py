class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoBST(valor)
        else:
            self._insertar(self.raiz, valor)
    
    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(valor)
            else:
                self._insertar(nodo.derecha, valor)
    
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)
    
    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)
    
    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
    
    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

def demostracion():
    print("Creando un BST (Árbol de Búsqueda) vacío.")
    bst = BST()
    
    print("Insertando elementos: 50, 30, 70, 20, 40, 60, 80")
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        bst.insertar(valor)
    
    print("Recorrido inorden del BST (debe aparecer ordenado):")
    print(bst.inorden())
    
    print("Buscando el valor 60:", "Encontrado" if bst.buscar(60) else "No encontrado")
    print("Buscando el valor 100:", "Encontrado" if bst.buscar(100) else "No encontrado")
