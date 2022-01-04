import pandas as pd
from flask import Blueprint, request
from services.model_utils import predict_hf, plot_shap_values

bp1 = Blueprint('main', __name__, url_prefix='/main')

@bp1.route('/api/make_prediction', methods=['POST'])
def make_prediction():

    form_df:pd.DataFrame = pd.DataFrame(request.form, index=[0])

    pred = predict_hf(form_df)
    pred_class_1 = pred[0][1]

    plot = plot_shap_values(form_df)

    return {'pred':round(pred_class_1, 2), 'plot':plot}

