"""
Classe che rappresenta i Nodi del Grafo
"""
class Node(object):
    
    def __init__(self, value):
        self.value = value  # valore contenuto nel nodo
        
    def __repr__(self):
        return str(self.value)
    
    def getValue(self):
        return self.value

    
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
    
    """
    def hasNode(self, node):
        return ((node == self.from_node) 
                    or (node == self.to_node))
    """

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
        
    def getStart(self):
        return self.path[0]
        
    def getLastNode(self):
        return self.path[-1]
    
    def __str__(self):
        s = ""
        for e in self.path:
            if self.path.index(e) == (len(self.path)-1):
                s = s + "{}".format(e)
            else:
                s = s + "{} -> ".format(e)
        return s
    
    def add(self, state):
        self.path.append(state)
        


"""
p = Path(State(3))
print(p.getStart())
print(p.getLastNode())
p.add(State(4))
p.add(State(11))
print(p.getStart())
print(p.getLastNode())
print(p.__str__())
"""      
    
n0 = Node(3)
n1 = Node(8)
print(n0)
print(n1)

a = Arc(n0, n1)
print(a)

n2 = Node(7)
a2 = Arc(n0, n2, 10)
print(a2)        