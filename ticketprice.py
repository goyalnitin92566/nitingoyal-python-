# Take user input
age = int(input("Enter Your age :"))
is_student=("Are you a student ? (Yes/No): ")
# Determine Ticket Price
if age<=5:
  print("Your ticket is free!")
elif age<=13:
  print("Your ticket is Rs.99/-")
elif age<=18:
  print("Your ticket is Rs.149/-")
else:
  print("Your ticket is Rs.199/-")