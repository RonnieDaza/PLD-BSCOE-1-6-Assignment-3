# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the ouput in the following format.
# You can buy __________ apples and your change is __________ pesos.

def getMoney():
    _money = int(input("Enter the amount of money: "))
    return _money

# Steps
# 1. Ask for the amount of money the user have.
money = getMoney()