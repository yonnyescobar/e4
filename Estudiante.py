class Estudiante():
    def __init__(self, Documento, Carne, Nombres, Apellidos, Telefono, Email):
        self.__Documento=Documento
        self.__Carne=Carne
        self.__Nombres=Nombres
        self.__Apellidos=Apellidos
        self.__Telefono=Telefono
        self.__Email=Email
   
    @property
    def Documento(self):
        return self.__Documento

    @Documento.setter
    def Documento(self,Documento):
        self.__Documento=Documento

    @property
    def Carne(self):
        return self.__Carne

    @Carne.setter
    def Carne(self,Carne):
        self.__Carne=Carne

    @property
    def Nombres(self):
        return self.__Nombres

    @Nombres.setter
    def Nombres(self,Nombres):
        self.__Nombres=Nombres

    @property
    def Apellidos(self):
        return self.__Apellidos

    @Apellidos.setter
    def Apellidos(self,Apellidos):
        self.__Apellidos=Apellidos

    @property
    def Telefono(self):
        return self.__Telefono

    @Telefono.setter
    def Telefono(self,Telefono):
        self.__Telefono=Telefono

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self,Email):
        self.__Email=Email

    def __str__(self):
        return self.Documento+' '+self.Carne+' '+self.Nombres+' '+self.Apellidos+' '+self.Telefono+' '+self.Email

