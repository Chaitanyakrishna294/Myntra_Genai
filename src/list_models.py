from google import genai

client = genai.Client(api_key="AIzaSyD7kcvc7LYys_MvZPLqyNAXK9QRUCC8Ihg")

models = client.models.list()

for m in models:
    print(m.name)
