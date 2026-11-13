# Proyecto01 Discretas 2

Implementación en Python de grafos dirigidos y no dirigidos sin usar librerías externas, junto con funciones para cargar grafos desde archivos de texto y verificar sus propiedades básicas.

## Archivos del repositorio

- `graph.py`: contiene las clases `UndirectedGraph` y `DirectedGraph` con todos los métodos solicitados.
- `main.py`: archivo principal donde se cargan los datos de prueba y se ejecutan las verificaciones.
- `sample.txt`: archivo de ejemplo para probar la lectura de aristas.

## Representación usada

Para representar tanto los grafos no dirigidos como los dirigidos se usó una lista de adyacencia con diccionarios anidados (`{vertice: {vecino: peso}}`). 

Se escogió esta estructura porque permite usar cualquier nombre en los vértices ya sealetras o números sin tener que mapear índices como pasaría en una matriz de adyacencia, además de guardar el peso de cada arista directamente. Para el grafo dirigido, `DirectedGraph` hereda de `UndirectedGraph` y modifica `add_edge` para guardar la conexión en un solo sentido (`source -> target`).

El proyecto está configurado con `uv`. Para correr las pruebas desde la raíz del repositorio: uv run main.py