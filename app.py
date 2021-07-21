from flask import Flask
from flask import json
from logging import Logger, DEBUG, basicConfig
log = Logger(name='a log')
basicConfig(filename='app.log',  level=DEBUG, handlers=[log])

app = Flask(__name__)

log.log(1, msg="This is a log message")
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/status")
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    return response
@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
