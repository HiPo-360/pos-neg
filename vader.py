import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize

# Download necessary resources
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

# Example usage
summary = """

Rajnish Sharma should not be expected to make quick decisions, but rather to investigate all available
sources of information prior to the decision making process. He is probably better at providing
supportive data and suggestions rather than making decisions. He is a good administrator who
organises well on a daily basis, but who could be less adept at long-term planning. He
dislikes antagonism and interpersonal conflict. He could yield his opinion to avoid confrontation.
In both a social and work sense Rajnish Sharma is likely to be a good team member. He needs clear
guidelines and areas of responsibility. He dislikes having to deal with unexpected time pressures.
There is a tendency for this person to become overly involved with the problems of others. He is likely
to take criticism personally. He may frustrate others by being overly cautious and specific.



"""



# Process the paragraph
strengths, weaknesses, neutral = process_paragraph(summary)

# Display results in a clear and organized manner
print("\nStrengths:")
for sentence, vader_score in strengths:
    print(f"Sentence: {sentence}")
    print(f"VADER Scores: {vader_score}")
    print()

print("\nWeaknesses:")
for sentence, vader_score in weaknesses:
    print(f"Sentence: {sentence}")
    print(f"VADER Scores: {vader_score}")
    print()

print("\nNeutral:")
for sentence, vader_score in neutral:
    print(f"Sentence: {sentence}")
    print(f"VADER Scores: {vader_score}")
    print()
