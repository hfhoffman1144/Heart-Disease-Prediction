import pandas as pd
from catboost import CatBoostClassifier

# Global variable that stores trained model instance
MODEL = CatBoostClassifier().load_model('models/heart_disease_model_2021-12-28')

# Dictionary that converts frontend feature names to names understood by model
display_to_model = {'age':'Age', 'sex':'Sex', 'cpt':'ChestPainType', 'bp':'RestingBP', 
                    'chol':'Cholesterol', 'bs':'FastingBS', 'restingECG':'RestingECG',
                    'maxHR':'MaxHR', 'exerciseAngina':'ExerciseAngina', 'oldpeak':'Oldpeak',
                    'sts':'ST_Slope'}

def predict_hf(data:pd.DataFrame):

    # Make sure column names are correct
    data_predict = data.rename(display_to_model, axis=1)

    # Make sure columns are in the correct order
    data_predict = data_predict[MODEL.feature_names_]

    return MODEL.predict_proba(data_predict)


