
from abc import ABCMeta,abstractclassmethod
class person(metaclass=ABCMeta):
    nbr=0
    def __init__(self ,name ,age , code, last_name ) :
        self.name =name
        self.age =age
        self.code =code
        self.last_name =last_name
        person.nbr+= 1
      
    
    def getName(self):
        return self.name 
      
    def getLast_name(self):
        return self.last_name


    def getAge(self):
        return self.age
      
    def getCode(self):
        return self.code
     
    def setAge(self , name):
        self.age = age

    def setLast_name(self,last_name):
        self.last_name = last_name

    def setCode(self,code):
        self.code =code

    def setName(self ,name):
        self.name =name

    @abstractclassmethod
    def equals(self):
     pass

    @abstractclassmethod
    def tostring(self):
        pass

class employee(person):
    def ___init__(self,name ,age , code, last_name,grade):
     super().__init__(self,name,age ,code ,last_name)
     self.grade= grade

    def tostring(self):
       print("name",{self.name},"last_name",{self.last_name},"age",{self.age},"code",{self.code})

    def equals(self ,code):
        return self.code == code

class student (person ):

    def ___init__(self,moyenne , name ,age , code, last_name ,niveau):
        super().__init__(name ,last_name ,age ,code)
        self.moyenne =moyenne
        self.niveau = niveau



    def tosrtring(self):
       print("name",{self.name},"last_name",{self.last_name},"age",{self.age},"code",{self.code},"moyen",{self.moyenne},"niveau",{self.niveau})

var1=employee("khadija","20","14","nassima")
print( var1.tostring())

var2=student("Fatima","jihht","17","1100","18","1bac")
print( var2.tostring())
