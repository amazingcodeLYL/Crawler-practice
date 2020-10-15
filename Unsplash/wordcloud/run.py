from lyricsCrawler import *
import TagCloud


if __name__ == '__main__':
    os.makedirs('./lyrics', exist_ok=True)
    get_song_id(SINGER)
    word_list = TagCloud.iterate_all_lyrics()
    word_freq = TagCloud.get_word_freq(word_list)
    print(word_freq)
    print("###################")
    TagCloud.generate_word_cloud(word_freq)
