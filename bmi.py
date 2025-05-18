
def calculate_bmi(height, weight):
    print ("Height = " + str(height))
    print ("Weight = " + str(weight))
    BMI = weight / (height * height )
    print ("BMI =" + str(round(float(BMI_value))))
    if BMI< 18.5:
         print ("You are underweight")
         return -1
   
    elif BMI >= 18.5 and BMI <= 25.0:
        print("you are normal weight")
        return 0
    
    else:
        print ("you are overweight")
        return 1

    

BMI = calculate_bmi(weight = 57, height = 1.73)

