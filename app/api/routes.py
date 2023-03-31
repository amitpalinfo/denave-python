from flask import Blueprint, jsonify, request
from flask_mail import Message
from .. import mail

import smtplib
from email.mime.text import MIMEText

import urllib.parse


import pyodbc

conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=UDB;UID=sa;PWD=Admine51%%'
conn = pyodbc.connect(conn_str)

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return 'Hello, World!'

@api.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    name = "Amit"
    email = "amitmahto64@gmail.com"
    message = "Following are the download link as per your request"
    
    msg = Message('Denave downlaod link', sender='amit@palinfocom.com', recipients=[email])
    msg.body = f'Hi {name},\n\n{message}'
    msg.html = f'<h1>Hello {name}</h1><br> {message}'

    
    mail.send(msg)
    
    return jsonify({'status': True})

@api.route('/getdata', methods=['GET'])
def get_my_table():
    cursor = conn.cursor()
    # Execute the query to get the column names
    table_name = 'TGT_ORGANIZATION_DETAIL'
    querysql = ''

    industryparam = request.args.get('VERTICAL')
    industryparamdecoded_param= urllib.parse.unquote(industryparam)

    subindustryparam = request.args.get('SUB_VERTICAL')
    subindustryparamdecoded_param= urllib.parse.unquote(subindustryparam)

    activityparam = request.args.get('ACTIVITY_TYPE')
    activityparamparamdecoded_param= urllib.parse.unquote(activityparam)

    countryparam = request.args.get('COUNTRY')
    countryparamparamdecoded_param= urllib.parse.unquote(countryparam)

    if(countryparamparamdecoded_param):
        querysql+= f" COUNTRY IN ({countryparamparamdecoded_param})"

    if(industryparamdecoded_param):
        querysql+= f" AND VERTICAL IN ({industryparamdecoded_param})"

    if(subindustryparamdecoded_param):
        querysql+= f" AND SUB_VERTICAL IN ({subindustryparamdecoded_param})"

    if(activityparamparamdecoded_param):
        querysql+= f" AND ACTIVITY_TYPE IN ({activityparamparamdecoded_param})"        



    
    query = f"SELECT * FROM {table_name} WHERE {querysql} "

    # Execute the query and pass the array values as a parameter
    cursor.execute(query)
    
    # Fetch the results and extract the column names and values
    columns = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    
    # Convert the column names and values into a list of dictionaries
    data = []
    for row in rows:
        row_dict = {}
        for i in range(len(columns)):
            row_dict[columns[i]] = row[i]
        data.append(row_dict)

    print("mm",data)    
    
    # Return the list of dictionaries as a response
    return jsonify(data)
