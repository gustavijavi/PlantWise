#classes
class Plant:
    def __init__(self,name,hum,temp):
        self.name=name
        self.hum=hum
        self.temp=temp
    def getName(self):
        return self.name
    def getH(self):
        return self.hum
    def getT(self):
        return self.temp
    def Display(self):
        print(self.name,"H:",self.hum,"T",self.temp)

class Collection:
    def __init__(self):
        self.garden=[]

    def getAll(self):
        return self.garden

    def getOne(self, _name):
        for i in self.garden:
            if i.getName==_name:
                return i

    def addPlant(self, _plant):
        self.garden.append(_plant)

    def DisplayAll(self):
        for i in self.garden:
            i.Display()

   #hardware:
