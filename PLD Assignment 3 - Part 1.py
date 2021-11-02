# Create a program that will ask for name, age, and address.
# Display those details in the following format.
# Hi, my name is __________. I am __________ years old and I live in __________.

def getName():
    _name = input("Enter your name: ")
    return _name

def getAge():
    _age = int(input("Enter your age: ")
    return _age

def getAddress():
    _add = input("Enter your address: ")
    return _add

# Steps
# 1. Ask for name then save to variable.
name = getName()
# 2. Ask for age then save to variable.
age = getAge()
# 3. Ask for address then save to variable.
address = getAddress