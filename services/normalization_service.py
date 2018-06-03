import re
from nltk.corpus import stopwords
import pymorphy2


def to_lowercase(text):
    return text.lower()


def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)


def to_basic_morph(text):
    basic_words = []
    trimmed_text = remove_punctuation(text)
    word_list = trimmed_text.split()
    morph = pymorphy2.MorphAnalyzer()
    for word in word_list:
        normalized = morph.parse(word)[0]
        basic_words.append(normalized.normal_form)
    return ' '.join(basic_words)


def remove_stopwords(text, lang):
    return ' '.join([word for word in text.split() if word not in (stopwords.words(lang))])


def normalize_text(text, language='russian'):
    return to_basic_morph(remove_stopwords(to_lowercase(text)))
