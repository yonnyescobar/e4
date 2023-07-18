from System import System
global sys
sys=System() 

def Load():
    loadStudents()
    loadCourses()
    loadRegisters()
    return sys

def loadStudents():
    file_estudiantes=open("Estudiantes.csv","r")
    
    eLine=file_estudiantes.readline()
    eLine=file_estudiantes.readline()
    
    while eLine!="":
        eData=eLine.split(";")
        sys.addStudent(eData[0], eData[1], eData[3], eData[2], eData[4], eData[5][:-1])
        eLine=file_estudiantes.readline()
    
    file_estudiantes.close()

def loadCourses():    
        
    file_cursos=open("Cursos.csv","r")
        
    cLine=file_cursos.readline()
    cLine=file_cursos.readline()
    
    while cLine!="":
        cData=cLine.split(";")
        sys.addCourse(cData[0], cData[1], int(cData[2]),int(cData[3]))
        cLine=file_cursos.readline()
    
    file_cursos.close()

def loadRegisters():
    
    file_registros=open("RegistrosMatricula.csv","r")
        
    cLine=file_registros.readline()
    cLine=file_registros.readline()
    while cLine!="":
        rData=cLine.split(";")
        sys.addRegister(rData[0], rData[1], rData[2], float(rData[3][:-1].replace(",", ".")))
        cLine=file_registros.readline()
    
    file_registros.close()
    
    