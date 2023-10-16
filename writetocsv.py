import csv

if __name__ == '__main__':
    name = input("name: ")
    home = input("home: ")

    with open("students.csv", 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'home'])
        writer.writerow({'name': name, 'home': home})
