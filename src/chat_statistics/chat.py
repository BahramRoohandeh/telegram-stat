import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
from src.data import data_dir
from wordcloud import WordCloud


class chatstats:
    def __init__ (self, chat_json):

        #load chat data
        with open(chat_json) as f:
            self.chat_data = json.load(f)

        #load Stop words
        stop_words = open(data_dir / "stopwords.txt").readlines()
        self.stop_words = list(map(str.strip , stop_words))

    def generate_wordcloud(self, output_dir):
        text_con = ""
        for msg in self.chat_data["messages"]:
            if type(msg['text']) is str:
                text_con += f" {msg['text']}"

        token_text = text_con.split()
        x = Counter(token_text).most_common()[0:2000]

        re_text_con = ""
        for word, num in x:
            re_text_con += f" {word}" * num

        re_text_con_token = re_text_con.split()

        none_SW_tex = ""
        for item in re_text_con_token:
            if not item in self.stop_words:
                none_SW_tex += f" {item}"

        none_SW_tex = Counter(none_SW_tex.split()).most_common()

        final_text = ""
        for word_ , num_ in none_SW_tex:
            final_text += f" {word_}" * num_


        wordcloud = WordCloud(font_path=str(data_dir/"B HOMA_P30DOWNLOAD.COM.TTF"), background_color='white').generate(final_text)
        wordcloud.to_file(str(Path(output_dir) / "pic.png"))


data_obj = chatstats(data_dir/"chat.json")
data_obj.generate_wordcloud(output_dir = str(data_dir))

























print("done")