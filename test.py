# from flask import Flask, render_template, jsonify, request
# from flask_pymongo import PyMongo

# import google.generativeai as genai
# import os, time

# genai.configure(api_key="AIzaSyCxEGZRzw3bKFo_SBhxmCFWdO322ierrWI")

# model = genai.GenerativeModel(model_name="gemini-1.5-flash")




# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://anamayx13:mOC3OKpllCNHjgkG@firstcluster.wdla5.mongodb.net/wizGPT"
# mongo = PyMongo(app)

# @app.route('/')
# def hello_world():
#     chats = mongo.db.chats.find({})
#     myChats = [chat for chat in chats]
#     print(myChats)
#     return render_template("index.html", myChats = myChats)

# @app.route('/api', methods=["GET","POST"])
# def qa():
#     if request.method == "POST":
#         print(request.json)
#         question = request.json.get("question")
#         chat = mongo.db.chats.find_one({"question": question })

#         print(chat)
#         if chat:
#             data = {"result": f"{chat['answer']}"}
#             return jsonify(data)
#         else:
#             response = model.generate_content(question)
#             data = {"result": f'Answer of the asked prompt is {question}'}
#             mongo.db.chats.insert_one({"question":question , "answer": response.text})
#             return jsonify(data)

# app.run(debug=True)

from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import google.generativeai as genai
import os, time

genai.configure(api_key="YOUR_GEMINI_API KEY")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://anamayx13:mOC3OKpllCNHjgkG@firstcluster.wdla5.mongodb.net/wizGPT"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    return render_template("index.html", myChats=myChats)

@app.route('/api', methods=["POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})

        if chat:
            data = {"result": f"{chat['answer']}"}
        else:
            response = model.generate_content(question)
            answer = response.text  # Assuming 'response.text' contains the answer
            mongo.db.chats.insert_one({"question": question, "answer": answer})
            data = {"result": f"{answer}"}

        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
