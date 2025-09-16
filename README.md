# Call Transcript Analyzer

## 📄 Project Overview

The **Call Transcript Analyzer** is a Python-based web application that enables users to input customer call transcripts and automatically generate a summary and sentiment analysis using the Groq API. The results are displayed in an intuitive interface and stored in a CSV file for record-keeping.

The application is built with Python and Flask, styled with Tailwind CSS, and includes a dark/light mode toggle for enhanced user experience. It’s designed to be clean, responsive, and easy to use while demonstrating API integration, data handling, and frontend design.


## 🚀 Features

✔ **Transcript Input** – Users can paste or type customer conversations into a form.  
✔ **API Integration** – Summarizes the transcript and extracts sentiment using the Groq API.  
✔ **Results Display** – Shows the original transcript, summary, and sentiment clearly.  
✔ **CSV Storage** – Saves all submissions into `call_analysis.csv` with timestamps.  
✔ **Dark/Light Mode** – Toggle between themes for better accessibility and user preference.  
✔ **Responsive Design** – Clean and professional UI using Tailwind CSS.

---

## 📂 Project Structure

mini_tech_challenge/
├── app.py # Python Flask web application script
├── .env # Environment file storing the Groq API key (not for public sharing)
├── call_analysis.csv # CSV file storing transcripts, summaries, sentiments, and timestamps
├── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download the Project

Download or clone the project repository to your local machine.

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # For Mac/Linux
venv\Scripts\activate        # For Windows

-> Install Required Python Packages
pip install flask requests pandas python-dotenv

-> Setup Environment Variables
Create a .env file in the project directory with the following content: GROQ_API_KEY=your_actual_api_key_here
##Replace your_actual_api_key_here with your API key from Groq

-> Run the Application
python app.py

-> Open your browser and go to: http://127.0.0.1:5000/
