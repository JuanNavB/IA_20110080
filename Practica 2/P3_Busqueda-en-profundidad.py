grafo  = {          #se declara el grafo.
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visitado = set() #se declara la lista.

def dfs(visitado, grafo, nodo): #Se declara la función DFS
  if nodo not in visitado:
    print(nodo)
    visitado.add(nodo)
    for neighbour in grafo[nodo]:
        dfs(visitado, grafo, neighbour)



print("La busqueda a profundidad es:")
dfs(visitado, grafo, 'F')