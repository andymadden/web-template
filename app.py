from flask import Flask, Response, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    content = ""
    with open("index.html") as index_file:
        content = index_file.read()
    return Response(content, content_type="text/html")

@app.route("/css/<file>")
def css(file):
    content = ""
    with open("css/<file>") as css_file:
        content = css_file.read()
    return Response(content, content_type="text/css")

@app.route("/js/<file>")
def js(file):
    content = ""
    with open("js/<file>") as js_file:
        content = js_file.read()
    return Response(content, content_type="text/javascript")

app.run(debug=True)