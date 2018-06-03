import collections
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
pd.set_option("display.max_columns", 100)


class DataProcessor:
    def __init__(self, data):
        self.data = data

    def vectorize(self):
        tfidf_vectorizer = TfidfVectorizer(min_df=1, use_idf=True)
        tfidf_model = tfidf_vectorizer.fit_transform(self.data)
        idf_df = pd.DataFrame(tfidf_model.toarray(), columns=tfidf_vectorizer.get_feature_names())
        print(idf_df)
        return {
            'vectorizer': tfidf_vectorizer,
            'model': tfidf_model
        }

    def form_clusters(self, vectorized_data, clusters=2):
        km_model = KMeans(n_clusters=clusters)
        km_model.fit(vectorized_data["model"])
        clustering = collections.defaultdict(list)
        for idx, label in enumerate(km_model.labels_):
            clustering[label].append(self.data[idx])

        return clustering

    def generate_cloud(self):
        vectorizer_data = self.vectorize()
        clustering = self.form_clusters(vectorizer_data)

        for ind in range(clustering.__len__()):
            wordcloud = WordCloud(width=1920, height=1080, max_words=1628, relative_scaling=1, normalize_plurals=False)\
                .generate(' '.join(clustering[ind]))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.figure()
        plt.show()
