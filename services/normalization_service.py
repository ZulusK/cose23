import re
from nltk.corpus import stopwords
import nltk
import pymorphy2

nltk.download('stopwords')

def to_lowercase(text):
    return text.lower()


def remove_punctuation(text):
    return re.sub(r'[^\w\s]', ' ', text)


def to_basic_morph(text):
    basic_words = []
    trimmed_text = remove_punctuation(text)
    word_list = trimmed_text.split()
    morph = pymorphy2.MorphAnalyzer()
    for word in word_list:
        normalized = max(morph.parse(word), key=lambda x: x.score)
        basic_words.append(normalized.normal_form)
    return ' '.join(basic_words)


def remove_artifacts(post):
    post = re.sub(r'https?://[\S]+', ' url ', post)
    post = re.sub(r'\d+ ?гг?', ' date ', post)
    post = re.sub(r'\d+:\d+(:\d+)?', ' time ', post)
    post = re.sub(r'@\w+', ' tname ', post)
    post = re.sub(r'#\w+', ' htag ', post)
    post = re.sub(r'[\W]+', ' ', post)
    return post


def remove_stopwords(text, lang):
    return ' '.join([word for word in text.split() if word not in (stopwords.words('russian'))])


def normalize_text(text, language='russian'):
    data = to_lowercase(text)
    data = to_basic_morph(data)
    data = remove_stopwords(data, language)
    return data


def normalize_data(data):
    for idx, item in enumerate(data):
        # print("Processed %s" % idx)
        if (item != None):
            yield normalize_text(item)
