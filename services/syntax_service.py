import re
from nltk.corpus import stopwords
import nltk


class SyntaxService:

    def __init__(self, text):
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def remove_punctuation(self):
        return re.sub(r'[^\w\s]', '', self.text)

    def to_basic_morph(self):
        basic_words = []
        trimmed_text = self.remove_punctuation()
        word_list = trimmed_text.split()

        for word in word_list:
            word = nltk.WordNetLemmatizer().lemmatize(word, 'v')
            word = nltk.WordNetLemmatizer().lemmatize(word, 'n')

            basic_words.append(word)
        return ' '.join(basic_words)

    def remove_stopwords(self):
        return ' '.join([word for word in self.text.split() if word not in (stopwords.words('english'))])

