from flask import Flask, send_file, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)
@app.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    directory = 'images'
    return send_file(os.path.join(directory, filename))

@app.route('/image_list', methods=['GET'])
def get_image_list():
    directory = 'images'
    files = os.listdir(directory)
    return jsonify(files)

if __name__ == '__main__':
    app.run(debug=True)
