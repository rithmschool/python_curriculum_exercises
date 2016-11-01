import re
import csv

def add_student(first_name):
    with open('students.txt', 'a') as file:
        file.write(first_name)

def find_student(first_name):
    with open('students.txt', 'r') as file:
        for f in file:
            if f == first_name:
                print("{} was found!".format(first_name))

def update_student(first_name,new_name):
    with open('students.txt', 'r+') as file:
        text = file.read()
        text=  re.sub(first_name, new_name, text)
        file.seek(0)
        file.write(text)
        file.truncate()

def remove_student(first_name):
    with open('students.txt', 'r+') as file:
        text = file.read()
        text=  re.sub(first_name, '', text)
        file.seek(0)
        file.write(text)
        file.truncate()


# Part 2

def print_names():
    with open('users.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("{} {}".format(row['first_name'], row['last_name']))

def add_name():
    with open('users.csv', 'a') as file:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(file, fieldnames)
        print("First name please:")
        first = input()
        print("Last name please:")
        last = input()
        writer.writerow(dict(first_name=first, last_name=last))

