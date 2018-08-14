class Multiselect:
    def __init__(self):
        self.ls = []
    def add(self,elem):
        self.ls.append(elem)
    def remove(self,elem):
        del self.ls[self.ls.index(elem)]
    def multiplicity(self,elem):
        return self.ls.count(elem)


m=Multiselect()
m.add(1)
m.add(1)
m.add(1)
m.add(2)
m.add(3)
m.remove(1)
print(m.multiplicity(1))
