import re
from collections import Counter

def get_words(paragraph):
    txt = re.sub(r'[^\w\s]', '', paragraph.lower())
  
    words = txt.split()
    counts = Counter(words)

    commons = [word for word, count in counts.most_common(3)]
    print(commons)



s = input("Enter any paragraph: ")

get_words(s)