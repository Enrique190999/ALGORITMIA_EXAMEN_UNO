class Diccionario:
    def __init__(self):
        self.datos = {}
    
    def agregar(self, clave, valor):
        self.datos[clave] = valor
    
    def obtener(self, clave):
        return self.datos.get(clave, None)
    
    def eliminar(self, clave):
        if clave in self.datos:
            del self.datos[clave]
    
    def __str__(self):
        return str(self.datos)

def demostracion():
    print("Creando un diccionario vacío.")
    dic = Diccionario()
    
    print("Agregando pares: ('clave1', 'valor1') y ('clave2', 'valor2')")
    dic.agregar('clave1', 'valor1')
    dic.agregar('clave2', 'valor2')
    
    print("Contenido del diccionario:", dic)
    print("Obteniendo el valor asociado a 'clave1':", dic.obtener('clave1'))
    
    print("Eliminando la clave 'clave1'.")
    dic.eliminar('clave1')
    print("Diccionario tras la eliminación:", dic)
