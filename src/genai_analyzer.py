import os
import time
import pandas as pd
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()
API_KEY = os.environ.get("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Load negative reviews CSV
df = pd.read_csv("../data/myntra_negative_reviews.csv")

# Limit reviews to stay within free-tier quota
df = df.head(10)

results = []

def analyze_review(review_text):
    prompt = f"""
You are a product analyst for Myntra.

Analyze the following customer review and return:
1. Issue category (Delivery / Quality / Size-Fit / App Bug / Customer Support / Pricing / Other)
2. One-line issue summary

Review:
{review_text}

Respond in this exact format:
Category: <category>
Summary: <summary>
"""
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=prompt
    )
    return response.text.strip()

for idx, row in df.iterrows():
    try:
        analysis = analyze_review(row["review"])
        results.append({
            "rating": row["rating"],
            "review": row["review"],
            "analysis": analysis
        })
        time.sleep(5)  # rate-limit protection
    except Exception as e:
        print("Skipped one review:", e)

# Save output CSV
output_df = pd.DataFrame(results)
output_df.to_csv("../output/myntra_genai_insights.csv", index=False)

print("✅ GenAI analysis completed successfully")
print("📁 Output saved to output/myntra_genai_insights.csv")
