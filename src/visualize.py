import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load Gemini output
df = pd.read_csv("../output/myntra_genai_insights.csv")

# -------- Extract Category --------
def extract_category(text):
    match = re.search(r"Category:\s*(.*)", text)
    return match.group(1).strip() if match else "Unknown"

df["category"] = df["analysis"].apply(extract_category)

# -------- Bar Chart: Issue Categories --------
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")
plt.title("Myntra App Issues by Category")
plt.xlabel("Issue Category")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("../output/issue_category_distribution.png")
plt.show()

# -------- Word Frequency from Reviews --------
all_text = " ".join(df["review"].astype(str)).lower()
words = re.findall(r"\b[a-z]{4,}\b", all_text)

common_words = Counter(words).most_common(15)

labels, values = zip(*common_words)

plt.figure()
plt.bar(labels, values)
plt.xticks(rotation=45)
plt.title("Most Common Words in Negative Reviews")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../output/common_issue_words.png")
plt.show()

print("✅ Visualizations generated successfully")
print("📁 Saved in output folder")
