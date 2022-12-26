import webbrowser
setup = input("Welcome to UserPass! Would you like to set up an account using Google or Email?")
if setup.lower() == "google":
  url = "https://accounts.google.com/ServiceLogin/signinchooser?elo=1&ifkv=AeAAQh4m4_aKUtVMmW-iz9EMx8VNwtBcNc7rfxZziQEyyj4-BFOdBOcSI4MgbLPGc5v7sLQPtVwXTA&flowName=GlifWebSignIn&flowEntry=ServiceLogin/"
  webbrowser.open(url)
elif setup.lower() == "email":
  input("Please enter most preferable email: ")

print("Now we set up your account")

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

  for counter2 in range(1):
    Password = input("Enter desired Password no longer than 10 characters: ")
    if len(Password) > 11:
      print("Invalid Input")
    else:
      if Password == UsernameInput:
        print("Username and Password can not be the same. Please re-run the program and try again")
        break

      Check2 = input("You entered" +' '+ Password +' '+ "is this correct?")
      if Check2.lower() == "yes":
        print("Great! This is saved in the system")
    
      elif Check2.lower() == "no":
        print("Re-run program and try again")
   
