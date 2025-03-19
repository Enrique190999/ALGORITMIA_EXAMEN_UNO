'''
Para pasar de un grafo 
grafo = {
    'a': {'b':1,'c':2},
    'b': {'a':3, 'd':6},
    ...
}

a un grafo

grafo = { ('a','b'):1,
        ('a','c'):2
        }

si el grafo es dirigido solo se indica en una direccion y no bidireccional.

Pregunta de examen

- Matriz de adyacencia kruskal

Se resuelve en una hora (15-20 mins) 5 - 6 preguntas el examen es sonre 10. vale el examen
un 13,3%

Las tuplas se ordenan en caso de empate por el primer elemento

Como se nos ocurra escribir el nombre de las variables como x, y o cosas del estilo 
no lee el codigo, el nombre de las variables tiene que ser comprensible.

3 soluciones posibles para union-pertenencia
    - asignacion por tamaño
    - asignacion por altura
    - asignacion por caminos
    - asignacion por altura y comprimimos por caminos
    
En el examen debemos sabernos las 4 opciones 
'''