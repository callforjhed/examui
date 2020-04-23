#!./virtual/Scripts
import os
from flask import *
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config.from_object('config.Config')
app.logger.info('Loading configurations...done.')

#Generate secret key
key = os.urandom(16)
app.config['SECRET_KEY'] = key
app.logger.info('Loading secret key...done.')

r = requests.get('http://localhost:8080/lookup/products')
products = r.json()

@app.route('/')
def home():   
    r1 = requests.get('http://localhost:8080/cust/1')
    baskets = r1.json()

    return render_template('exam.html', products=products,baskets=baskets)

@app.route('/addbasket', methods=['POST'])
def addbasket():
    basketname = request.form['basketname']
            
    resp = requests.post(url='http://localhost:8080/cust/1/addbasket',json={'basketname':basketname})
    message  = resp.text

    r1 = requests.get('http://localhost:8080/cust/1')
    baskets = r1.json()

    return render_template('exam.html', msg = message, products=products,baskets=baskets)

@app.route('/addbasketitem', methods=['POST'])
def addbasketitem():
    basketname = request.form['basketname']
    
    resp = requests.post(url='http://localhost:8080/cust/1/addbasket',json={'basketname':basketname})
    message  = resp.text

    r1 = requests.get('http://localhost:8080/cust/1')
    baskets = r1.json()

    return render_template('exam.html', msg = message, products=products,baskets=baskets)

@app.route('/mybasket')
def mybasket():
    r1 = requests.get('http://localhost:8080/cust/1')
    cust = r1.json()

    total = 0
    for basket in cust['baskets']:
        for item in basket['items']:
            total = total + (item['quantity'] * item['itemprice'])

    return render_template('mybasket.html',msg="",customer=cust,total=total)


#main program
if __name__ == '__main__':      
    app.run()
    
    

