import collections
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from PIL import Image

pd.set_option("display.max_columns", 100)


def vectorize(data):
    tfidf_vectorizer = TfidfVectorizer(min_df=1, use_idf=True)
    tfidf_model = tfidf_vectorizer.fit_transform(data)
    idf_df = pd.DataFrame(tfidf_model.toarray(), columns=tfidf_vectorizer.get_feature_names())
    return {
        'vectorizer': tfidf_vectorizer,
        'model': tfidf_model
    }


def form_clusters(data, vectorized_data, clusters=1):
    km_model = KMeans(n_clusters=clusters)
    km_model.fit(vectorized_data["model"])
    clustering = collections.defaultdict(list)
    for idx, label in enumerate(km_model.labels_):
        clustering[label].append(data[idx])

    return clustering


def openPNG(name):
    png = Image.open(name)
    png.load()
    bg = Image.new("RGB", png.size, (255, 255, 255))
    bg.paste(png, mask=png.split()[3])
    return bg


def generate_cloud(data):
    vectorizer_data = vectorize(data)
    clustering = form_clusters(data, vectorizer_data)
    # create coloring from image
    image = openPNG("mask.png")
    alice_colors = np.array(image)
    image_colors = ImageColorGenerator(alice_colors)
    for ind in range(clustering.__len__()):
        wc = WordCloud(
            width=image.width,
            height=image.height,
            relative_scaling=1,
            normalize_plurals=False,
            mask=alice_colors,
            max_words=2000,
            background_color="white")
        wc.generate(' '.join(clustering[ind]))
        # create coloring from image
        wc.recolor(color_func=image_colors)
        wc.to_file("image%s.png" % ind)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.figure()
    plt.show()
