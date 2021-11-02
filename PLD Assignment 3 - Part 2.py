# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if the apple price is 20 pesos and the orange price is 25 pesos.
# Display the output in the following format.
# The total amount is __________.

def howmanyApples():
    _appleQuestion = int(input("How many apples you want to buy? "))
    return _appleQuestion

def howmanyOranges():
    _orangeQuestion = int(input("How many oranges you want to buy? "))
    return _orangeQuestion

def appleWhatisprice():
    _applePrice = 20
    return _applePrice

def orangeWhatisprice():
    _orangePrice = 25
    return _orangePrice

def appleWhatistotal():
    _appleTotal = appleQuestion * applePrice
    return _appleTotal

def orangeWhatistotal():
    _orangeTotal = orangeQuestion * orangeTotal

# Steps
# 1. Ask how many apples you want to buy then save to variable.
appleQuestion = howmanyApples
# 2. Ask how many oranges you want to buy then save to variable.
orangeQuestion = howmanyOranges
# 3. Define the price of apple.
applePrice = appleWhatisprice
# 4. Define the price of orange.
orangePrice = orangeWhatisprice
# 5. Compute the total price of apple.
appleTotal = appleWhatistotal
# 6. Compute the total price of orange.
orangeTotal = orangeWhatistotal
