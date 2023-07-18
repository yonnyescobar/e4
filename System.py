import Curso as cu
import DoubleList as dl
import Estudiante as es
import RegistroMatricula as rm

class System():
    def __init__(self):
        self.Students = dl.DoubleList()
        self.Registers = dl.DoubleList()
        self.Courses = dl.DoubleList()
#---------------------------------------------------------------------------------------------------
# addStudent (0.25): Agrega un nuevo estudiante evitando que se dupliquen.
    def addStudent(self, Documento, Carne, Nombres, Apellidos, Telefono, Email): 
        temp = self.findStudent(Documento)
        
        if temp == None:
            estudiante = es.Estudiante(Documento, Carne, Nombres, Apellidos, Telefono, Email)
            self.Students.addFirst(estudiante)
        else:
            print("El estudiante ya esta registrado")
#--------------------------------------------------------------------------------------------------- 
# addCourse (0.25): Agrega un nuevo curso evitando que se dupliquen.           
    def addCourse(self, Codigo, Nombre, Creditos, Quotas):
        temp = self.findCourse(Codigo)
                
        if temp == None:
            curso = cu.Curso(Codigo, Nombre, Creditos, Quotas)
            self.Courses.addFirst(curso)
        else:
            print("El curso ya existe")
#---------------------------------------------------------------------------------------------------
# addRegister (1.0): Agrega un nuevo registro de matrícula.
    # a. Un estudiante no puede matricular dos veces el mismo curso en el periodo.
    # b. Evitar que un estudiante supere los 16 créditos matriculados en el periodo.
    # c. Evitar que el curso sobrepase su cupo en el periodo.
    # d. Evitar que se matriculen cursos o estudiantes que no están registrados.
    def addRegister(self, Curso, Estudiante, Periodo, Nota=0):
        
        consultar_estudiante = self.findStudent(Estudiante)
        if consultar_estudiante == None:
            print("Error, el estudiante no existe")
            return
            
        
        consultar_cursos = self.findCourse(Curso)
        if consultar_cursos == None: 
            print("Error, el curso no existe")
            return

        consultar_creditos = self.sumCredits(Estudiante, Periodo)
        if consultar_creditos + consultar_cursos.data.Creditos > 16:
            print("Error, Se exceden los creditos")
            return
        
        consultar_cupos = self.sumQuotas(Curso, Periodo)
        if consultar_cupos + 1 > consultar_cursos.data.Quotas:
            print("Error, Se exceden los cupos")
            return
            
        
        consultar_matricula = self.findRegister(consultar_estudiante.data,consultar_cursos.data, Periodo)
        if consultar_matricula != None:
            print("Error, la matricula ya existe")
            return
                    
        matricula = rm.RegistroMatricula(consultar_estudiante.data,consultar_cursos.data , Periodo, Nota)
        self.Registers.addFirst(matricula)
#---------------------------------------------------------------------------------------------------
# findStudent (0.25): Buscar un estudiante por Documento           
    def findStudent(self, doc):
        temp = self.Students.first()
        
        while temp != None and temp.data.Documento != doc:
            temp = temp.next
            
        if temp == None:
            return None
        else:
            return temp
#---------------------------------------------------------------------------------------------------
# findCourse (0.25): Buscar un curso por Código
    def findCourse(self, cod):
        temp = self.Courses.first()
        
        while temp != None and temp.data.Codigo != cod:
            temp = temp.next
            
        if temp == None:
            return None
        else:
            return temp
#---------------------------------------------------------------------------------------------------
# findRegister (0.25): Buscar un registro de matricula por Estudiante, Curso y Periodo
    def findRegister(self, Estudiante, Curso, Periodo):
        temp = self.Registers.first()

        while temp != None:
            if temp.data.Estudiante == Estudiante and temp.data.Curso == Curso and temp.data.Periodo == Periodo:
                return temp
            temp = temp.next
    
        return None
