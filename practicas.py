"""Solución del laboratorio formativo: grafos en Python.

Decisión: agregar_arista lanza ValueError si alguno de los vértices no existe;
primero deben agregarse explícitamente con agregar_vertice.
"""


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "E"],
    "E": ["B", "D", "F"],
    "F": ["C", "E"],
}


def contar_vertices(grafo):
    """Devuelve la cantidad de vértices del grafo."""
    return len(grafo)


def contar_aristas(grafo):
    """Cuenta las aristas no dirigidas registradas en ambos extremos."""
    return sum(len(vecinos) for vecinos in grafo.values()) // 2


def estan_conectados(grafo, origen, destino):
    """Indica si existe una arista directa entre dos vértices existentes."""
    if origen not in grafo or destino not in grafo:
        return False
    return destino in grafo[origen]


def agregar_vertice(grafo, vertice):
    """Agrega un vértice vacío si todavía no existe."""
    if vertice in grafo:
        return False
    grafo[vertice] = []
    return True


def agregar_arista(grafo, origen, destino):
    """Agrega una arista no dirigida sin duplicados ni lazos."""
    if origen not in grafo or destino not in grafo:
        raise ValueError("Los dos vértices deben existir antes de agregar la arista.")
    if origen == destino:
        return False
    if destino in grafo[origen] and origen in grafo[destino]:
        return False

    if destino not in grafo[origen]:
        grafo[origen].append(destino)
    if origen not in grafo[destino]:
        grafo[destino].append(origen)
    return True


def recorrido_amplitud(grafo, inicio):
    """Devuelve el recorrido en amplitud, conservando el orden de vecinos."""
    if inicio not in grafo:
        return []

    cola = [inicio]
    visitados = []

    while cola:
        actual = cola.pop(0)
        if actual not in visitados:
            visitados.append(actual)
            for vecino in grafo[actual]:
                if vecino in grafo and vecino not in visitados and vecino not in cola:
                    cola.append(vecino)

    return visitados


def existe_ruta(grafo, origen, destino):
    """Indica si hay un camino entre dos vértices, incluso si son iguales."""
    if origen not in grafo or destino not in grafo:
        return False
    if origen == destino:
        return True

    cola = [origen]
    visitados = [origen]

    while cola:
        actual = cola.pop(0)
        for vecino in grafo[actual]:
            if vecino == destino:
                return True
            if vecino in grafo and vecino not in visitados:
                visitados.append(vecino)
                cola.append(vecino)

    return False


if __name__ == "__main__":
    print(f"Vértices: {contar_vertices(grafo)}")
    print(f"Aristas: {contar_aristas(grafo)}")
    print(f"A y B: {estan_conectados(grafo, 'A', 'B')}")
    print(f"A y F: {estan_conectados(grafo, 'A', 'F')}")
    print(f"X y A: {estan_conectados(grafo, 'X', 'A')}")
    print(f"Recorrido desde A: {recorrido_amplitud(grafo, 'A')}")
    print(f"Ruta de A hasta F: {existe_ruta(grafo, 'A', 'F')}")
    print(f"Ruta de A hasta A: {existe_ruta(grafo, 'A', 'A')}")
    print(f"Ruta de A hasta X: {existe_ruta(grafo, 'A', 'X')}")

    agregar_vertice(grafo, "G")
    agregar_arista(grafo, "F", "G")
    print(f"Vecinos de F: {grafo['F']}")
    print(f"Vecinos de G: {grafo['G']}")

    print(
        "Reflexión: representar cada arista en los dos extremos facilita "
        "consultar vecinos, pero obliga a mantener ambas listas sincronizadas. "
        "Los recorridos con visitados evitan repetir nodos y permiten terminar "
        "aunque el grafo tenga ciclos."
    )