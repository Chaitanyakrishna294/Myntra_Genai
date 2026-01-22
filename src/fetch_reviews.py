from google_play_scraper import Sort, reviews
import pandas as pd

result, _ = reviews(
    'com.myntra.android',
    lang='en',
    country='in',
    sort=Sort.NEWEST,
    count=100
)

data = []
for r in result:
    if r['score'] <= 2:   # 🔴 negative reviews only
        data.append([r['score'], r['content']])

df = pd.DataFrame(data, columns=['rating', 'review'])
df.to_csv('../data/myntra_negative_reviews.csv', index=False)

print("✅ Negative reviews saved")
