# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:18:19 2021

@author: marta
"""

import math
import folium
import webbrowser

from SearchProblemUtilities import SearchProblem, Astar
from GeoLocationsUtilities import Location, loadLocations

# File da cui caricare la mappa
MAP_FILE_PATH = "C:\\Users\\marta\\YOUniversity\\resources\\locations\\Bari.csv"

"""
Crea una mappa nella cartella corrente, dato un file .csv
"""
def saveMap(strPath):
    points = []
    streets = []
    
    points, streets = loadLocations(strPath)
    
    locationMap = folium.Map(location = [points[0].getValue().getY(), points[0].getValue().getX()], zoom_start = 15)

    for n in points:
        folium.Marker(location = [n.getValue().getY(), n.getValue().getX()], tooltip = n.getValue().getName()).add_to(locationMap)

    for a in streets:
        folium.PolyLine(locations = [(a.getFromNode().getValue().getY(), a.getFromNode().getValue().getX()), (a.getToNode().getValue().getY(), a.getToNode().getValue().getX())], color = 'red').add_to(locationMap)

    locationMap.save("mymap.html")


"""
Mostra la mappa aprendola nel browser
"""
def showMap(strPath):
    webbrowser.open_new_tab(strPath)


"""
Dati un punto di inizio e di fine, sfrutta l'algoritmo A* per risolvere il problema di ricerca tra luoghi
nello spazio della mappa del file .csv passato in input
"""
def findLocationsPath(startLocation, goalLocation, strPath):
    # Strutture dati per il problema di ricerca
    nodes = []
    arcs = []
    start = []
    goal = None

    nodes, arcs = loadLocations(strPath)

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
    sp = SearchProblem(nodes, arcs, start, goal)
    
    # Utilizza l'algoritmo A* per risolvere efficientemente il problema di ricerca
    result = Astar(sp, heur)
    
    # Crea la mappa dove visualizzare il percorso, partendo dal nodo che identifica il luogo iniziale
    resultMap = folium.Map(location = [start[0].getValue().getY(), start[0].getValue().getX()], zoom_start = 15)

    # Inserisce sulla mappa i vari Marker e Linee per indicare i luoghi e i percorsi
    rNodes = result.getNodes()
    
    # Inserisce icone specifiche per indicare il punto di partenza (in rosso) e di arrivo (in verde)
    folium.Marker(location = [rNodes[0].getValue().getY(), rNodes[0].getValue().getX()], tooltip = rNodes[0].getValue().getName(), icon=folium.Icon(color = 'red', icon = "fas fa-map-pin", prefix = "fa")).add_to(resultMap)
    folium.Marker(location = [rNodes[-1].getValue().getY(), rNodes[-1].getValue().getX()], tooltip = rNodes[-1].getValue().getName(), icon=folium.Icon(color = 'green', icon = "fas fa-flag-checkered", prefix = "fa")).add_to(resultMap)

    # Aggiunge i restanti luoghi e cammini del percorso
    for n in rNodes[1:-1]:
        folium.Marker(location = [n.getValue().getY(), n.getValue().getX()], tooltip = n.getValue().getName()).add_to(resultMap)

    for i in range(0, len(rNodes)-1):
        folium.PolyLine(locations = [(rNodes[i].getValue().getY(),rNodes[i].getValue().getX()),(rNodes[i+1].getValue().getY(),rNodes[i+1].getValue().getX())], color = 'red').add_to(resultMap) 
    
    resultMap.save("resultMap.html")
    showMap("resultMap.html")



"""
Funzione euristica utilizzata per le ricerche euristiche
Nello specifico viene usata la distanza euclidea, ottimale per calcolare 
la distanza in linea d'aria in sistemi basati su coordinate
Funzione ammissibile, non sovrastima il costo effettivo della distanza
"""
def heur(a, b):
    return math.sqrt((a.getValue().getX() - b.getValue().getX())**2 + abs(a.getValue().getY() - b.getValue().getY())**2)

   
# Esempi di utilizzo:
    
saveMap(MAP_FILE_PATH)
showMap("mymap.html")


#findLocationsPath(Location(16.872332011131505, 41.115107626544855, "Corso Benedetto Croce(1)"), Location(16.880681, 41.10796, "Politecnico/Campus-Via Edoardo Orabona"))
findLocationsPath(Location(16.87138842777386, 41.122805359113045, "Feltrinelli-Via Melo da Bari(2)"), Location(16.865199699266178, 41.10720272253909, "Viale Papa Giovanni XXIII(1)"), MAP_FILE_PATH)


