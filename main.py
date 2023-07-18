from Load import Load

try:
    sys=Load()
    print(sys.Registers.size())
    sys.removeCourse("A176")
    sys.generateReport("1011259737")
    
    print(sys.Registers.size())
    sys.removeStudent("1018045431")
    sys.generateReport("1018045431")
    print(sys.Registers.size())
    
    """
        Por Completar: 
            
        1. Matricule a los integrantes al curso de Estructuras de Datos en el periodo 2022-2
        2. Consulte el historial de uno de los integrantes.   
        
        
    """
    print("--------------------------------------------------------------------")
    print("Total actual de estudiantes: ",sys.Students.size(),"\n")
    e1 = sys.addStudent("1027880290", "21158393", "Yonny Mauricio", "Escobar Casas", "3007543343", "yonnyescobar179547@correo.itm.edu.co")
    e2 = sys.addStudent("1007273121", "20258653", "Jeiferson", "santillana giraldo,", "3122534257", "jeifersonsantillana256664@correo.itm.edu.co")
    e3 = sys.addStudent("1039475443", "21258021", "Bryan", "Arroyave Giraldo", "3014927678", "bryanarroyave315983@correo.itm.edu.co")
    e4 = sys.addStudent("1020479757", "21258347", "Andrés Felipe", "villa calderón", "3122366057", "andresvilla318095@correo.itm.edu.co")
    e5 = sys.addStudent("1000871453", "20158407", "Geraldine", "Ramirez Giraldo", "3152324426", "geraldineramirez299304@correo.itm.edu.co")
    e6 = sys.addStudent("1017276357", "22158429", "Jhon Alejandro", "Isaza Perez", "3226493521", "jhonisaza250859@correo.itm.edu.co")
    print("Se han ingresado los siguientes estudiantes: \n",sys.findStudent("1027880290").data.Nombres,"\n",
          sys.findStudent("1007273121").data.Nombres,"\n",sys.findStudent("1039475443").data.Nombres,"\n",
          sys.findStudent("1020479757").data.Nombres,"\n", sys.findStudent("1000871453").data.Nombres,"\n",
          sys.findStudent("1017276357").data.Nombres,"\n")
    print("Nuevo total de estudiantes: ",sys.Students.size())
    print("--------------------------------------------------------------------")
    print("Total actual de matriculas: ",sys.Registers.size())
    m1 = sys.addRegister("E869", "1027880290", "2022-2")
    m2 = sys.addRegister("E869", "1007273121", "2022-2")
    m3 = sys.addRegister("E869", "1039475443", "2022-2")
    m4 = sys.addRegister("E869", "1020479757", "2022-2")
    m5 = sys.addRegister("E869", "1000871453", "2022-2")
    m6 = sys.addRegister("E869", "1017276357", "2022-2")
    print("Los estudiantes ingresados se han matriculado al curso",sys.findCourse("E869").data.Nombre)
    print("Nuevo total de matriculas: ",sys.Registers.size())

except :
    print("An error has occurring while loading.")
