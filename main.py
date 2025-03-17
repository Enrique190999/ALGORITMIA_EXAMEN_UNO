# main.py
# Este archivo principal importa cada módulo y llama a su función de demostración,
# mostrando cómo crear, insertar, eliminar, buscar, etc., en cada estructura de datos.

from data_type import vector,lista,arbol,tabla_hash,pila,cola,conjunto,diccionario,monticulo,arbol_busqueda,grafo

def main():
    
    print("=== DEMOSTRACIÓN DE VECTOR ===")
    vector.demostracion()
    '''
    print("\n=== DEMOSTRACIÓN DE LISTA ENLAZADA ===")
    lista.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE ÁRBOL BINARIO ===")
    arbol.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE TABLA HASH ===")
    tabla_hash.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE PILA ===")
    pila.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE COLA ===")
    cola.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE CONJUNTO ===")
    conjunto.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE DICCIONARIO ===")
    diccionario.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE MONTÍCULO ===")
    monticulo.demostracion()
    
    print("\n=== DEMOSTRACIÓN DE ÁRBOL DE BÚSQUEDA (BST) ===")
    arbol_busqueda.demostracion()
    '''
    print("\n=== DEMOSTRACIÓN DE GRAFO Y ALGORITMO DE KRUSKAL ===")
    grafo.demostracion()
    
if __name__ == '__main__':
    main()
