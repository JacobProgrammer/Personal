"""
This program takes user information and outputs the optimal area to buy a home
If user puts in value of budget less that 1000000...
Do not include the 0's after number (ex -> 900,000 = 900)

Author: Jacob Olshanskiy
Date:4-12-22
"""
def price():
        return eval(input("What is your price range"))
def greeting():
    print("Great! Let me do some research")
print()
print("Hello, I can show you the area of your perfect home")
print()
homestate = input("What state would you like to live in").lower()
if homestate == " Alabama" or homestate == " alabama":
    greeting()
    price1 = price()
    if price1 > 1000000:
        print("The optimal city for you to shop is Orange Beach")
    elif 999 > price1 > 500:
        print("The optimal city for you to shop is Vesatvia Hills")
    else:
        print("The optimal city for you to shop is Hoover")
if homestate == " Alaska" or homestate == " alaska":
    greeting()
    price2 = price()
    if price2 > 1000000:
        print("The optimal city for you to shop is Juneau")
    elif 999 > price2 > 500:
        print("The optimal city for you to shop is Anchorage")
    else:
        print("The optimal city for you to shop is Fairbanks")
if homestate == " Arizona" or homestate == " arizona":
    greeting()
    price3 = price()
    if price3 > 1000000:
        print("The optimal city for you to shop is Paridise Valley")
    elif 999 > price3 > 500:
        print("The optimal city for you to shop is Scottsdale")
    else:
        print("The optimal city for you to shop is Cave Creek")
if homestate == " Arkansas" or homestate == " arkansas":
    greeting()
    price4 = price()
    if price4 > 1000000:
        print("The optimal city for you to shop is Fayetteville")
    elif 999 > price4 > 500:
        print("The optimal city for you to shop is Bentonville")
    else:
        print("The optimal city for you to shop is Rogers")
if homestate == " California" or homestate == " california":
    greeting()
    price4 = price()
    if price4 > 1000000:
        print("The optimal city for you to shop is Beverly Hills")
    elif 999 > price4 > 500:
        print("The optimal city for you to shop is Los Angeles")
    else:
        print("The optimal city for you to shop is Canoga Park")
if homestate == " Colorado" or homestate ==" colorado":
    greeting()
    price6 = price()
    if price6 > 1000000:
        print("The optimal city for you to shop is Aspen/Vail")
    elif 999 > price6 > 500:
        print("The optimal city for you to shop is Denver")
    else:
        print("The optimal city for you to shop is Lakewood")
if homestate == " Connecticut" or homestate == " connecticut":
    greeting()
    price7 = price()
    if price7 > 1000000:
        print("The optimal city for you to shop is Greenwich")
    elif 999 > price7 > 500:
        print("The optimal city for you to shop is Ridgefield")
    else:
        print("The optimal city for you to shop is Trumbull")    
if homestate == " Delaware" or homestate == " delaware":
    greeting()
    price8 = price()
    if price8 > 1000000:
        print("The optimal city for you to shop is Bethany Beach")
    elif 999 > price8 > 500:
        print("The optimal city for you to shop is Rehoboth Beach")
    else:
        print("The optimal city` for you to shop is Lewes")
if homestate == " Florida" or  homestate == " florida":
    greeting()
    price9 = price()
    if price9 > 1000000:
        print("The optimal city for you to shop is Boca Raton/Palm Beach")
    elif 999 > price9 > 500:
        print("The optimal city for you to shop is Highland Beach")
    else:
        print("The optimal city for you to shop is Sunny Isles")
if homestate == " Georgia" or homestate == " georgia":
    greeting()
    price9 = price()
    if price9 > 1000000:
        print("The optimal city for you to shop is Milton")
    elif 999 > price9 > 500:
        print("The optimal city for you to shop is Atlana")
    else:
        print("The optimal city for you to shop is Greensboro")
if homestate == " Hawaii" or homestate == " hawaii":
    greeting()
    price10 = price()
    if price10 > 1000000:
        print("The optimal city for you to shop is Wailea")
    elif 999 > price10 > 500:
        print("The optimal city for you to shop is Kapolei")
    else:
        print("The optimal city for you to shop is Waianae")
if homestate == " Idaho" or homestate == " idaho":
    greeting()
    price11 = price()
    if price11 > 1000000:
        print("The optimal city for you to shop is Ketchum")
    elif 999 > price11 > 500:
        print("The optimal city for you to shop is Eagle")
    else:
        print("The optimal city for you to shop is Star")
if homestate == " Illinois" or homestate == " illinois":
    greeting()
    price12 = price()
    if price12 > 1000000:
        print("The optimal city for you to shop is Hinsdale")
    elif 999 > price12 > 500:
        print("The optimal city for you to shop is Burr Ridge")
    else:
        print("The optimal city for you to shop is Barrington")
if homestate == " Indiana" or homestate == " indiana":
    greeting()
    price13 = price()
    if price13 > 1000000:
        print("The optimal city for you to shop in is Zionsville")
    elif 999 > price13 > 500:
        print("The optimal city for you to shop in is Carmel")
    else:
        print("The optimal city for you to shop in is Westfield")
if homestate == " Iowa" or homestate == " iowa":
    greeting()
    price14 = price()
    if price14 > 1000000:
        print("The optimal city for you to shop in is Bettendorf")
    elif 999 > price14 > 500:
        print("The optimal city for you to shop in is Johnston")
    else:
        print("The optimal city for you to shop in is Coralville")
if homestate == " Kansas" or homestate == " kansas":
    greeting()
    price15 = price()
    if price15 > 1000000:
        print("The optimal city for you to shop in is Leawood")
    elif 999 > price15 > 500:
        print("The optimal city for you to shop in is Overland Park")
    else:
        print("The optimal city for you to shop in is Lenexa")
if homestate == " Kentucky" or homestate == " kentucky":
    greeting()
    price16 = price()
    if price16 > 1000000:
        print("The optimal city for you to shop is in Nicholasville")
    elif 999 > price16 > 500:
        print("The optimal city for you to shop in is Lexington-Fayette")
    else:
        print("The optimal city for you to shop in is Union")
