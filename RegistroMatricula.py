class RegistroMatricula():
    def __init__(self, Estudiante, Curso, Periodo, Nota):
        self.__Estudiante=Estudiante
        self.__Curso=Curso
        self.__Periodo=Periodo
        self.__Nota=Nota

    @property
    def Estudiante(self):
        return self.__Estudiante

    @Estudiante.setter
    def Estudiante(self,Estudiante):
        self.__Estudiante=Estudiante

    @property
    def Curso(self):
        return self.__Curso

    @Curso.setter
    def Curso(self,Curso):
        self.__Curso=Curso

    @property
    def Periodo(self):
        return self.__Periodo

    @Periodo.setter
    def Periodo(self,Periodo):
        self.__Periodo=Periodo

    @property
    def Nota(self):
        return self.__Nota

    @Nota.setter
    def Nota(self,Nota):
        self.__Nota=Nota

    def __str__(self):
        return str(self.Estudiante.Documento)+' '+str(self.Curso)+' '+self.Periodo+' '+str(self.Nota)

