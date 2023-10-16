class Wizard:
    def __init__(self,name,patronus):
        if not name:
            raise ValueError("Missing name")
        self.name=name
        self.patronus=patronus

class Student(Wizard):
    def __init__(self,name,house,patronus):
        super().__init__(name,patronus)
        self.house=house

    def __str__(self):
        return f"{self.name} from {self.house} with {self.patronus}"

    @classmethod
    def get(cls):
        name=input("Name: ")
        house=input("House: ")
        return cls(name,house)

class Professor(Wizard):
    def __init__(self,name,subject,patronus):
        super().__init__(name,patronus)
        self.subject=subject
    def __str__(self):
        return f"{self.name} from {self.subject} with {self.patronus}"

    @classmethod
    def get(cls):
        name=input("Name: ")
        subject=input("Subject: ")
        patronus=input("Patronus: ")
        return cls(name,subject)
def main():
    #wizard=Wizard("Albus")  #only wizard __init__ method is called
    student=Student.get()   #__init__ of both student and wizard is called
    print(student)
    professor=Professor.get()  #__init__ of both professor and wizard
    print(professor)

if __name__ == '__main__':
    main()