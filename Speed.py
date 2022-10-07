"""
This program has the user input the speed and terrain of
which they are on and gives a unique output to each

Author: Jacob Olshanskiy
Date: 3-17-22
"""
vehicle = eval(input("How fast is your vehicle driving in the unit miles per hour?"))
area = input("What terrain is your vehicle driving on (Freeway, Main Road, Residential Street)")
if vehicle > 65:
    if area =="Freeway" or area == "freeway":
        print("Thank you! Have a safe drive")
    elif area == "Main Road" or area == "main road":
        print("Consider slowing down the vehicle")
    elif area == "Residential Street" or area == "residential street":
        print("Slow down vehicle immediately")
elif 45 < vehicle < 64.9:
    if area =="Freeway" or area == "freeway":
        print("Consider increasing speed on vehicle")
    elif area == "Main Road" or area == "main road":
        print("Thank you! Have a safe drive")
    elif area == "Residential Street" or area == "residential street":
        print("Slow down vehicle immediately")
elif 0 < vehicle < 44.9:
    if area == "Freeway" or area == "freeway":
        print("Increase speed of vehicle immediately")
    elif area == "Main Road" or area == "main road":
        print("Consider increasing speed on vehicle")
    elif area == "Residential Street" or area == "residential street":
        print("Thank you! Have a nice day")