    BMI = weight / (height/100)**2
    return BMI

def bmi_judgemement(BMI):
    if BMI <= 18.4:
        return("underweight.")
    elif BMI <= 24.9:
        return("healthy.")
    elif BMI <= 29.9:
        return("over weight.")
    elif BMI <= 34.9:
        return("severely over weight.")
    elif BMI <= 39.9:
        return("obese.")
    else:
        return("severely obese.")


height = float(input("height in cm>> "))
weight = float(input("weight in kg>> "))
BMI = bmi_information(weight, height)
print(f"You BMI is {BMI}")
print(f"You are {bmi_judgemement(BMI)}")
