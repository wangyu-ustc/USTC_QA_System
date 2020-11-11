from textrank4zh import TextRank4Keyword, TextRank4Sentence
from best_syn import *

if __name__ == '__main__':
    tr4w = TextRank4Keyword()

    # Question = input("Input a Question:")
    Question = 'Where is USTC?'
    key_list = []
    # get the interrogative of this sentence
    for word in Question.lower().split(' '):
        if word in ['who', 'where', 'how', 'why']:
            key_list.append(word)

    # get the other key words
    tr4w.analyze(text=Question, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        # print(item.word, item.weight)
        key_list.append(item.word)

    print(key_list)

    # using key_list[1:] to search in the Internet.




