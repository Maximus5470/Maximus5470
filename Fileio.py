'''if __name__ == '__main__':
    names = []
    with open("names.txt", 'r') as file:
        for line in file:
            names.append(line.rstrip())
        for i in sorted(names, reverse=True):
            print(f"hello {i}")
'''
import csv

if __name__ == '__main__':
    students = []
    with open("Students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})

    for student in sorted(students, key=lambda i: i["name"]):
        print(f"{student["name"]} is from {student["home"]}")
