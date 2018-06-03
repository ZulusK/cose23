import re
from nltk.corpus import stopwords
import pymorphy2


class NormalizationService:
    def __init__(self, data):
        self.data = data

    def to_lowercase(self, text):
        return text.lower()

    def remove_artifacts(self, post):
        post = re.sub(r'https?://[\S]+', ' url ', post)
        post = re.sub(r'\d+ ?гг?', ' date ', post)
        post = re.sub(r'\d+:\d+(:\d+)?', ' time ', post)
        post = re.sub(r'@\w+', ' tname ', post)
        post = re.sub(r'#\w+', ' htag ', post)
        post = re.sub(r'[\W]+', ' ', post)

        return post

    def to_basic_morph(self, post):
        basic_words = []
        trimmed_text = self.remove_artifacts(post)
        word_list = trimmed_text.split()
        for word in word_list:
            morph = pymorphy2.MorphAnalyzer()
            normalized = morph.parse(word)[0]
            basic_words.append(normalized.normal_form)
        return ' '.join(basic_words)

    def remove_stopwords(self, post):
        return ' '.join([word for word in post.split() if word not in (stopwords.words('russian'))])

    def normalize_text(self):
        for ind in range(self.data.__len__()):
            if self.data[ind] is not None:
                self.data[ind] = self.to_lowercase(self.data[ind])
                self.data[ind] = self.remove_stopwords(self.data[ind])
                self.data[ind] = self.to_basic_morph(self.data[ind])
        return self.data
