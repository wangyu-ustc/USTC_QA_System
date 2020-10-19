import nltk
import indexer
from tqdm import tqdm
from reformulate_query import *
from textrank4zh import TextRank4Keyword, TextRank4Sentence
from best_syn import *
from google_search import *

lch = 2.16   # empirically

def ngrams(lst, n=1):
    """
    Gives all possible n-grams (by defalut 1) from the list of words (lst).
    We can use nltk's in-buit n-gram function also. It returns a list of tuples
    """
    res=[]
    for i in range(len(lst)-n+1):
        res.append(tuple(lst[i:i+n]))
    return res

def ngram_weight(ngram, mark):
    """
    This function returns the weight associated with the ngram parameter.
    This helps in the proper nouns being favoured as results (Since majority of 'Who' functions deal with them)
    """
    num = 0 #holds number of words starting with capitals
    for temp in ngram:
        if temp == temp.capitalize():
            num+=1
    return mark * (WEIGHT_FACTOR**num)

def analyze_query(Question):
    ir_query = indexer.regularize(indexer.tokenizer.tokenize(Question))
    tagged = nltk.pos_tag(ir_query)
    ir_query_tagged = []
    for word, pos in tagged:
        pos = {
            pos.startswith('N'): wordnet.NOUN,
            pos.startswith('V'): wordnet.VERB,
            pos.startswith('J'): wordnet.ADJ,
            pos.startswith('R'): wordnet.ADV,
        }.get(pos, None)
        if pos:
            synsets = wordnet.synsets(word, pos=pos)
        else:
            synsets = wordnet.synsets(word)
        ir_query_tagged.append((word, synsets))
    # # Add additional special hidden term
    # ir_query_tagged.append(('cause', [wordnet.synset('cause.v.01')]))
    return ir_query_tagged

def related_values(synsets, word2):
    related = []
    for net1 in synsets:
        for net2 in wordnet.synsets(word2):
            try:
                lch = net1.lch_similarity(net2)
            except:
                continue
            related.append(lch)
    return related

def compute_score(raw_tokens, ir_query_tagged):
    term_count = 0
    related = []
    causal_match = False
    position = []
    for term, synsets in ir_query_tagged:
        match = False
        term_related = []
        for i, page_term in enumerate(indexer.regularize(raw_tokens)):
            page_term_related = related_values(synsets, page_term)
            if page_term_related:
                term_related.append((max(page_term_related), i))
                if term == page_term or max(page_term_related) >= lch:
                    match = True
        if match:  # above LCH value
            term_count += 1
            if term == 'cause':
                causal_match = True
        if term_related:
            term_related.sort(key=lambda tup: tup[0])
            term_related, i = term_related[-1]  # maximum value
            related.append(term_related)
            position.append(i)
    # return term_count, related, causal_match, position
    return sum(related)

if __name__ == '__main__':
    tr4w = TextRank4Keyword()

    # Question = input("Input a Question:")
    Question = 'Who is the president of USTC?'
    key_list = []
    # get the interrogative of this sentence
    for word in Question.lower().split(' '):
        if word in ['who', 'where', 'how', 'why']:
            key_list.append(word)

    rewrited_queries = reformulated_queries(Question)
    Question = Question[:-1]  # eliminate "?"

    # get the other key words
    tr4w.analyze(text=Question, lower=True, window=2)
    for item in tr4w.get_keywords(20, word_min_len=1):
        # print(item.word, item.weight)
        key_list.append(item.word)

    print(key_list)

    # using key_list[1:] to search in the Internet.
    google_api = GoogleAPI()
    results = google_api.search(' '.join(key_list[1:]))

    # Using the rewrited_queries to search in the result
    # 暂时未考虑一个n_gram多次出现在不同的document中的情况
    n_grams = []
    ir_query_tagged = None
    for result in results:
        # get all the ngrams
        n_grams.extend(ngrams(result.content.split(' '), 1))
        n_grams.extend(ngrams(result.content.split(' '), 2))
        n_grams.extend(ngrams(result.content.split(' '), 3))
        # marks = ngram_weight(n_grams, [WEIGHT_FACTOR] * len(n_grams))
        # get the scores of the n_grams
        ir_query_tagged = analyze_query(Question)
    marks = [ngram_weight(x, WEIGHT_FACTOR) for x in n_grams]
    scores = []
    for raw_token in tqdm(n_grams):
        score = compute_score(raw_token, ir_query_tagged)
        scores.append(score)

    for i, score in enumerate(scores):
        if score > lch:
            print(n_grams[i], "score = ", score)
