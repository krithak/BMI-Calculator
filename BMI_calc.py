#BMI calculator

#less than or equal to 18.4 = underweight
#18.5-24.9 = normal
#25.0-39.9 = overweight
#40.0 and above = obese

#equation = weight (lbs)/height(in)^2 * 703
#user input for weight and height(decimals)

weight = float(input("Weight (lbs): ")) #taking the user's weight input, converting into float, storing in "weight" variable
height = input("Height (ex: 5'2 = 5.02): ") #taking user's height input, is a string, storing in "height" variable

#separating first and second values of height
feet = float(height[0]) #taking the first value from the height input, storing in "feet" variable
inches = float(height[2] + height[3]) #taking the 3rd and 4th input, adding together, storing in "inches" variable

total_height = (feet*12) + inches #taking 1st value from height input, converting to inches, adding to value of "inches" variable

#BMI formula
bmi = (weight/(total_height**2)) * 703
bmi = (round(bmi, 2)) #taking the bmi, rounding values after decimal to two places

#statements displaying BMI and what it is considered
if bmi <= 18.4:
    print('Your BMI ', bmi, ' is considered underweight.')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Your BMI ', bmi, ' is considered normal.')
elif bmi >=25.0 and bmi <=39.9:
    print('Your BMI ', bmi, ' is considered overweight.')
elif bmi >=40.0:
    print('Your BMI ', bmi, ' is considered obese.')
