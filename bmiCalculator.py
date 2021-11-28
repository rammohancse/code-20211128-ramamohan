
# sample date
# personCollection = [{"Gender": "Male", "HeightCm": 175, "WeightKg": 75},
#                     {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
#                     {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
#                     {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
#                     {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
#                     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
#                     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
#                     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
#                     {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]


def updateBmiCategoryAndHealthRisk(personData):
    bmi_range_kg_m2 = personData['bmi_range_kg_m2']
    if bmi_range_kg_m2 <= 18.4:
        personData['Bmi_category'] = 'Underweight'
        personData['Health_risk'] = 'Malnutrition risk'
    elif bmi_range_kg_m2 <= 24.9:
        personData['Bmi_category'] = 'Normal weight'
        personData['Health_risk'] = 'Low risk'
    elif bmi_range_kg_m2 <= 29.9:
        personData['Bmi_category'] = 'Overweight'
        personData['Health_risk'] = 'Enhanced risk'
        return 1
    elif bmi_range_kg_m2 <= 34.9:
        personData['Bmi_category'] = 'Moderately obese'
        personData['Health_risk'] = 'Medium risk'
    elif bmi_range_kg_m2 <= 39.9:
        personData['Bmi_category'] = 'Severely obese'
        personData['Health_risk'] = 'High risk'
    else:
        personData['Bmi_category'] = 'Very severely obese'
        personData['Health_risk'] = 'Very high risk'
    return 0


def calculatebmi(personData):
    personData['bmi_range_kg_m2'] = round(personData['WeightKg'] / ((personData['HeightCm'] / 100) ** 2), 1)


def processPersonData():
    overweightPeopleCount = 0
    from datetime import datetime
    startDate = datetime.now()
    import json
    with open(r'./personData.json', 'r') as file:
        personCollection = json.load(file)

    for personData in personCollection:
        calculatebmi(personData)
        overweightPeopleCount += updateBmiCategoryAndHealthRisk(personData)
    endDate = datetime.now()
    print(f'process time : start {startDate} and end {endDate} and delta {endDate - startDate}')
    return overweightPeopleCount

if __name__ == '__main__':
    print(f'OverweightPeopleCount : {processPersonData()}')

