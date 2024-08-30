from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/api', methods=["GET","POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        data = {"result": f'Answer of the asked prompt is {question}'}
        return jsonify(data)

app.run(debug=True)