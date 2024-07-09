import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline
from nltk.tokenize import sent_tokenize

# Download necessary resources
nltk.download('vader_lexicon')
nltk.download('punkt')

# VADER Sentiment Analysis
def analyze_sentiment_vader(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    return scores

# RoBERTa Sentiment Analysis
def analyze_sentiment_roberta(text):
    sentiment_pipeline = pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment')
    results = sentiment_pipeline(text)
    return results

# Function to process the paragraph
def process_paragraph(paragraph):
    sentences = sent_tokenize(paragraph)
    strengths = []
    weaknesses = []

    for sentence in sentences:
        vader_score = analyze_sentiment_vader(sentence)
        roberta_score = analyze_sentiment_roberta(sentence)[0]  # RoBERTa returns a list

        # Using VADER for classification
        if vader_score['compound'] >= 0.05:
            strengths.append((sentence, vader_score, roberta_score))
        elif vader_score['compound'] <= -0.05:
            weaknesses.append((sentence, vader_score, roberta_score))

    return strengths, weaknesses

# Example usage
summary = """You are someone who interprets situations primarily in terms of the logical relation to established rules
of knowledge or order within a given organization. You prefer to solve problems according to the system
of rules rather than by gut intuition. You are comfortable with change, but work well with structure and
order as well. Having a set way of doing things is a good thing to you. You are better at seeing the big
picture and overall operations or direction than you are the actual steps involved in getting it done. You
don't see people as clearly as you could and sometimes this could cause you to ignore their needs in
favor of results or procedures. Overall level of development for the Systems dimension is good while the
Tasks and People dimensions are less developed in comparison. Level of development speaks to your
ability to "see" a specific dimension. The more clearly we see a dimension of thought, the more able we
are to use it; therefore the better we are at it"""

# Process the paragraph
strengths, weaknesses = process_paragraph(summary)

# Display results in a clear and organized manner
print("\nStrengths:")
for sentence, vader_score, roberta_score in strengths:
    print(f"Sentence: {sentence}")
    print(f"VADER Scores: {vader_score}")
    print(f"RoBERTa Scores: {roberta_score}")
    print()

print("\nWeaknesses:")
for sentence, vader_score, roberta_score in weaknesses:
    print(f"Sentence: {sentence}")
    print(f"VADER Scores: {vader_score}")
    print(f"RoBERTa Scores: {roberta_score}")
    print()
