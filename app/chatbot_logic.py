from logic.rules import bmi_calculate, bmi_category, tdee_calculate, food_recommendation, get_goal

def process_input(data):
    weight = data['weight']
    height = data['height']
    age = data['age']
    gender = data['gender']
    activity_level = data['activity_level']

    bmi = bmi_calculate(weight, height)
    category = bmi_category(bmi)
    goal = get_goal(bmi)
    tdee = tdee_calculate(weight, height, age, gender, activity_level)
    food = food_recommendation(goal)
    return {
        'bmi' : bmi,
        'category' : category,
        'goal' : goal,
        'tdee' : tdee,
        'food' : food,
    }


