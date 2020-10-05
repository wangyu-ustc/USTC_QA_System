from textrank4zh import TextRank4Keyword, TextRank4Sentence
from best_syn import *

if __name__ == '__main__':
    tr4w = TextRank4Keyword()

    Question = input("Input a Question:")
    tr4w.analyze(text=Question, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        print(item.word, item.weight)



