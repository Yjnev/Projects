
# IMPORTS
import re
from collections import Counter
from itertools import islice
import matplotlib.pyplot as plt

# START
with open("data.txt", "r") as file:
    content = file.read()

content = content.lower()
words = content.split()
cleaned_words = [re.sub(r"[^a-z]", "", word) for word in words]
word_counts = Counter(cleaned_words)
sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=1))
most_frequent_words = list(islice(sorted_word_counts.items(), 10))

# Console Printing
print("The top 10 most frequent words:")
for i, (word, count) in enumerate(most_frequent_words, start=1):
    print(f"{i}. [{word}: {count}]")

# Graph Visualization
x_label = [word for word, count in most_frequent_words]
y_label = [count for word, count in most_frequent_words]

plt.figure(figsize=(10, 6))
plt.bar(x_label, y_label, color="skyblue")

plt.xlabel("Word")
plt.ylabel("Frequency")
plt.title("Top 10 Most Frequent Words")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()