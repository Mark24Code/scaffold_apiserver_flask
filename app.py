from flask import Flask, jsonify, request
from mock_data import sample_data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def return_nb_data():
    print('request对象',request)
    print('response数据',sample_data)

    res = jsonify({
        "sample_data": sample_data
    })
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
