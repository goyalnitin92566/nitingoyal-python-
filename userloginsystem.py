# Ques: User Login System

# Predefine the username and the passward

stored_username="goyalnitin@"
stored_password="123456"

# Take user input

username=input("Enter your usename :")
password=input("Enter your password :")

# Check login credentials

if username==stored_username:
  if password==stored_password:
    print("login successfull!")
  else:
   print("incorrect credentials")
else:
  print("Username is not found")
  
