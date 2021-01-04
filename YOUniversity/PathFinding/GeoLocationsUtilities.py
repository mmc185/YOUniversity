# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:40:20 2021

@author: marta
"""

import pandas as pd

"""
Classe che identifica un luogo sulla mappa
Contiene le coordinate (latitudine e longitudine) (in quest'ordine???)
e il nome del luogo
"""
class Location(object):
    
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getName(self):
        return self.name
    
    def __repr__(self):
        return str(self.name)
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if (self.x == other.x):
            print("trueX")
            print(self.name, " ", other.name)
            print(self.name == other.name)
        if (self.y == other.y):
            print("trueY")
        return (self.name == other.name) and (self.x == other.x) and (self.y == other.y)
    
    def __hash__(self):
        return hash(str(self))
    

#C:\\Users\\marta\\Downloads\\map\\roads.csv
# Funzione per caricare i luoghi da file .csv
def loadLocations(strPath):
    locs = []
    locs_csv = pd.read_csv(strPath)
    locs_csv["name"].fillna("Unnamed", inplace = True)
    
    for i, l in locs_csv.iterrows():
        locs.append(Location(l["X"], l["Y"], l["name"]))
    
    return locs

l1 = loadLocations("C:\\Users\\marta\\Downloads\\map\\roads.csv")