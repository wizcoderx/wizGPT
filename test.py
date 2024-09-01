from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import google.generativeai as genai
import os, time

# Configure the Google Gemini API with your API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Create a model instance for the Google Gemini model (version 1.5 flash)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Initialize the Flask application
app = Flask(__name__)

# Set up the connection to MongoDB using the MongoDB URI
app.config["MONGO_URI"] = "YOUR_MONGODB_CONNECTION_STRING"
mongo = PyMongo(app)  # Initialize PyMongo with the Flask app

# Define the route for the homepage
@app.route('/')
def hello_world():
    # Retrieve all chat records from the MongoDB 'chats' collection
    chats = mongo.db.chats.find({})
    # Convert the retrieved MongoDB cursor to a list of chat records
    myChats = [chat for chat in chats]
    # Render the 'index.html' template, passing in the list of chats
    return render_template("index.html", myChats=myChats)

# Define the API endpoint for handling questions and generating responses
@app.route('/api', methods=["POST"])
def qa():
    if request.method == "POST":
        # Extract the 'question' from the incoming JSON request
        question = request.json.get("question")

        # Check if the question has already been asked and stored in the database
        chat = mongo.db.chats.find_one({"question": question})

        if chat:
            # If the question exists in the database, use the stored answer
            data = {"result": f"{chat['answer']}"}
        else:
            # If the question is new, generate a response using the Gemini model
            response = model.generate_content(question)
            answer = response.text  # Extract the text of the generated response

            # Store the new question and answer pair in the MongoDB 'chats' collection
            mongo.db.chats.insert_one({"question": question, "answer": answer})

            # Return the generated answer in the API response
            data = {"result": f"{answer}"}

        # Return the result as a JSON response
        return jsonify(data)

# Run the Flask application in debug mode if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
