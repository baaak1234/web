from flask import Flask, render_template,request,jsonify,Blueprint
import pymysql
from db import get_db_connection
import joblib
import numpy as np
import pandas as pd

# route 설정
ai_route = Blueprint('ai',__name__)
# model 불러오기
lin_reg = joblib.load('house_price_model_lin.pkl')
rf_reg = joblib.load('house_price_model_rf.pkl')


@ai_route.route("/predict-house-price",methods=['get'])

# 함수지정
def predictHouseprice():
    
    area = request.args.get('area')
    rooms = request.args.get('rooms')
    year_built = request.args.get('year')
    income = request.args.get('income')
    school_rating = request.args.get('school_rating')
    transit_score = request.args.get('transit_score')

    # feature 설정

    features = np.array([[
        int(area),
        int(rooms),
        int(year_built),
        int(income),
        int(school_rating),
        int(transit_score),
    ]])

    # 예측 실행
    lin_reg_pred = lin_reg.predict(features)[0]
    rf_reg_pred = rf_reg.predict(features)[0]

    #DB연결
    conn=get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    #SQL 쿼리 작성

    query = """
    INSERT INTO house
    (area,rooms,year_built,income,school_rating,transit_score,created_date,pred_lin,pred_rf)
    VALUES
    (%s,%s,%s,%s,%s,%s,sysdate(),%s,%s)
    """
    cursor.execute(query,(area,rooms,year_built,income,school_rating,transit_score,lin_reg_pred,rf_reg_pred))
    conn.commit()
    cursor.close()
    conn.close()



#결과 도출
    return jsonify({
        "message":"ok",
        "price_by_lin": lin_reg_pred,
        "price_by_rf": rf_reg_pred
        })
        