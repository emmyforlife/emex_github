#BMI Calculator

name = input ("Please enter your name here: ")
height_m = float (input ("Please enter your height in meters: "))
weight_kg = float (input ("Please enter your weight in kilograms: "))

bmi = weight_kg / (height_m ** 2)
print("bmi:  ")
print (bmi)
if bmi < 18.5:
    print (name, "is underweight")
elif bmi <= 24.9:
    print (name, "your weight is normal")
elif bmi <= 29.9:
    print (name, "you are overweight")
else:
    print (name, "you are obese")

