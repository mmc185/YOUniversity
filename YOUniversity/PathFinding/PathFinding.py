# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:18:19 2021

@author: marta
"""

import math
import folium
import webbrowser

from GraphUtilities import Node, Arc, Path
from SearchProblemUtilities import AstarFrontier, SearchProblem, Astar
from GeoLocationsUtilities import Location, loadLocations

# File da cui caricare la mappa
MAP_FILE_PATH = "C:\\Users\\marta\\YOUniversity\\resources\\locations\\Bari.csv"

"""
Crea una mappa nella cartella corrente
"""
def saveMap(strPath):
    points = []
    streets = []
    
    points, streets = loadLocations(strPath)
    
    bariMap = folium.Map(location = [points[0].getValue().getY(), points[0].getValue().getX()], zoom_start = 15)

    for n in points:
        folium.Marker(location = [n.getValue().getY(), n.getValue().getX()], tooltip = n.getValue().getName()).add_to(bariMap)

    for a in streets:
        folium.PolyLine(locations = [(a.getFromNode().getValue().getY(), a.getFromNode().getValue().getX()), (a.getToNode().getValue().getY(), a.getToNode().getValue().getX())], color = 'red').add_to(bariMap)

    bariMap.save("mymap.html")

"""
Mostra la mappa aprendola nel browser
"""
def showMap(strPath):
    webbrowser.open_new_tab(strPath)

"""
Dati un punto di inizio e di fine, sfrutta l'algoritmo A* per risolvere il problema di ricerca tra luoghi
"""
def findLocationsPath(startLocation, goalLocation):
    # Strutture dati per il problema di ricerca
    nodes = []
    arcs = []
    start = []
    goal = None

    nodes, arcs = loadLocations("C:\\Users\\marta\\YOUniversity\\resources\\locations\\Bari.csv")

    for n in nodes:
        # Se le coordinate coincidono con il luogo di partenza dato in input, lo salva nella struttura dati apposita
        # Controllo in più per assicurarsi che sia unico, se trovato
        if n.getValue().getX() == startLocation.getX() and n.getValue().getY() == startLocation.getY() and not start:
            start.append(n)
        # Se le coordinate coincidono con il luogo di arrivo dato in input, lo salva nella variabile
        # Controllo in più per assicurarsi che sia unico, se trovato
        if n.getValue().getX() == goalLocation.getX() and n.getValue().getY() == goalLocation.getY() and goal == None:
            goal = n
            
    print("Calcolando percorso da ", startLocation.getName(), " a ", goalLocation.getName())
    
    # Crea un problema di ricerca con i nostri dati
    spBari = SearchProblem(nodes, arcs, start, goal)
    
    # Utilizza l'algoritmo A* per risolvere efficientemente il problema di ricerca
    result = Astar(spBari, heur)
    print("Result: ", result) # stampa di debug
    
    # Crea la mappa dove visualizzare il percorso, partendo dal nodo che identifica il luogo iniziale
    resultMap = folium.Map(location = [start[0].getValue().getY(), start[0].getValue().getX()], zoom_start = 15)

    # Inserisce sulla mappa i vari Marker e Linee per indicare i luoghi e i percorsi
    rNodes = result.getNodes()
    for n in rNodes:
        folium.Marker(location = [n.getValue().getY(), n.getValue().getX()], tooltip = n.getValue().getName()).add_to(resultMap)

    for i in range(0, len(rNodes)-1):
        folium.PolyLine(locations = [(rNodes[i].getValue().getY(),rNodes[i].getValue().getX()),(rNodes[i+1].getValue().getY(),rNodes[i+1].getValue().getX())], color = 'red').add_to(resultMap) 
    
    resultMap.save("resultMap.html")
    showMap("resultMap.html")
    
"""
Funzione euristica utilizzata per le ricerche euristiche
"""
def heur(a, b):
    print("distanza: ")
    return math.sqrt((a.getValue().getX() - b.getValue().getX())**2 + abs(a.getValue().getY() - b.getValue().getY())**2)
    #print("norma2: ")
    #return (a.getValue().getX()*b.getValue().getX() + a.getValue().getY()*b.getValue().getY())/(math.sqrt(a.getValue().getX()**2 + a.getValue().getY()**2) * math.sqrt((b.getValue().getX()**2 + b.getValue().getY()**2)))
    #print("dijkstra: ")
    #return 0 # == dijkstra

   
# Esempi di utilizzo:
    
saveMap(MAP_FILE_PATH)
showMap("mymap.html")

findLocationsPath(Location(16.872332011131505, 41.115107626544855, "Corso Benedetto Croce(1)"), Location(16.880681, 41.10796, "Politecnico/Campus-Via Edoardo Orabona"))

