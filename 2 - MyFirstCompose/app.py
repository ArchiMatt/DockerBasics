import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Coucou les loulous</h1>
                <p>Vous avez exposé une API via flask et docker</p>'''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)