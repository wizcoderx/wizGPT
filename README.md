# ChatGPT Clone using Google Gemini API and MongoDB Atlas

This project is a ChatGPT-like application that uses Google Gemini for generating AI responses and MongoDB Atlas for storing chat data. Below are the steps to set up your environment, including how to get your Google Gemini API key and how to set up MongoDB Atlas.

## Prerequisites

- Python 3.x
- Flask
- MongoDB Compass (for connecting to your MongoDB cluster)
- A Google Cloud Platform (GCP) account
- A MongoDB Atlas account

## 1. Get Google Gemini API Key

To use the Google Gemini API, you need to get an API key from the Google AI Developer platform.

### Steps to Obtain the API Key:

1. Visit the [Google AI Developer](https://ai.google.dev/) website.
2. Sign in with your Google account.
3. Navigate to the **Google Gemini** section.
4. Click on **Get API Key** or **Start Free Trial** (if applicable).
5. Follow the on-screen instructions to create a new API key.
6. Copy the API key for later use.

### Add API Key to Your Flask Application:

Once you have your API key, add it to your Flask application as shown below:

```python
import google.generativeai as genai

# Replace 'YOUR_GEMINI_API_KEY' with your actual API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```
## 2. Set Up MongoDB Atlas Free Tier Cluster

MongoDB Atlas offers a free tier where you can create a small MongoDB cluster. Below are the steps to set it up using Google Cloud Platform (GCP).

### Steps to Set Up MongoDB Atlas:

1. **Create a MongoDB Atlas Account**:
   - Visit the [MongoDB Atlas website](https://www.mongodb.com/cloud/atlas).
   - Sign up for a new account or log in if you already have one.

2. **Create a New Cluster**:
   - After logging in, click on **Build a Cluster**.
   - Choose the **Free Tier** option.
   - Under the **Cloud Provider & Region** section, select **Google Cloud Platform (GCP)** and choose a region that is close to you.
   - Click **Create Cluster**.

3. **Set Up Database Access**:
   - After your cluster is created, go to the **Database Access** section.
   - Click on **Add New Database User**.
   - Create a new user with a username and password. Make sure to note these credentials.

4. **Set Up Network Access**:
   - Go to the **Network Access** section.
   - Click on **Add IP Address**.
   - You can allow access from anywhere by adding `0.0.0.0/0`, or you can add a specific IP address.

5. **Get the Connection String**:
   - Go to your cluster and click on the **Connect** button.
   - Choose **Connect Your Application**.
   - Copy the connection string provided. It will look something like this:
     ```
     mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<dbname>?retryWrites=true&w=majority
     ```
   - Replace `<username>` and `<password>` with your database user credentials, and replace `<dbname>` with your database name (e.g., `wizGPT`).

### Connect to MongoDB Using MongoDB Compass:

1. Download and install [MongoDB Compass](https://www.mongodb.com/try/download/compass).
2. Open MongoDB Compass and paste your connection string into the connection dialog.
3. Click **Connect**.

## 3. Set Up the Flask Application

### Steps to Set Up the Flask Application:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/chatgpt-clone.git
   cd chatgpt-clone
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```
3. Add your Google Gemini API key and MongoDB connection string to the Flask application:

```bash
genai.configure(api_key="YOUR_GEMINI_API_KEY")
app.config["MONGO_URI"] = "YOUR_MONGODB_CONNECTION_STRING"
```

4. Run the Flask App:

```bash
python app.py
```