import csv
import re
from googletrans import Translator


class WordsTranslater():
    english_words = []
    japanese_words = []

    def create_words_list(self, source='english-words/words.txt'):
        with open(source, newline='') as f:
            reader = f.readlines()
            for row in reader:
                row = row.split()
                self.english_words.append(row[1])

    # 1000語を一気にやろうとするとリジェクトされる
    def translate_words(self, n=200):
        for i in range(n):
            translator = Translator()
            trans_de_ja = translator.translate(
                self.english_words[i], src='en', dest='ja'
            )
            self.japanese_words.append(trans_de_ja.text)

    def write_csv(self, output_file='output/output.csv'):
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            for s, t in zip(self.english_words, self.japanese_words):
                writer.writerow([s, t])


words_translater = WordsTranslater()
words_translater.create_words_list()
words_translater.translate_words()
words_translater.write_csv()
