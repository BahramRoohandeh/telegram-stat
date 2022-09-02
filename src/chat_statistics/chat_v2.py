
import json
from pathlib import Path

import matplotlib.pyplot as plt
from hazm import Normalizer, word_tokenize
from src.data import data_dir
from typing_extensions import Self
from wordcloud import WordCloud


class chat_statics:
    def __init__(self, stopwords= "stopwords.txt", chat_text= "chat.json"):
        
        
        with open(data_dir/stopwords) as sw:
            sw_ = sw.readlines()
            self.stop_words = list(map(str.strip, sw_))


        with open (data_dir/chat_text) as f:
            self.p_data = json.load(f)


    def word_cloud(self, output_dir=data_dir):
        text_content = ""
        for msg in self.p_data['messages']:
            if type(msg['text']) is str:
                 text_content += f" {msg['text']}"

        normalizer = Normalizer()
        text_content = normalizer.normalize(text_content)

        wordcloud = WordCloud(
            stopwords= self.stop_words,
         width = 1000, height = 800, max_font_size=200,
          font_path = str(data_dir/ "B Titr Bold_0.ttf")
          ).generate(text_content)
        
        plt.imshow(wordcloud, interpolation=None)
        plt.axis("off")

        wordcloud.to_file(str(Path(output_dir) / "pic.png"))

        print("image is ready....")


obj1 = chat_statics()
obj1.word_cloud()



 
