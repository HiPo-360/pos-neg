from flask import Flask, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

# Initialize Flask app
app = Flask(__name__)

# Download necessary NLTK resources
nltk.download('vader_lexicon')
nltk.download('punkt')

# VADER Sentiment Analysis
def analyze_sentiment_vader(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    return scores

# Function to process the paragraph
def process_paragraph(paragraph):
    sentences = sent_tokenize(paragraph)
    strengths = []
    weaknesses = []
    neutral = []

    for sentence in sentences:
        vader_score = analyze_sentiment_vader(sentence)

        # Classify based on VADER compound score
        if vader_score['compound'] >= 0.05:
            strengths.append((sentence, vader_score))
        elif vader_score['compound'] <= -0.05:
            weaknesses.append((sentence, vader_score))
        else:
            neutral.append((sentence, vader_score))

    return strengths, weaknesses, neutral

# Define the API endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    summary = data.get('summary', '')

    if not summary:
        return jsonify({"error": "No summary provided"}), 400

    strengths, weaknesses, neutral = process_paragraph(summary)

    result = {
        "strengths": [{"sentence": s, "vader_scores": vs} for s, vs in strengths],
        "weaknesses": [{"sentence": s, "vader_scores": vs} for s, vs in weaknesses],
        "neutral": [{"sentence": s, "vader_scores": vs} for s, vs in neutral]
    }

    return jsonify(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
