
def calculate_bmi(height, weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))
    BMI_value = weight / (height * height )
    print ("BMI =" + str(round(float(BMI_value))))
    return BMI_value 


BMI = calculate_bmi(weight = 57, height = 1.73)


if BMI< 18.5:
    print ("You are underweight")
elif BMI >= 18.5 and BMI <= 25.0:
    print("you are normal weight")
else:
    print ("you are overweight")