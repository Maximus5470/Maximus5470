class Student:
    def __init__(self,name,house):
        self.name=name      #getter name name
        self.house=house    #getter house name

    def __str__(self):  #similar to display function in java
        return f"{self.name}'s from {self.house}"

    @classmethod
    def get(cls):
        name=input("Name: ")
        house=input("House: ")
        return cls(name,house)

    @property   #fancy way of mentioning getter
    def house(self):
        return self._house

    @house.setter   #fancy way of mentioning setter
    def house(self,house):
        if house not in ["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house=house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:    # similar to name==""
            raise ValueError("Missing name")
        self._name=name
def main():
    student = Student.get()
    print(student)

if __name__ == '__main__':
    main()
"""def get_student():
    # student=Student()
    # student.name=input("Enter name: ")
    # student.house=input("Enter house: ")
    name=input("Enter name: ")
    house=input("Enter house: ")
    student=Student(name,house)
    return student
"""