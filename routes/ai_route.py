from flask import Flask, render_template,request,jsonify,Blueprint
import pymysql
from db import get_db_connection
import joblib
import numpy as np
import pandas as pd

ai_route = Blueprint('ai',__name__)

lin_reg = joblib.load('house_price_model_lin.pkl')
rf_reg = joblib.load('house_price_model_rf.pkl')


@ai_route.route("/predict-house-price",methods=['get'])
def predictHouseprice():
    
    area = request.args.get('area')
    rooms = request.args.get('rooms')
    year_built = request.args.get('year')
    income = request.args.get('income')
    school_rating = request.args.get('school_rating')
    transit_score = request.args.get('transit_score')



    features = np.array([[
        int(area),
        int(rooms),
        int(year_built),
        int(income),
        int(school_rating),
        int(transit_score),
    ]])

    lin_reg_pred = lin_reg.predict(features)[0]
    rf_reg_pred = rf_reg.predict(features)[0]

    return jsonify({
        "message":"ok",
        "price_by_lin": lin_reg_pred,
        "price_by_rf": rf_reg_pred
        })
        