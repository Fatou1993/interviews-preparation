class Vertice :
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

    def changePriority(self, newP):
        self.priority = newP

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

    def __str__(self):
        return "("+str(self.priority)+","+str(self.val)+")"

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)