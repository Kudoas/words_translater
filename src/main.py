import csv
import random
from googletrans import Translator


class WordsTranslater():
    english_words = []
    meanings = []

    def create_words_list(self, source='english-words/words.txt'):
        with open(source, newline='') as f:
            reader = f.readlines()
            for row in reader:
                row = row.split()
                if len(row) == 1:
                    self.english_words.append(row[0])
                elif len(row) == 2:
                    self.english_words.append(row[1])

    def shuffle_words_list(self):
        random.shuffle(self.english_words)

    # googletransの仕様で一気に多くの単語を処理できない
    def translate_words(self, n=100):
        for i in range(n):
            translator = Translator()
            trans_de_ja = translator.translate(
                self.english_words[i], src='en', dest='ja'
            )
            self.meanings.append(trans_de_ja.text)

    def write_csv(self, output_file='output/output.csv'):
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            for s, t in zip(self.english_words, self.meanings):
                writer.writerow([s, t])


class WordsTestCreater():
    # 作りたいテストの数、問題数を指定
    num_tests = 5
    num_questions = 5

    wrong_options = 3
    words_dict = {}

    def create_words_dict(self, source='output/output.csv'):
        with open(source, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                self.words_dict[row[0]] = row[1]

    def create_words_test(self):
        for i in range(1, self.num_tests+1):
            with open('testfile/第{:02d}回: 英単語テスト'.format(i), 'w') as f:
                f.write('第{:02d}回: 英単語テスト'.format(i))
                f.write('\n\n')

                for num_question in range(self.num_questions):
                    quetion_word = random.choice(list(self.words_dict.keys()))
                    correct_answer = self.words_dict[quetion_word]

                    copy_meanings = list(self.words_dict.values()).copy()
                    copy_meanings.remove(correct_answer)
                    wrong_answers = random.sample(
                        copy_meanings, self.wrong_options
                    )
                    answer_options = [correct_answer] + wrong_answers
                    random.shuffle(answer_options)

                    f.write('問{}. {}'.format(num_question + 1, quetion_word))
                    f.write('\n')
                    for i in range(4):
                        f.write('{}. {}\n'.format(i+1, answer_options[i]))
                    f.write('\n\n')


words_translater = WordsTranslater()
test_creater = WordsTestCreater()

if __name__ == "__main__":
    words_translater.create_words_list()
    words_translater.shuffle_words_list()
    words_translater.translate_words()
    words_translater.write_csv()
    test_creater.create_words_dict()
    test_creater.create_words_test()
