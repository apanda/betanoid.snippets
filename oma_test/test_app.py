#!/usr/bin/env python
from flask import Flask
from flask import request
import logging
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD', 'DELETE', 'PUT', 'OPTIONS'])
def test():
    app.logger.debug(request.method + " " + request.data)

    return "Hello world\n" + request.method + request.data

if __name__ == "__main__":
    logging.basicConfig(filename='test.log')
    app.run(host='0.0.0.0', debug=True)
