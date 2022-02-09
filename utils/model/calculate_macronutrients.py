import json
def calculate_macronutrients(classes):
    """
    input: classes predicted (list)
    output: sum of all macronutrients
    description: calculate macronutrients 
    """
    res = {"protein": 0, "carb": 0, "fat": 0}
    with open('nutrients.json', 'r') as file:
        data = json.load(file)
        for classe in classes:
            res["protein"] += data[classe]["protein"]
            res["carb"] += data[classe]["carb"]
            res["fat"] += data[classe]["fat"]
    return res
