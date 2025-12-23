from random import randint, seed
seed(0)


class Edge:
    def __init__(self,
                 start:'Node',
                 ziel:'Node',
                 gewicht:int|float) -> None:
        self.start = start
        self.ziel = ziel
        self.gewicht = gewicht

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return f"Edge: {self.start.name} -> {self.ziel.name} : {self.gewicht}"
    
class Node:
    def __init__(self, name:str) -> None:
        self.name = name
        self.edges:list[Edge,] = []
        
    def add_nachbar(self, nachbar:'Node', gewicht):
        self.edges.append(Edge(self, nachbar, gewicht))
        
    def del_nachbar(self, nachbar:'Node'):
        edges = []
        for edge in self.edges:
            if edge.ziel != nachbar:
                edges.append(edge)
        self.edges = edges
        
    def __str__(self) -> str:
        s = f"Node {self.name} | Edges:"
        for edge in self.edges:
            s += f"\n  ->{edge.ziel.name} | Gewicht: {edge.gewicht}"
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
        
    def get_edge(self, start:str, ziel:str) -> Edge|None:
        n_start = self.get_node(start)
        n_ziel = self.get_node(ziel)
        assert isinstance(n_start, Node), "Start-Node existiert nicht"
        assert isinstance(n_ziel, Node), "Ziel-Node existiert nicht"
        
        for edge in n_start.edges:
            if edge.ziel == n_ziel:
                return edge
        return None
        
    def __str__(self) -> str:
        s = f"Graph:\n {len(self.nodes)} Nodes\n"
        n = ''
        for node in self.nodes:
            n += f"{node}\n"
        return s + n
    
    def rekursive_loesung(self, weg=None, rest=None, bester_weg=([], float("inf"))):
        if rest is None: 
            rest = self.nodes.copy()
            
        if weg is None:
            weg = [rest.pop(0)]
        
        if len(rest) == 0:
            weg.append(weg[0])
            laenge = 0
            for idx in range(len(weg)-1):
                edge = self.get_edge(weg[idx].name, weg[idx+1].name)
                if edge is None: continue
                laenge += edge.gewicht
            # laenge += self.get_edge(weg[-1].name, weg[0].name).gewicht
            return weg, laenge
        
        for idx, kante in enumerate(rest):
            tmp_weg = self.rekursive_loesung(weg + [rest[idx]], rest[:idx] + rest[idx+1:], bester_weg)
            if tmp_weg[1]< bester_weg[1]:
                bester_weg = tmp_weg
        return bester_weg
        
    def naechste_Node(self):
        rest = self.nodes.copy()
        weg = [rest.pop(randint(0, len(rest)-1))]
        laenge = 0
        while len(rest) != 0:
            min_edge, min_gewicht = None, float("inf")
            for node in rest:
                edge = self.get_edge(weg[0].name, node.name)
                if edge is None: continue
                if edge.gewicht < min_gewicht: 
                    min_edge = edge
                    min_gewicht = edge.gewicht
            if min_edge is not None:
                weg.append(min_edge.ziel)
                rest.remove(min_edge.ziel)
                laenge += min_edge.gewicht
        weg.append(weg[0])
        laenge += self.get_edge(weg[-1].name, weg[0].name).gewicht
        return weg, laenge
        
    def entfernteste_node(self):
        rest = self.nodes.copy()
        weg = [rest.pop(0)]*2
        
        for i in range(len(rest)):
            max_distanz, max_node = float("inf"), None
            # Entfernteste Node finden
            for ziel_node in rest:
                for start_node in weg[1:]:
                    edge = self.get_edge(start_node.name, ziel_node.name)
                    if edge is None: continue
                    if edge.gewicht > max_distanz:
                        max_distanz = edge.gewicht
                        max_node = ziel_node
            # Node einfuegen
            if max_node is None: continue
            min_distanz, min_weg = float("inf"), []
            for j in range(len(weg)-1):
                tmp_weg = weg[:j] + [max_node] + weg[j:]
                if sum([self.get_edge(tmp_weg[k].name, tmp_weg[k%len(tmp_weg)].name).gewicht for k in range(len(tmp_weg))]) < min_distanz:
                    min_distanz = sum([self.get_edge(tmp_weg[k].name, tmp_weg[k%len(tmp_weg)].name).gewicht for k in range(len(tmp_weg))])
                    min_weg = tmp_weg
            weg = min_weg
        return weg, sum([self.get_edge(weg[k].name, weg[k%len(weg)].name).gewicht for k in range(len(weg))])
        
    def load_adj_matrix(self, names:list[str], matrix:list[list[int]]):
        for name in names:
            self.add_node(name)
        
        for idx_start, kanten in enumerate(matrix):
            for idx_ziel, gewicht in enumerate(kanten):
                self.add_edge(names[idx_start], names[idx_ziel], gewicht)
    
def main():
    G = Graph()
    
    # AB "Rundreise in Graphen"
    
    namen = ["Bonn", "Paris", "Rom", "Den Haag", "Bruessel", "Luxenburg"]
    
    M = [
        # Bonn | Paris | Rom | Den Haag | Bruessel | Luxenburg
        [    0,    401, 1066,       244,       195,        145],
        [  401,      0, 1108,       383,       262,        287],
        [ 1066,   1108,    0,      1289,      1174,        989],
        [  245,    383, 1289,         0,       137,        302],
        [  195,    262, 1174,       137,         0,        187],
        [  145,    287,  989,       302,       187,          0]
    ]
    
    G.load_adj_matrix(namen, M)
    
    # print(G)
    
    print(G.rekursive_loesung())
    print(G.naechste_Node())
    
    
    
if __name__ == "__main__":
    main()