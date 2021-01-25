# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 12:21:36 2021

@author: marta
"""
import heapq
from copy import deepcopy
from GraphUtilities import Path

"""
Classe che identifica un problema di ricerca generico.
E' definito come un modello astratto indipendente dal particolare dominio,
riconducendo il problema ad un grafo, con un insieme di nodi connessi da archi, 
nel quale bisogna trovare un percorso tra un nodo di partenza e uno obiettivo.
"""
class SearchProblem(object):
    
    # Prende in input l'insieme di stati (nodi), l'insieme di archi, l'insieme dei nodi di partenza e un singolo nodo obiettivo
    def __init__(self, states, arcs, start, goal):
        self.states = states
        self.arcs = arcs
        self.start = start
        self.goal = goal
        
    def isGoal(self, state):
        return state == self.goal
    
    def getStates(self):
        return self.states
    
    def getArcs(self):
        return self.arcs
    
    def getStart(self):
        return self.start
    
    def getGoal(self):
        return self.goal
    
    def __repr__(self):
        s = "Problema di Ricerca:\nStati/Nodi: "
        for state in self.states:
            s = s + str(state) + " "
        s = s + "\nArchi: "
        for arc in self.arcs:
            s = s + str(arc) + " "
        s = s + "\nNodi di Partenza: " + str(self.start)
        s = s + "\nNodo obiettivo: "
        s = s + str(self.goal) + " "
        s = s + "\n"
        return s
    
    
"""
Frontiera per l'algoritmo A*
Implementata con una coda con priorità (heap) che memorizza costo e percorso associato.
La coda con priorità ritornerà sempre l'elemento con costo minore presente in quel momento nella Frontiera.
"""
class AstarFrontier(object):
    
    def __init__(self):
        self.frontierpq = []  # Struttura dati

    def empty(self):
        return self.frontierpq == []

    # Aggiunge un percorso con il costo associato alla frontiera
    def add(self, path, cost):
        heapq.heappush(self.frontierpq, (cost, path))

    # Restituisce il percorso con costo minimo, rimuovendolo dalla frontiera
    def pop(self):
        return heapq.heappop(self.frontierpq)

    # Ritorna la lunghezza della frontiera
    def __len__(self):
        return len(self.frontierpq)
    
    def __repr__(self):
        return "".join(str(["Costo: {}, Path: ({})".format(c, p) for (c, p) in self.frontierpq]))

    # Permette di iterare sulla frontiera
    def __iter__(self):
        for (_, p) in self.frontierpq:
            yield p
 
           
"""
Funzione che implementa l'algoritmo A* per un problema di ricerca
Prende in input un problema di ricerca e la funzione euristica per stimare il costo
del percorso da un nodo all'obiettivo
"""
def Astar(sProb, heuristic):
    
    goal = sProb.getGoal()
    
    # Inizialmente si conoscono solo i nodi di partenza
    openSet = AstarFrontier()
    for nStart in sProb.getStart():
       openSet.add(Path(nStart), heuristic(nStart, goal))
        
    # Per un nodo n, cameFrom[n] è il nodo che lo precede nel path di costo minimo
    # da un nodo di partenza all'n corrente
    cameFrom = {}
    
    # Per un nodo n, gScore[n] è il costo effettivo del percorso da un nodo di partenza all'n corrente
    gScore = {}
    for path in openSet:
        gScore[path.getLastNode()] = 0 # Il costo del percorso da un nodo di partenza a se stesso è 0
        
    # Per un nodo n, fScore[n] = gScore[n] + heuristic(n)
    # ovvero il costo effettivo del percorso da un nodo di partenza al nodo n corrente
    # più una stima, basata sulla funzione euristica data in input, del costo del percorso da n al nodo obiettivo
    fScore = {}
    for path in openSet:
        n = path.getLastNode()
        fScore[n] = heuristic(n, goal)
        
    while len(openSet) != 0:
        
        # O(1) con coda con priorità/minheap
        currentCost, currentPath = openSet.pop()  # Restituisce il Path con costo minore e lo rimuove dalla frontiera
        current = currentPath.getLastNode() # Restituisce l'ultimo nodo del percorso
        
        # Se il nodo finale del percorso è un nodo obiettivo, restituiamo il percorso
        if sProb.isGoal(current):
            return currentPath

        # Per ogni nodo cerchiamo gli archi in cui è presente (come nodo di partenza o arrivo)
        for a in sProb.getArcs():
            if (a.hasNode(current)):
                
                # A seconda che il nodo corrente sia di partenza o arrivo, prende il suo vicino
                if a.getFromNode() == current:
                    neighbor = a.getToNode() 
                elif a.getToNode() == current:
                    neighbor = a.getFromNode()
                
                # Costo del percorso da un nodo di partenza fino a current + costo di arco <current, neighbor>
                tentative_gScore = gScore[current] + a.getCost() 
                
                # Se già esaminato, prende il costo del percorso già esaminato fino a neighbor
                # altrimenti mette un valore molto grande/infinito
                neighbor_gScore = gScore[neighbor] if (neighbor in gScore) else 50000
                
                if tentative_gScore < neighbor_gScore:
                    # il percorso trovato fino al neighbor è migliore di quello precedentemente esaminato
                    # lo salviamo
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    
                    fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, goal)
                    
                    newPath = deepcopy(currentPath)
                    newPath.add(neighbor)
                    
                    if newPath not in openSet:
                        openSet.add(newPath, fScore[neighbor])
                        
    return None # non è stato trovato alcun percorso