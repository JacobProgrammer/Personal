import re
import sys
import hashlib
import webbrowser

users = {}  

def get_user(username):
  return users.get(username)

def is_valid_email(email):
  pattern = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
  match = re.fullmatch(pattern, email)
 
  if match:
    return True
  else:
    return False

def login_user():
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  user = get_user(username)
  if user is None:
    print("Invalid username or password")
    return

  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  if hashed_password == user["password_hash"]:
    print("Login successful!")
    print()
    print("Welcome back to UserPass " + username + "!")
    post_login = input("What would you like to view today?")
    if post_login.lower() == "weather":
      weather_location = input("(What area would you like to view (Los Angeles, New York, Miami)")
      if weather_location.lower() == "los angeles":
        webbrowser.open("https://weather.com/weather/today/l/ba9caaca5638fe037a3f428a2a0366c2bd02877d91cb0c5e494384f1cbfc5c1f")
      elif weather_location.lower() == "new york":
        webbrowser.open("https://weather.com/weather/tenday/l/New+York+NY+USNY0996:1:US")
      elif weather_location.lower() == "miami":
        webbrowser.open("https://weather.com/weather/tenday/l/864c2346b3a36fcc8c5d5a73b0651ea44f9968ff6c6b445530eeb9cef734ae58")
      else:
        sys.exit()
    elif post_login.lower() == "stock market" or post_login.lower() == "stocks":
      webbrowser.open("https://finance.yahoo.com/")
    else:
      sys.exit()
  else:
    print("Invalid username or password")

  if not is_valid_email(emailsetup):
    print("Please enter a valid email address.")
    return
  hashed_password = hashlib.sha256(password.encode()).hexdigest()


setup = input("Welcome to UserPass! Lets set up your account. Enter 'setup' to continue ")
if setup.lower() == "login":
  login_user()
  sys.exit()

emailsetup = input("Please enter your email address: ")

while not is_valid_email(emailsetup):
  print("Please enter a valid email address")
  emailsetup = input("Please enter your email address: ")

enteremail2 = input("Please re-enter your email address: ")
while True:
  if emailsetup != enteremail2:
      print("Please enter your email as you did in the first step")
      print()
      enteremail2 = input("Please enter your email again: ")
  else:  
      emailcheck = input("You entered " + emailsetup + " is this correct?")
      if emailcheck.lower() == "yes":
        print("Great! This is saved")
        break
      elif emailcheck.lower() != "yes":
        print("\033[1mPlease re-enter your email\033[0m")
        enteremail2 = ""

print()
print()   

print("Now that you set up your preferred account settings, we will get some personalization")
print()
print()

desired_username = input("Enter a desired username no longer than 10 characters: ")
if len(desired_username) > 11:
  print("Invalid Input")
else:
  check = input("You entered" +' '+ desired_username  +' '+ "is this correct?")
  for counter in range(1):
    if check.lower() == "yes":
      print("Great! This is saved in the system")
   
    if check.lower() != "yes":
      print("Re-run program and try again")
      sys.exit

while True:
  desired_password = input("Enter a desired password no longer than 10 characters: ")
  if len(desired_password) > 11:
    print("Invalid Input")
  else:
    if desired_password == desired_username:
      print("Your password cannot be the same as your username")
      continue
    check = input("You entered" +' '+ desired_password  +' '+ "is this correct?")
    if check.lower() == "yes":
      hashed_password = hashlib.sha256(desired_password.encode()).hexdigest()
      users[desired_username] = {
        "username": desired_username,
        "password_hash": hashed_password
      }
      print("Your account has been created successfully!")
      print("Please login to continue")
      login_user()  
      break
    elif check.lower() != "yes":
      print("Re-run program and try again")
      break
