import flask
import datetime
from flask import request, jsonify
app = flask.Flask(__name__)
filename = "/tmp/log.txt"
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    file=open(filename,'a')
    file.write("Connection at "+str(datetime.datetime.now())+"\r\n")
    file.close()
    return '''<h1>Coucou les loulous</h1>
                <p>Vous avez exposé une API via flask et docker</p>'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)