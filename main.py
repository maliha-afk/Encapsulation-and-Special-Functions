class employee:
    def __init__(self,name,salary):
        self.__name=name
        self.salary=salary
    def getname(self):
        print(f"employee name: {self.__name}")     

    def setname(self,newname):
        self.__name = newname
        print("name updated succesfully!")
employee1=employee("rahul",3000)
employee1.getname()
employee1.setname("atiya")
employee1.getname()
