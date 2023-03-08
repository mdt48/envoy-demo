from flask import Flask
from random import randint
import numpy as np
from flask import make_response
import time
import os

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

    # requests.get('https://127.0.0.1:8010/fib')
    print('curling')
    os.system('curl 127.0.0.1:8020/fib')
    # os.system('curl 
    time.sleep(2)
    return '200'
    # return response


if __name__ == "__main__":
    app.run(debug=True)