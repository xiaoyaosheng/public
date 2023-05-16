from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import jieba.analyse

paper = open("data/paper.txt", encoding="UTF-8").read()

mask = np.array(Image.open('dj.png'))

font = r'C:\Windows\Fonts\simhei.ttf'


# This function takes in your text and your mask and generates a wordcloud.

def generate_wordcloud(tags, mask):
    word_cloud = WordCloud(width=512, height=512, random_state=10, background_color='white', font_path=font,
                           stopwords=STOPWORDS, mask=mask)

    word_cloud.generate_from_frequencies(tags)

    plt.figure(figsize=(10, 8), facecolor='white', edgecolor='blue')

    plt.imshow(word_cloud)

    plt.axis('off')

    plt.tight_layout(pad=0)

    plt.show()


def tokenize_content(content):
    """

        1：去停用词

        2:根据TF-IDF权重来生成词和权重对应的字典

    """

    jieba.analyse.set_stop_words("data/stop_words.txt")

    tags = jieba.analyse.extract_tags(content, topK=50, withWeight=True)

    word_tokens_rank = dict()

    for tag in tags:
        word_tokens_rank[tag[0]] = tag[1]

    return word_tokens_rank


tags = (tokenize_content(paper))

# Run the following to generate your wordcloud

generate_wordcloud(tags, mask)
