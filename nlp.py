from nltk import sent_tokenize, word_tokenize
import nltk
nltk.download('stopwords')
# s = 'Hi! my friend.'
# tokens = sent_tokenize(s)
# for token in tokens:
#     print(token)

s2 = 'The weather is really fucking hot and i want to go for a swim right now!'
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(s2)
tokens = [word for word in tokens if not word in stop_words]
print(tokens)