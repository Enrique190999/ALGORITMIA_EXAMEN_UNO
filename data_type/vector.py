class Vector:
    def __init__(self):
        self.data = []  # Usamos la lista interna para almacenar los elementos
    
    def append(self, value):
        self.data.append(value)
    
    def get(self, index):
        return self.data[index]
    
    def set(self, index, value):
        self.data[index] = value
    
    def delete(self, index):
        del self.data[index]
    
    def size(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)

def demostracion():
    print("Creando un vector vacío.")
    vec = Vector()
    
    print("Insertando elementos (10, 20, 30, 40, 50):")
    for v in [10, 20, 30, 40, 50]:
        vec.append(v)
    print("Contenido del vector:", vec)
    
    print("Accediendo al elemento en posición 2:", vec.get(2))
    print("Modificando el elemento en posición 2 a 999.")
    vec.set(2, 999)
    print("Vector modificado:", vec)
    
    print("Eliminando el elemento en posición 1.")
    vec.delete(1)
    print("Vector tras eliminación:", vec)
    
    print("Tamaño del vector:", vec.size())
