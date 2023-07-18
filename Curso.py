class Curso():
    def __init__(self, Codigo, Nombre, Creditos, Quotas):
        self.__Codigo=Codigo
        self.__Nombre=Nombre
        self.__Creditos=Creditos
        self.__Quotas=Quotas

    @property
    def Codigo(self):
        return self.__Codigo

    @Codigo.setter
    def Codigo(self,Codigo):
        self.__Codigo=Codigo

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self,Nombre):
        self.__Nombre=Nombre

    @property
    def Creditos(self):
        return self.__Creditos

    @Creditos.setter
    def Creditos(self,Creditos):
        self.__Creditos=Creditos
    
    @property
    def Quotas(self):
        return self.__Quotas

    @Quotas.setter
    def Quotas(self,Quotas):
        self.__Quotas=Quotas
    
    def __str__(self):
        return self.Codigo+' '+self.Nombre+' '+str(self.Creditos)



