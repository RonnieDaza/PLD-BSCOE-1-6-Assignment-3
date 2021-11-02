# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the ouput in the following format.
# You can buy __________ apples and your change is __________ pesos.

def getMoney():
    _money = int(input("Enter the amount of money: "))
    return _money

def getApple():
    _apple = int(input("Enter the price of an apple: "))
    return _apple

def getApplequantity():
    _appleQuantity = money // apple
    return _appleQuantity

def getAppleprice():
    _applePrice = appleQuantity * apple
    return _applePrice

def getMoneyleft():
    _moneyLeft = money - applePrice

# Steps
# 1. Ask for the amount of money the user have.
money = getMoney()
# 2. Ask for the price of an apple.
apple = getApple()
# 3. Define the quantity of the apple.
appleQuantity = getApplequantity()
# 4. Define the price of the apple.
applePrice = getAppleprice()
# 5. Define the remaining money that the user will have.
moneyLeft = getMoneyleft