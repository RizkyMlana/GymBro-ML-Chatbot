import pandas as pd
def bmi_calculate(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi,2)

def bmi_category(bmi):
    if bmi < 18.5 :
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def tdee_calculate(weight, height, age, gender, activity_level):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else :
        bmr = 10 * weight + 6.25 + height - 5 * age - 161
    
    activity_map = {
        "low" : 1.2,
        "moderate" : 1.55,
        "high" : 1.9, 
    }
    multiplier = activity_map.get(activity_level, 1.2)
    tdee = bmr * multiplier
    return round(tdee)

def caloried_deficit(tdee, goal):
    if goal == "naik":
        return tdee + 500
    elif goal == "turun":
        return tdee - 500
    else:
        return tdee
    
