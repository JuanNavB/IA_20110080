grafo  = {          #se declara el grafo.
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visitado = [] #se declara la lista.
fila = []     #se inicia la fila o cola.

def bfs(visitado, grafo, nodo):
  visitado.append(nodo)
  fila.append(nodo)

  while fila:
    s = fila.pop(0) 
    print (s, end = " ") 

    for neighbour in grafo[s]:
      if neighbour not in visitado:
        visitado.append(neighbour)
        fila.append(neighbour)

# Muestra
bfs(visitado, grafo, 'B')