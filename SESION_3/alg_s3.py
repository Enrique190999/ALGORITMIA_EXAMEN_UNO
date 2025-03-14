# # Algoritmia
# ## Práctica 3

# El objetivo de esta práctica es trabajar con los algoritmos de la mochila y dar la vuelta. 

# En el cuerpo de cada función hay una instrucción "pass", se debe sustituir por la implementación adecuada. 

# Para cada clase o función que se pide se proporcionan algunos tests. Las implementaciones deberían superar estos tests.


def dar_la_vuelta(cambio, valores_monedas):
    """
    Se recibe una cantidad de dinero y una lista de monedas. Se devuelve un generador de las monedas que se necesitan para dar ese cambio de forma que se minimice el número de monedas.

    Se han de devolver las monedas de mayor a menor valor.

    Nota: Para evitar el problema de los decimales en python se puede usar la función round() para redondear a dos decimales.
    """
    valores_monedas.sort(reverse=True)
    i=0
    while cambio > 0:
        
        for valor in valores_monedas:
            if valor <= cambio:
                yield valor
                cambio -= valor
                cambio = round(cambio,2)
                break
        '''
        if cambio >= valores_monedas[i]:
            cambio -= valores_monedas[i]
            cambio = round(cambio, 2)
            yield valores_monedas[i]
        else:
            i += 1
        '''
    pass

# Implementa dar la vuelta utilizando las recomendaciones de la diapositiva 5 de la presentación del tema 2 y comprueba si es más rápido que la implementación básica.

# optimo no es que mia lgoritmo tega la menor complegidad temporal que exista, es buscar una solución perfecta y no hay aleatoriedad
# ya sea optimo o aproximado debe de obtener siempre una solución igual (dada una entrada habrá siempre la misma salida)

# este algoritmo es aproximado porque no se puede partir
def algoritmo_mochila_voraz(objetos, peso_soportado):
    """
    Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Seleccionar las claves de los objetos cuya suma del peso no sea mayor que el peso soportado y se 
    maximice el valor usando un algoritmo voraz. Los objetos no pueden partirse.
    """
    objetos = sorted(objetos.items(), key= lambda x: x[1][1]/x[1][0], reverse=True) # lambda: dada una x retorna 
    # x es cada elemento, 1 1 valor   1 0 peso  (valor/peso)
    peso = 0
    candidatos = []
    for k, (p,v) in objetos: # peso y valor
        if peso +p <= peso_soportado:
            candidatos.append(k)
            peso += p
    return candidatos


# esto es optimo porque se puede partir
def algoritmo_mochila_voraz_partida(objetos, peso_soportado):
    """
    Se recibe un diccionario de objetos, cada elemento del diccionario es una tupla (peso, valor)
    y una variable numérica, peso_soportado.
    Cambiamso el retorno, que si no no funcionaria 
    Devolver un diccionario con cada objeto y la cantidad ddevuelta
    
    """

    candidatos = {k:0 for k in objetos}
    objetos = sorted(objetos.items(), key= lambda x: x[1][1]/x[1][0], reverse=True) # lambda: dada una x retorna 
    # x es cada elemento, 1 1 valor   1 0 peso  (valor/peso)
    peso = 0
    
    for k, (p,_) in objetos: # peso y valor
        if peso +p <= peso_soportado:
            candidatos[k] = 1
            peso += p
        else:
            candidatos[k] = (peso_soportado -peso)/p
            peso += (peso_soportado - peso)
            break
    return candidatos

