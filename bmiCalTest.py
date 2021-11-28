import unittest
import unittest.mock as mock
import bmiCalculator

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_calculatebmi_bmi(self):
        person = {"Gender": "Male", "HeightCm": 175, "WeightKg": 55}
        bmiCalculator.calculatebmi(person)
        self.assertEqual(person['bmi_range_kg_m2'], 18.0)

    def test_updateBmiCategoryAndHealthRisk_UnderweightAndMalnutritionRisk(self):
        person = {"Gender": "Male", "HeightCm": 175, "WeightKg": 55, "bmi_range_kg_m2":18.0}
        overweightCount = bmiCalculator.updateBmiCategoryAndHealthRisk(person)
        self.assertEqual(person['Bmi_category'], "Underweight")
        self.assertEqual(person['Health_risk'], "Malnutrition risk")
        self.assertEqual(overweightCount, 0)

    def test_updateBmiCategoryAndHealthRisk_NormalWeightAndLowRisk(self):
        person = {"Gender": "Male", "HeightCm": 175, "WeightKg": 55, "bmi_range_kg_m2":23.0}
        overweightCount = bmiCalculator.updateBmiCategoryAndHealthRisk(person)
        self.assertEqual(person['Bmi_category'], "Normal weight")
        self.assertEqual(person['Health_risk'], "Low risk")
        self.assertEqual(overweightCount, 0)

    def test_updateBmiCategoryAndHealthRisk_OverweightAndEnhancedRisk(self):
        person = {"Gender": "Male", "HeightCm": 175, "WeightKg": 55, "bmi_range_kg_m2":28.5}
        overweightCount = bmiCalculator.updateBmiCategoryAndHealthRisk(person)
        self.assertEqual(person['Bmi_category'], "Overweight")
        self.assertEqual(person['Health_risk'], "Enhanced risk")
        self.assertEqual(overweightCount, 1)

    def test_updateBmiCategoryAndHealthRisk_ModeratelyObeseAndMediumRisk(self):
        person = {"Gender": "Male", "HeightCm": 175, "WeightKg": 55, "bmi_range_kg_m2":32.0}
        overweightCount = bmiCalculator.updateBmiCategoryAndHealthRisk(person)
        self.assertEqual(person['Bmi_category'], "Moderately obese")
        self.assertEqual(person['Health_risk'], "Medium risk")
        self.assertEqual(overweightCount, 0)

    def test_updateBmiCategoryAndHealthRisk_SeverelyObeseAndHighRisk(self):
        person = {"Gender": "Male", "HeightCm": 175, "WeightKg": 55, "bmi_range_kg_m2":37.0}
        overweightCount = bmiCalculator.updateBmiCategoryAndHealthRisk(person)
        self.assertEqual(person['Bmi_category'], "Severely obese")
        self.assertEqual(person['Health_risk'], "High risk")
        self.assertEqual(overweightCount, 0)

    def test_updateBmiCategoryAndHealthRisk_VerySeverelyObeseAndVeryHighRisk(self):
        person = {"Gender": "Male", "HeightCm": 175, "WeightKg": 55, "bmi_range_kg_m2":47.0}
        overweightCount = bmiCalculator.updateBmiCategoryAndHealthRisk(person)
        self.assertEqual(person['Bmi_category'], "Very severely obese")
        self.assertEqual(person['Health_risk'], "Very high risk")
        self.assertEqual(overweightCount, 0)

    def test_processPersonData_overweightPeopleCount(self):

        mock_data = mock.mock_open(read_data='[{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]')
        overweightPeopleCount=0
        with mock.patch('builtins.open', mock_data):
            overweightPeopleCount = bmiCalculator.processPersonData()
        self.assertEqual(overweightPeopleCount, 1)

if __name__ == '__main__':
    unittest.main()