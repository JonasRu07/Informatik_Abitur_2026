

class Edge:
    def __init__(self,
                 start:'Node',
                 ziel:'Node') -> None:
        self.start = start
        self.ziel = ziel
    
class Node:
    def __init__(self, name:str) -> None:
        self.name = name
        self.edges:list[Edge,] = []
        self.abstand = float("inf")
        self.weg = []
        
    def add_nachbar(self, nachbar:'Node', gewicht=1):
        self.edges.append(Edge(self, nachbar))
        
    def del_nachbar(self, nachbar:'Node'):
        edges = []
        for edge in self.edges:
            if edge.ziel != nachbar:
                edges.append(edge)
        self.edges = edges
        
    def __str__(self) -> str:
        s = f"Node {self.name} | Abstand:{self.abstand} | Weg:{self.weg} | Edges:"
        for edge in self.edges:
            s += f"\n  ->{edge.ziel.name}"
        return s

    def __repr__(self) -> str:
        return self.name
        
class Graph:
    def __init__(self) -> None:
        self.nodes:list[Node,] = []
        
    def add_edge(self, start:str, ziel:str, gewicht=0):
        n_start = self.get_node(start)
        n_ziel = self.get_node(ziel)
        assert isinstance(n_start, Node), "Start-Node existiert nicht"
        assert isinstance(n_ziel, Node), "Ziel-Node existiert nicht"
        
        n_start.add_nachbar(n_ziel, gewicht)
        
    def add_node(self, name:str):
        test = self.get_node(name)
        assert test is None, f"Node {name} is schon da"
        self.nodes.append(Node(name))
        
    def del_node(self, name:str):
        node = self.get_node(name)
        if node is None: return 
        self.nodes.remove(node)
        for loc_node in self.nodes:
            loc_node.del_nachbar(node)
            
    def del_edge(self, start:str, ziel:str):
        n_start = self.get_node(start)
        n_ziel = self.get_node(ziel)
        assert isinstance(n_start, Node), "Start-Node existiert nicht"
        assert isinstance(n_ziel, Node), "Ziel-Node existiert nicht"
        n_start.del_nachbar(n_ziel)
    
    def get_node(self, node:str) -> None|Node:
        for loc_node in self.nodes:
            if loc_node.name == node:
                return loc_node
        else:
            return None
        
    def __str__(self) -> str:
        s = f"Graph:\n {len(self.nodes)} Nodes\n"
        n = ''
        for node in self.nodes:
            n += f"{node}\n"
        return s + n
    
    def moore(self, start:str, ziel:str):
        start_node = self.get_node(start)
        ziel_node = self.get_node(ziel)
        assert isinstance(start_node, Node), "Start-Node existiert nicht"
        assert isinstance(ziel_node, Node), "Ziel-Node existiert nicht"
        
        start_node.abstand = 0
        start_node.weg = [start_node.name]
        teste:list[Node] = [start_node]
        getestet = []
        while len(teste) != 0:
            print(teste)
            aktuelle_node = teste.pop(0)
            for edge in aktuelle_node.edges:
                if edge.ziel in getestet or edge.ziel in teste:
                    continue
                edge.ziel.abstand = aktuelle_node.abstand + 1
                edge.ziel.weg = [*aktuelle_node.weg, edge.ziel.name]
                teste.append(edge.ziel)
            getestet.append(aktuelle_node)
        return ziel_node.abstand, ziel_node.weg
                    
        
def load_ungewichten_graph(graph:Graph, adj):
    for node in adj:
        graph.add_node(node[0])
    for node in adj:
        for nachbar in node[1]:
            graph.add_edge(node[0], nachbar)
        
def main():
    G = Graph()
    
    # 2.3.5.3.2
    adj = [
        [
            'A', ['C', 'E', 'G']
        ],
        [
            'B', ['C', 'D']
        ],
        [
            'C', ['A', 'D', 'E']
        ],
        [
            'D', ['B', 'E']
        ],
        [
            'E', ['D', 'G']
        ],
        [
            'F', ['B', 'D', 'H']
        ],
        [
            'G', ['D']
        ],
        [
            'H', ['F', 'G']
        ]
    ]
    
    load_ungewichten_graph(G, adj)
    
    
    print(G.moore('A', 'B'))
    print(G)
    
    
if __name__ == "__main__":
    main()