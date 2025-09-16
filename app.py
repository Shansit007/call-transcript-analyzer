# print("Hello! Your environment is ready.")

from datetime import datetime

import requests
import csv
import os


from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get Groq API key from environment
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
def get_summary(transcript):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {
                "role": "user",
                "content": f"Summarize the following conversation in 2-3 sentences:\n{transcript}"
            }
        ]
    }
    print("Sending Summary Request...")
    print("URL:", url)
    print("Headers:", headers)
    print("Data:", data)

    response = requests.post(url, headers=headers, json=data)

    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}"


def get_sentiment(transcript):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {
                "role": "user",
                "content": f"Extract the sentiment (positive / neutral / negative) from the following conversation:\n{transcript}"
            }
        ]
    }
    print("Sending Sentiment Request...")
    print("URL:", url)
    print("Headers:", headers)
    print("Data:", data)

    response = requests.post(url, headers=headers, json=data)

    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}"

def save_to_csv(transcript, summary, sentiment):
    file_name = 'call_analysis.csv'
    file_exists = os.path.isfile(file_name)

    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        
        # Write header only if file doesn't exist
        if not file_exists:
            writer.writerow(["Timestamp", "Transcript", "Summary", "Sentiment"])
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Write the data row
        writer.writerow([timestamp, transcript.strip(), summary.strip(), sentiment.strip()])


# HTML Template with Tailwind CSS

form_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Call Transcript Analyzer</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center p-4">
    <div class="max-w-2xl w-full bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
        <h1 class="text-2xl font-bold mb-4 text-center text-gray-800">Call Transcript Analyzer</h1>
        
        <form method="POST" class="space-y-4">
            <textarea name="transcript" rows="5" placeholder="Type the transcript here..." 
                class="w-full p-3 border rounded-md focus:ring-2 focus:ring-blue-400 focus:outline-none resize-none"></textarea>
            <button type="submit" 
                class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition-colors duration-200">
                Analyze
            </button>
        </form>

        {% if transcript %}
        <div class="mt-6 space-y-4">
            <div class="bg-gray-50 p-4 rounded-md shadow-sm hover:shadow-md transition-shadow duration-200">
                <h2 class="font-semibold text-gray-700">Transcript</h2>
                <p class="text-gray-600 mt-2">{{ transcript }}</p>
            </div>

            <div class="bg-gray-50 p-4 rounded-md shadow-sm hover:shadow-md transition-shadow duration-200">
                <h2 class="font-semibold text-gray-700">Summary</h2>
                <p class="text-gray-600 mt-2">{{ summary }}</p>
            </div>

            <div class="bg-gray-50 p-4 rounded-md shadow-sm hover:shadow-md transition-shadow duration-200">
                <h2 class="font-semibold text-gray-700">Sentiment</h2>
                <p class="text-gray-600 mt-2 capitalize">{{ sentiment }}</p>
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""






@app.route('/', methods=['GET', 'POST'])
def home():
    transcript = None
    summary = ""
    sentiment = ""

    if request.method == 'POST':
        transcript = request.form['transcript']
        print("Transcript received:", transcript)

        summary = get_summary(transcript)
        sentiment = get_sentiment(transcript)

        # Save the result into CSV
        save_to_csv(transcript, summary, sentiment)
        print("Saved to call_analysis.csv")

    return render_template_string(form_template, transcript=transcript, summary=summary, sentiment=sentiment)




if __name__ == '__main__':
    app.run(debug=True)

