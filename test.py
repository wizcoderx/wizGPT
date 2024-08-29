from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/api', methods=["GET","POST"])
def qa():
    if request.method == "GET":
        data = {"result": "This is my first project created using chatgpt"}
        return jsonify(data)

app.run(debug=True)