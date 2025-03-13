class Pila:
    def __init__(self):
        self.elementos = []
    
    def push(self, item):
        self.elementos.append(item)
    
    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        raise IndexError("pop from empty stack")
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.elementos)

def demostracion():
    print("Creando una pila vacía.")
    pila = Pila()
    
    print("Apilando elementos: 10, 20, 30")
    pila.push(10)
    pila.push(20)
    pila.push(30)
    
    print("Elemento en el tope (peek):", pila.peek())
    print("Extrayendo (pop):", pila.pop())
    print("Tamaño actual de la pila:", pila.size())
