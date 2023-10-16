def sentiment_analysis(text, sentiment_scores):
    
    words=text.lower().split()
    
    total_score=0
    
    for word in words:
        if word in sentiment_scores:
            total_score+=sentiment_scores[word]
    return total_score


text = "Good and good are two sides of a coin, but excellent always wins."
sentiment_scores = {
    'good': 1,
    'excellent': 2,
    'bad': -1,
    'poor': -2,
    'neutral': 0
}

result = sentiment_analysis(text, sentiment_scores)
print(result)  