#---------------------------------------------------------------------------------------------------
# removeStudent (0.25): Elimina un estudiante. Deben eliminarse los registros de matrícula asociados a éste.
    def removeStudent (self, doc):
        consultar_estudiante = self.findStudent(doc)

        if consultar_estudiante != None:
            self.Students.remove(consultar_estudiante)
            self.removeStudentRegisters(consultar_estudiante.data)
            return print("Se eliminó el estudiante: \n",consultar_estudiante.data)
        else:
            return None         
#---------------------------------------------------------------------------------------------------
# removeCourse (0.25): elimina un curso. Deben eliminarse los registros de matrícula asociados a éste.
    def removeCourse(self, cod):
        curso = self.findCourse(cod)

        if curso != None:
            self.Courses.remove(curso)
            self.removeCourseRegisters(curso.data)
            return print("Se eliminó el curso: \n",curso.data)
        else:
            return None      
#---------------------------------------------------------------------------------------------------
# removeRegister (0.25): elimina un registro de matrícula.
    def removeRegister(self, Estudiante, Curso, Periodo):
        consultar_registro = self.findRegister(Estudiante, Curso, Periodo)
        
        if consultar_registro != None:
            self.Registers.remove(consultar_registro)
            return consultar_registro.data
        else:
            return None
#---------------------------------------------------------------------------------------------------
# removeStudentRegisters (0.25): elimina todos los registros de matrícula asociados a un estudiante.
    def removeStudentRegisters(self, Estudiante):
        temp = self.Registers.first()
        
        while temp != None:
            if temp.data.Estudiante == Estudiante:
                temp2=temp
                temp = temp.next
                self.Registers.remove(temp2)
            else:
                temp = temp.next
#---------------------------------------------------------------------------------------------------
# removeCourseRegisters (0.25): elimina todos los registros de matrícula asociados a un curso.
    def removeCourseRegisters(self, Curso):
        temp = self.Registers.first()
        
        while temp != None:
            if temp.data.Curso == Curso:
                temp2 = temp
                temp = temp.next
                self.Registers.remove(temp2)
            else:
                temp = temp.next
#---------------------------------------------------------------------------------------------------
# sumCredits (0.25): Calcula el número de créditos matriculados por un estudiante en un periodo en específico.
    def sumCredits(self, ID, Periodo):
        temp = self.findStudent(ID)
        acumulador=0
    
        if temp == None:
            print ("Error, no se encuentra el estudiante")
        else:
            temp2 = self.Registers.first()
            while temp2 != None :
                if temp2.data.Estudiante == temp.data and temp2.data.Periodo == Periodo:
                    acumulador+=temp2.data.Curso.Creditos
                temp2=temp2.next
        return acumulador                         
#---------------------------------------------------------------------------------------------------
# sumQuotas (0.25): Calcula el número de estudiantes inscritos a un curso en un periodo en específico.
    def sumQuotas(self, Curso,Periodo):
        temp = self.findCourse(Curso)
        acumulador=0
    
        if temp == None:
            print ("Error, no se encuentra el curso")
        else:
            temp2 = self.Registers.first()
            while temp2 != None :
                if temp2.data.Curso == temp.data and temp2.data.Periodo == Periodo:
                    acumulador+=1
                temp2=temp2.next
        return acumulador   
#---------------------------------------------------------------------------------------------------
# generateReport (1.0): Genera un reporte del historial de matrícula de un estudiante. Se debe incluir:
    # a. Información del estudiante
    # b. Registros de Matrícula del estudiante ordenados por periodo.
    # c. Promedio acumulado (Indiferente al número de créditos).
    def generateReport(self, ID):
        temp = self.Registers.first()
        
        estudiante = self.findStudent(ID)
        if estudiante != None:
            print("Nombre completo: ",estudiante.data.Nombres,estudiante.data.Apellidos,
                  "\nDocumento: ",estudiante.data.Documento)
        
        else:
            print("El estudiante con documento ",ID," No tiene registros de matrícula")
     
        
#--------------------------------------------------------------------------------------------------- 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
