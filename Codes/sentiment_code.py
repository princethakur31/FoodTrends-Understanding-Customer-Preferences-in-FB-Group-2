import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the input CSV file (replace 'input.csv' with your file path)
df = pd.read_csv('sentiment_ip.csv')

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()



# Function to compute compound score and label only
def compute_sentiment(text):
    if pd.isna(text):
        return pd.Series([0.0, 'Neutral'])  # Handle NaN with neutral
    scores = analyzer.polarity_scores(str(text))
    compound = scores['compound']
    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'
    return pd.Series([compound, label])

# Apply to 'text' column, adding ONLY score and label columns (preserves all original fields)
df[['sentiment_score', 'sentiment_label']] = df['comment_text'].apply(compute_sentiment)

# Save to new CSV with all original fields plus the two new columns
df.to_csv('sentiment_analysis.csv', index=False)

print("New CSV 'output_with_sentiment.csv' created successfully!")
print(df[['comment_text', 'sentiment_score', 'sentiment_label']].head())  # Preview
