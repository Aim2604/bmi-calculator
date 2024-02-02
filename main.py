weight = input("What is your weight in kg? ")
weight = float(weight)

height = input("What is your height in m? ")
height = float(height)

bmi = weight / (height*height)

print("Your bmi is " + str(bmi))

if 18 <= bmi <= 25:
  print("You are healthy")

elif bmi < 18:
  print("You are underweight")

else:
  print("You are overweight")