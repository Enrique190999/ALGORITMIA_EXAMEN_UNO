class TablaHash:
    def __init__(self, tam=10):
        self.tam = tam
        self.tabla = [[] for _ in range(tam)]
    
    def _hash(self, clave):
        return hash(clave) % self.tam
    
    def insertar(self, clave, valor):
        indice = self._hash(clave)
        for i, (c, _) in enumerate(self.tabla[indice]):
            if c == clave:
                self.tabla[indice][i] = (clave, valor)
                return
        self.tabla[indice].append((clave, valor))
    
    def obtener(self, clave):
        indice = self._hash(clave)
        for c, v in self.tabla[indice]:
            if c == clave:
                return v
        return None
    
    def eliminar(self, clave):
        indice = self._hash(clave)
        for i, (c, _) in enumerate(self.tabla[indice]):
            if c == clave:
                del self.tabla[indice][i]
                return True
        return False

def demostracion():
    print("Creando una tabla hash de tamaño 5.")
    tabla = TablaHash(5)
    
    print("Insertando pares: ('a', 1), ('b', 2), ('c', 3)")
    tabla.insertar('a', 1)
    tabla.insertar('b', 2)
    tabla.insertar('c', 3)
    
    print("Obteniendo el valor para la clave 'b':", tabla.obtener('b'))
    
    print("Eliminando la clave 'a'.")
    tabla.eliminar('a')
    print("Obteniendo el valor para la clave 'a':", tabla.obtener('a'))
