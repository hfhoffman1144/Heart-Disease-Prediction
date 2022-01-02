from flask import Blueprint, render_template, request

bp1 = Blueprint('main', __name__, url_prefix='/main')

@bp1.route('/api/make_prediction', methods=['POST'])
def make_prediction():

    print(request.form)

    return "yuh"

