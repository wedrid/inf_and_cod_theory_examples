import copy
class Node:
    # non faccio i getters per prob e symb, per velocità..
    def __init__(self, symb = None, prob = 0):
        self.symb = symb
        self.prob = prob
        self.parent = None
        self.children = None
        self.isRoot = False
    
    def setSymb(self, symb):
        self.symb = symb

    def setProb(self, prob):
        self.prob = prob

    def setParent(self, parent):
        self.parent = parent
     
    def setChildren(self, children):
        self.children = children
    

class Tree:
    def __init__(self, symbols, probabilities):
        self.root = None
        self.original_nodes = []
        for symb, prob in zip(symbols, probabilities):
            self.original_nodes.append( Node(symb, prob) )
        self.work_nodes = self.original_nodes

    def createParentFromSiblings(self, symbols):
        #:param symbols: a list of symbols that have a common parent (for coding alphabet of 2 characters, they are just two symbols)
        children_nodes = []
        combined_symbol = "|"
        combined_prob = 0
        parent = Node()
        for node in self.work_nodes:
            if node.symb in symbols: 
                children_nodes.append(node)
                combined_symbol += f"{node.symb}|"
                combined_prob += node.prob
                #print(combined_prob)
                print(node.symb)
                node.setParent(parent)
                self.work_nodes.remove(node)
        parent.setSymb(combined_symbol)
        parent.setProb(combined_prob)
        parent.setChildren(children_nodes)
        self.work_nodes.append(parent)

    def print_all_nodes(self):
        for node in self.work_nodes:
            print(f"{node.symb} -> p: {node.prob}")
    
    def getMin2_Nodes(self, k):
        k1_id = None
        k2_id = None
        k1_prob = 2
        k2_prob = 2
        for node in self.nodes:
            if node.prob < k1_prob:
                if node.prob < k2_prob:
                    k2_prob
        