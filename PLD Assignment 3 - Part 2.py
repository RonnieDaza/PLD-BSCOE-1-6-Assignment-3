# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if the apple price is 20 pesos and the orange price is 25 pesos.
# Display the output in the following format.
# The total amount is __________.

def getApple():
    _appleQuestion = int(input("How many apples you want to buy? "))
    return _appleQuestion

def getOrange():
    _orangeQuestion = int(input("How many oranges you want to buy? "))
    return _orangeQuestion

def getAppleprice():
    _applePrice = 20
    return _applePrice

def getOrangeprice():
    _orangePrice = 25
    return _orangePrice

def getAppletotal():
    _appleTotal = getApple * getAppleprice
    return _appleTotal

def getOrangetotal():
    _orangeTotal = getOrange * getOrangeprice
    return _orangeTotal

def getTotal():
    _total = getOrangetotal + getAppletotal
    return _total

def display(totalF):
    print(f"The total amount is {totalF}.")

# Steps
# 1. Ask how many apples you want to buy then save to variable.
appleQuestion = getApple
# 2. Ask how many oranges you want to buy then save to variable.
orangeQuestion = getOrange
# 3. Define the price of apple.
applePrice = getAppleprice
# 4. Define the price of orange.
orangePrice = getOrangeprice
# 5. Compute the total price of apple.
appleTotal = getAppletotal
# 6. Compute the total price of orange.
orangeTotal = getOrangetotal
# 7. Compute the grand total price of apple and orange.
total = getTotal
# 8. Display the output.
display(total)