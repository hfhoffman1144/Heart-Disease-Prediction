import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, Pool
import plotly.graph_objects as go

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

def get_shap_df(data:pd.DataFrame):

    # Make sure column names are correct
    data_predict = data.rename(display_to_model, axis=1)

    # Make sure columns are in the correct order
    data_predict = data_predict[MODEL.feature_names_]

    data_pool = Pool(data_predict, cat_features=MODEL.get_cat_feature_indices())

    shap_values = MODEL.get_feature_importance(data_pool, type='ShapValues')
    
    shap_values = shap_values[:,:-1].reshape(shap_values.shape[0], len(MODEL.feature_names_))
    shap_df = pd.DataFrame(shap_values, columns=MODEL.feature_names_).T
    shap_df.columns = ['feature']
    shap_df['AbsVal'] = np.abs(shap_df['feature'])
    shap_df.sort_values('AbsVal', ascending=False, inplace=True)

    return shap_df

def plot_shap_values(data:pd.DataFrame):

    shap_df = get_shap_df(data)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=shap_df.index, y=shap_df.feature))
    fig.update_layout(title='Patient Risk Factors')

    return fig.to_json()






