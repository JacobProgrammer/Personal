import webbrowser
import re
import sys

def is_valid_email(email):
  pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
  match = re.fullmatch(pattern, email)
 
  if match:
    return True
  else:
    return False


setup = input("Welcome to UserPass! Would you like to set up an account using Google or Email?")
if setup.lower() == "google":
  url = "https://accounts.google.com/ServiceLogin/signinchooser?elo=1&ifkv=AeAAQh4m4_aKUtVMmW-iz9EMx8VNwtBcNc7rfxZziQEyyj4-BFOdBOcSI4MgbLPGc5v7sLQPtVwXTA&flowName=GlifWebSignIn&flowEntry=ServiceLogin/"
  webbrowser.open(url)
elif setup.lower() == "email":
  emailsetup = input("Please enter most preferable email: ")

  while not is_valid_email(emailsetup):
    print("Please enter a valid email address")
    emailsetup = input("Please enter most preferable email: ")


  enteremail2 = input("Please re-enter email: ")
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

print("Now that you set up your prefered account settings, we will get some personalization")
print()
print()

UsernameInput = input("Enter desired username no longer than 10 characters: ")
if len(UsernameInput) > 11:
  print("Invalid Input")
else:
  Check = input("You entered" +' '+ UsernameInput  +' '+ "is this correct?")
  for counter in range(1):
    if Check.lower() == "yes":
      print("Great! This is saved in the system")
   
    if Check.lower() != "yes":
      print("Re-run program and try again")
      break

while True:
  Password = input("Enter desired Password no longer than 10 characters: ")
  if len(Password) > 11:
    print("Invalid Input")
  else:
    if Password == UsernameInput:
      print("Username and Password can not be the same. Please re-enter your password")
    else:
      Check2 = input("You entered" +' '+ Password +' '+ "is this correct?")
      if Check2.lower() == "yes":
        print("Great! This is saved in the system")
        sys.exit()
      elif Check2.lower() == "no":
        print("Please re-enter your password")
