from flask import Flask
from random import randint
import numpy as np
from flask import make_response
import time
import os, requests
from flask import request, jsonify

# report = pyRAPL.outputs.DataFrameOutput()
app = Flask(__name__)

def multiply_matrices():
    # 100 x 100 matrix
    n = 50

    # create two random nxn matrices
    matrix1 = np.random.rand(n, n)
    matrix2 = np.random.rand(n, n)

    # multiply the matrices together
    result = np.dot(matrix1, matrix2)

@app.route('/matrix_ops', methods=['GET', 'POST'])
def some_work():
    # response = make_response(' Hello World ')
    # response.headers['THIS-IS-A-HEADER'] = 'THIS-IS-A-HEADER-VALUE'
    # multiply_matrices()

    # r = requests.get('http://www.google.com')
    # print all haeders
    # print(r.headers)
    # print()
    headers = dict(request.headers)
    id =  headers['X-Request-Id']
    del headers['X-Request-Id']
    headers = {}
    headers['init-req-id'] = id
    print(headers)
    response = requests.get('http://127.0.0.1:8020/fib', headers=headers)
    print(response.headers)
    # os.system('curl 127.0.0.1:8020/fib')
    # os.system('curl http://www.google.com/')
    # os.system('curl 
    time.sleep(2)
    # return '200'
    return jsonify(dict(response.headers))


if __name__ == "__main__":
    app.run(debug=True)