class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz_valor):
        self.raiz = NodoArbol(raiz_valor)
    
    def insertar(self, valor):
        self._insertar(self.raiz, valor)
    
    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar(nodo.derecha, valor)
    
    def recorrido_inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado
    
    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

def demostracion():
    print("Creando un árbol binario con raíz 50.")
    arbol = ArbolBinario(50)
    
    print("Insertando valores: 30, 70, 20, 40, 60, 80")
    for valor in [30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)
    
    print("Recorrido inorden (resultado ordenado):")
    print(arbol.recorrido_inorden())
