# Take user input

age = int(input("Enter Your Age"))

# checking eligibility

if age<=5:
  print("You are a Child")
elif age<=13:
  print("You are in mid teen")
elif age<=17:
  print("You are a Teenager")
else:
  print("You are Eligible to Vote")