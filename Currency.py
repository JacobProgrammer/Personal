"""
This program converts dollars alternate currencies

Author: Jacob Olshanskiy
Date: 3-16-22
"""
money = eval(input("Enter amount of money in dollars"))
print("The value of money in euros is", money // 1.20, "dollars")
print("The value in yen is", money // 0.0084, "dollars")
print("The value in rubles is", money // 0.00998610, "dollars")
print("The value in pesos is", money // 0.0482973, "dollars")
print("The value in pounds is", money // 1.31094, "dollars")
print("The value in rupees is", money // 0.0131285, "dollars")
print("The value in North Korean Won is", money // 0.00111116, "dollars")
print("The value in South Korean Won is", money // 0.000814509, "dollars")
print("The value in Chinese Yuan is", money // 0.157426, "dollars")