import random
class Hat:

    houses=["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]
    @classmethod
    def sort(cls,name):
        print(name,"is in",random.choice(cls.houses))

if __name__ == '__main__':
    Hat.sort("Harry")