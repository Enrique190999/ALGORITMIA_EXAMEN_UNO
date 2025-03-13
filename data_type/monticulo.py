import heapq

class Monticulo:
    def __init__(self):
        self.data = []
    
    def insertar(self, item):
        heapq.heappush(self.data, item)
    
    def extraer_minimo(self):
        if self.data:
            return heapq.heappop(self.data)
        raise IndexError("extraer de montículo vacío")
    
    def ver_minimo(self):
        if self.data:
            return self.data[0]
        raise IndexError("montículo vacío")
    
    def size(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)

def demostracion():
    print("Creando un montículo vacío.")
    mont = Monticulo()
    
    print("Insertando elementos: 5, 3, 8, 1")
    for item in [5, 3, 8, 1]:
        mont.insertar(item)
    
    print("Contenido del montículo:", mont)
    print("Elemento mínimo actual:", mont.ver_minimo())
    
    print("Extrayendo el elemento mínimo:", mont.extraer_minimo())
    print("Montículo tras la extracción:", mont)
