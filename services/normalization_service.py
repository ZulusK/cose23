import re
from nltk.corpus import stopwords
import pymorphy2


class NormalizationService:

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
            morph = pymorphy2.MorphAnalyzer()
            normalized = morph.parse(word)[0]
            basic_words.append(normalized.normal_form)
        return ' '.join(basic_words)

    def remove_stopwords(self):
        return ' '.join([word for word in self.text.split() if word not in (stopwords.words('russian'))])

