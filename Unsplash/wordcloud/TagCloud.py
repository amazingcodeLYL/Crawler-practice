from Config import *
import os
import jieba
from collections import Counter
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator


def get_word_list(text, stop_words):
    tmp_word_list = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)
    for myword in liststr.split('/'):
        if not(myword.strip() in stop_words) and len(myword.strip())>1:
            tmp_word_list.append(myword)
    return tmp_word_list


def generate_word_cloud(word_freq_dict):
    print('开始生成词云...')
    background_image = imread(BG_IMAGE_PATH)  # 设置背景图片
    wc = WordCloud(font_path=FONT_PATH,  # 设置字体
                   background_color="white",  # 背景颜色
                   max_words=2000,  # 词云显示的最大词数
                   mask=background_image,  # 设置背景图片
                   max_font_size=100,  # 字体最大值
                   random_state=42,
                   width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                   )


    wc.generate_from_frequencies(word_freq_dict)

    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(background_image)

    plt.figure()
    # 以下代码显示图片
    plt.imshow(wc)

    plt.axis("off")
    plt.show()
    # 绘制词云

    # 保存图片
    wc.to_file(GREY_OUTPUT_PATH)

    image_colors = ImageColorGenerator(background_image)

    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis("off")
    # 绘制背景图片为颜色的图片
    plt.figure()
    plt.imshow(background_image, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()
    # 保存图片
    wc.to_file(PAINTED_OUTPUT_PATH)


def iterate_all_lyrics():
    print('读取敏感词名单...')
    stopwords = [line.strip() for line in open(STOP_WORDS_PATH, 'r',encoding='utf-8').readlines()]
    all_words = []
    print('开始进行分词...')
    for filename in os.listdir('lyrics'):
        with open('lyrics/' + filename, 'r') as f:
            lyrics = f.read()
            lrc_words = get_word_list(lyrics, stopwords)
            all_words.extend(lrc_words)
    return all_words


def get_word_freq(word_list):
    print('开始统计词频...')
    word_freq_dict = {}
    count = Counter(word_list)
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    if len(result) > MAX_WORD:
        result = result[:MAX_WORD]
    for word in result:
        word_freq_dict[word[0]] = word[1]
    return word_freq_dict





