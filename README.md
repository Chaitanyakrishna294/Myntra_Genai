🧠 GenAI-Powered Myntra Customer Feedback Intelligence

An end-to-end Generative AI–driven analytics system that collects live Myntra Google Play Store reviews, analyzes negative customer feedback using Google Gemini, and visualizes actionable product insights.

📌 Problem Statement

Large-scale e-commerce platforms like Myntra receive thousands of user reviews daily. Manually analyzing negative feedback to identify recurring product and app issues is time-consuming and inefficient.

This project automates the collection, analysis, and visualization of customer complaints using GenAI to support data-driven product decisions.

🚀 Key Features

Live collection of Myntra app reviews from Google Play Store

Automatic filtering of negative customer feedback

AI-powered issue classification and summarization using Gemini API

Structured CSV outputs for downstream analysis

Visual insights highlighting dominant customer pain points

🛠️ Tech Stack

Programming Language: Python

GenAI Model: Google Gemini (Flash Lite – Free Tier)

Libraries: Pandas, Matplotlib, google-play-scraper

Data Format: CSV

Environment: Python 3.13

📂 Project Structure
Myntra GenAI Project/
│
├── .env
├── data/
│   └── myntra_negative_reviews.csv
├── output/
│   ├── myntra_genai_insights.csv
│   ├── issue_category_distribution.png
│   └── common_issue_words.png
└── src/
    ├── fetch_reviews.py
    ├── genai_analyzer.py
    └── visualize.py

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-link>
cd Myntra-GenAI-Project

2️⃣ Install Dependencies
pip install pandas matplotlib google-play-scraper google-genai python-dotenv

3️⃣ Configure API Key

Create a .env file in the root directory:

GOOGLE_API_KEY=your_gemini_api_key_here

▶️ How to Run the Project
Step 1: Fetch Live Reviews
cd src
python fetch_reviews.py

Step 2: Analyze Reviews Using GenAI
python genai_analyzer.py

Step 3: Generate Visualizations
python visualize.py

📊 Output

CSV: AI-generated insights from customer reviews

Bar Chart: Distribution of issue categories

Word Frequency Chart: Common complaint keywords

These outputs help identify:

Delivery issues

Product quality problems

App bugs

Customer support gaps

🧠 Example Use Cases

Product managers identifying top customer pain points

Data teams monitoring app experience issues

Intern-level demonstration of real-world GenAI pipelines

🔮 Future Enhancements

Streamlit dashboard for real-time insights

Trend analysis over time

Auto-generated product improvement recommendations

Integration with social media feedback (Twitter, Reddit)
