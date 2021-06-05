class Point():
    def __init__(self, type_, virus, human):
        self.__type = type_ #typ - door/excluded/active/wall/indoor jako 0/1/2/3/4
        self.__virus = virus #ilość wirusa w danym punkcie
        self.__humans = human #liczba osób w danym punkcie

    #zmiana typu
    def ChangeType(self,new_type):
        self.__type = new_type
        
    #zmiana ilości wirusa
    def ChangeVirus(self,new_virus):
        self.__virus = new_virus

    #dodawanie wirusa
    def AddVirus(self, x):
        self.__virus += x

    #dodawanie ludzi
    def AddHuman(self, x):
        self.__humans += x

    #zwracanie ilości wirusa
    def GetVirus(self):
        return self.__virus

    #zwracanie liczby osób
    def GetHumans(self):
        return self.__humans
    
    #zwracanie typu
    def GetType(self):
        return self.__type
