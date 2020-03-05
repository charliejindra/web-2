from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def index_file(path):
    return send_from_directory("", "index.html")

@app.route('/api/images_list', methods=['GET'])
def images_list(path):
    return send_from_directory("api", path)

@app.route('/static/<path:path>', methods=['GET'])
def static_file(path):
    return send_from_directory("static", path)