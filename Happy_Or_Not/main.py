import re

positive_words = {"happy", "joy", "love", "great", "awesome", "good", "wonderful", "delightful"}
negative_words = {"sad", "hate", "terrible", "bad", "awful", "angry", "horrible", "depressing"}

def analyze_sentiment(text):
    words = [re.sub(r"[^a-z]", "", word) for word in text.split()]
    positive = sum(1 for word in words if word in positive_words)
    negative = sum(1 for word in words if word in negative_words)
    
    if positive > negative:
        return "This seems like a POSITIVE sentence! 😊"
    elif positive == negative:
        return "Hmm... this sentence feels NEUTRAL. 😐"
    else:
        return "This seems like a NEGATIVE sentence. 😢"

# START
with open("Happy_Or_Not/data.txt", "r") as file:
    data = file.readlines()

choice = input("Evaluate each sentence individually [Y/N]? ").upper()

if choice == 'Y':
    for sentence in data:
        print(analyze_sentiment(sentence))
else:
    string_data = ' '.join(data)
    print(analyze_sentiment(string_data))
