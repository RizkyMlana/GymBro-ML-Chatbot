from logic.rules import bmi_calculate, bmi_category, tdee_calculate, food_recommendation

def handle_chat(input_user, data_user):
    weight = data_user.get("Weight")
    height = data_user.get("Height")
    age = data_user.get("Age")
    gender = data_user.get("Gender")
    activity = data_user.get("Activity Level")
    goal = data_user.get("goal")
    if input_user.lower() == "bmi":
        bmi = bmi_calculate(weight, height)
        category = bmi_category(bmi)
        return f"Your BMI : {bmi:2.f} ({category})"
    elif input_user.lower() == "calorie deficit" :
        tdee = tdee_calculate(weight, height, age, gender, activity)
        calorie = food_recommendation(tdee, goal)
        return f"Daily Calorie for {goal} weight : {calorie} kkal"
    else :
        return "Choose option BMI/Calorie"


