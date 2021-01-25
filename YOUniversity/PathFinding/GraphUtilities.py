"""
Classe che rappresenta i Nodi del Grafo
"""
class Node(object):
    
    def __init__(self, value):
        self.value = value  # valore contenuto nel nodo
        
    def getValue(self):
        return self.value
    
    def __repr__(self):
        return str(self.value)
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.value == other.getValue()
    
    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.value < other.getValue()
        
    def __le__(self, other):
        if type(self) != type(other):
            return False
        return self.value <= other.getValue()
    
    def __hash__(self):
        return hash(str(self))

    
"""    
Archi tra Nodi del Grafo
"""
class Arc(object):
    
    # Prende in input nodo di partenza, di arrivo, costo (default = 1 se non indicato), azione
    def __init__(self, fromNode, toNode, cost=1, action=None): # TODO rimuovere azione?
        assert cost >= 0, ("Il costo non può essere negativo per" +
                           str(fromNode) + "->" + str(toNode) + ", cost: " + str(cost))
        self.fromNode = fromNode
        self.toNode = toNode
        self.action = action
        self.cost = cost
        
    def getFromNode(self):
        return self.fromNode
    
    def getToNode(self):
        return self.toNode
    
    def getAction(self):
        return self.action
    
    def getCost(self):
        return self.cost
    
    # Dato un nodo di input, ritorna True se questo è coinvolto nell'arco altrimenti False
    # Per i grafi non orientati
    def hasNode(self, node):
        return ((node == self.fromNode) 
                    or (node == self.toNode))

    # Rappresentazione dell'arco, anche per stampe a video
    def __repr__(self):
        if self.cost != 1:
            return str(self.fromNode) + " --(" + str(self.cost) + ")--> " + str(self.toNode)
        else:
            return str(self.fromNode) + " --> " + str(self.toNode)

        
  
"""    
Insieme di nodi che delineano un percorso
"""
class Path(object):
    
    def __init__(self, start):
        self.path = []
        self.add(start)
        
    def add(self, state):
        self.path.append(state)
        
    def getStart(self):
        return self.path[0]
        
    def getLastNode(self):
        return self.path[-1]
    
    def getNodes(self):
        return self.path
    
    def __repr__(self):
        s = ""
        for e in self.path:
            if self.path.index(e) == (len(self.path)-1):
                s = s + "{}".format(e)
            else:
                s = s + "{} -> ".format(e)
        return s
    
    # Operatori di confronto
    def __eq__(self, other):
        return self.path == other
    
    def __lt__(self, other):
        if (len(self.path) >= len(other.getNodes())):
            return False
        
        for i in range(0, len(self.path)-1):
            if self.path[i] >= other.getNodes()[i]:
                return False

    def __le__(self, other):
        if (len(self.path) > len(other.getNodes())):
            return False
        
        for i in range(0, len(self.path)-1):
            if self.path[i] > other.getNodes()[i]:
                return False
