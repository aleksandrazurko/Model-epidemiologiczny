class Point():
    def __init__(self, type_, virus, human):
        self.__type = type_
        self.__virus = virus
        self.__humans = human
    
    def ChangeType(self,new_type):
        self.__type = new_type
        
    def ChangeVirus(self,new_virus):
        self.__virus = new_virus

    def AddVirus(self, x):
        self.__virus += x

    def AddHuman(self, x):
        self.__humans += x

    def GetVirus(self):
        return self.__virus

    def GetHumans(self):
        return self.__humans

    
