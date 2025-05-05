from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    print("Sentence Overall Rated As", end=" ")
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
    elif sentiment_dict['compound'] <= -0.05:
        print("Negative")
    else:
        print("Neutral")

if __name__ == "__main__":
    sentence = input("Enter a sentence to analyze its sentiment: ")
    sentiment_scores(sentence)
