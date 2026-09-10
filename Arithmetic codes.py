#Welcome message
print('Welcome to CrestPTK')
name = input(str('What is your name?'))

print(f'Hello {name}, we are pleased to have you here.')
#calculating age
birth_year = input(str('What is your birth year?'))
age = 2026- int(birth_year)
print(f'Your age is {age}')
print('Great! Now let us calculate your BMI to see the status of your health')

#calculating BMI
height = input(str('What is your height in m?'))
weight = input(str('What is your weight in kg'))
BMI = float(weight)/float(height)
print(f'Your BMI is {BMI}')

# Determining if one is healthy or not

if BMI < 18.5:
    print('You are underweight')
elif BMI >= 18.5 and BMI <= 24.9:
    print('You have a healthy weight')
elif BMI >= 25 and BMI <= 29.9:
    print('You are overweight')
else:
    print('You are obese')


