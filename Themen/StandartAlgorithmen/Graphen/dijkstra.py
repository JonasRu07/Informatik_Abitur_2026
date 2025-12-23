

class Edge:
    def __init__(self,
                 start:'Node',
                 ziel:'Node',
                 gewicht:int) -> None:
        self.start = start
        self.ziel = ziel
        self.gewicht = gewicht
    
class Node:
    def __init__(self, name:str) -> None:
        self.name = name
        self.edges:list[Edge,] = []
        self.abstand = float("inf")
        self.weg = []
        
    def add_nachbar(self, nachbar:'Node', gewicht):
        self.edges.append(Edge(self, nachbar, gewicht))
        
    def del_nachbar(self, nachbar:'Node'):
        edges = []
        for edge in self.edges:
            if edge.ziel != nachbar:
                edges.append(edge)
        self.edges = edges
        
    def __str__(self) -> str:
        s = f"Node {self.name} | Abstand:{self.abstand} | Weg:{self.weg} | Edges:"
        for edge in self.edges:
            s += f"\n  ->{edge.ziel.name} | Gewicht: {edge.gewicht}"
        return s

    def __repr__(self) -> str:
        return self.name
        
class Graph:
    def __init__(self) -> None:
        self.nodes:list[Node,] = []
        
    def add_edge(self, start:str, ziel:str, gewicht):
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
    
    def dijkstra(self, start:str, ziel:str):
        def node_teste_hinzufuegen(node:Node, teste:list[Node]):
            for index, test in enumerate(teste):
                if test == node:
                    break
                if test.abstand > node.abstand:
                    teste.insert(index, node)
                    break
            else:
                teste.append(node)
            
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
                if edge.ziel.abstand < aktuelle_node.abstand + edge.gewicht:
                    continue
                
                edge.ziel.abstand = aktuelle_node.abstand + edge.gewicht
                edge.ziel.weg = [*aktuelle_node.weg, edge.ziel.name]
                node_teste_hinzufuegen(edge.ziel, teste)
            getestet.append(aktuelle_node)
        return ziel_node.abstand, ziel_node.weg
                    
        
def load_gewichten_graph(graph:Graph, adj):
    for node in adj:
        graph.add_node(node[0])
    for node in adj:
        for nachbar in node[1]:
            graph.add_edge(node[0], nachbar[0], nachbar[1])
        
def main():
    G = Graph()
    
    # 2.3.5.3.3
    adj = [
        [
            'A', [('C', 20),
                  ('E',  2),
                  ('G',  9)]
        ],
        [
            'B', [('C', 1),
                  ('D', 8)]
        ],
        [
            'C', [('A', 20),
                  ('D', 10),
                  ('E', 13)]
        ],
        [
            'D', [('B',  8), 
                  ('E', 16)]
        ],
        [
            'E', [('D', 16), 
                  ('G',  0)]
        ],
        [
            'F', [('B', 3), 
                  ('D', 4), 
                  ('H', 5)]
        ],
        [
            'G', [('D', 2)]
        ],
        [
            'H', [('F', 5),
                  ('G', 7)]
        ]
    ]
    
    load_gewichten_graph(G, adj)
    
    
    print(G.dijkstra('A', 'B'))
    print(G)
    
    
if __name__ == "__main__":
    main()