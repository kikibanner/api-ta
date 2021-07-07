from flask import Flask,jsonify,request
import numpy as np
from pickle import load


app = Flask(__name__)
global model
global pca
model = load(open('model.pkl','rb'))
pca = load(open('pca.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def index():
    if(request.method=='POST'):
        reqjson = request.get_json()
        return jsonify({'request':"kosong"}),201
    else:
        return jsonify({'request':'kosong'})

""" @app.route('/covidtest/<string:data>',methods=['GET'])
def proses(data):
    global model
    global pca
    dataMasuk = np.array([data.split(',')])
    dataMasuk = dataMasuk.astype('int32')
    dataPCA = pca.transform(dataMasuk)
    predModel = model.predict(dataPCA)
    hasilFix = int(predModel[0])
    return jsonify({'result':hasilFix}) """

@app.route('/covidtest/<string:data>',methods=['GET'])
def proses(data):
    global model
    global pca
    dataMasuk = np.array([data.split(',')])
    dataMasuk = dataMasuk.astype('int32')
    dataPCA = pca.transform(dataMasuk)
    predModel = model.predict(dataPCA)
    hasilFix = int(predModel[0])
    response = jsonify({'result':hasilFix})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
