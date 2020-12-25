from pattern.web import Bing, Google, plaintext
from pattern.en import ngrams, wordlist, parsetree
from pattern.metrics import similarity
import operator, re

class Engine(object):

    def __init__(self, provider, key=None):
        if provider.lower() == "bing":
            key = key or 'd6Mz4slIdgIxcKR4609FO+QKOFTEFFRB3i7j8VioPiE'
            self._engine = Bing(license=key)
        elif provider.lower() == "google":
            key = key or 'AIzaSyCAADAKnnkmDwIlLk_Q1p6foqI_ZMrgzcg'
            self._engine = Google(license=key)
        else:
            raise ValueError('Not a recognized provider.')

    def fuzzySearch(self, result, query):
        best, best_i = 0, None
        for i in range(len(result) - len(query) + 1):
            score = similarity(result[i:i+len(query)], query)
            if best < score:
                best = score
                best_i = i
        return result[best_i+len(query):] if best_i != None else ''

    def getPatterns(self, query):
        cleaned = query.strip('?')
        p = [(cleaned, 3)]
        t = parsetree(query)[0]
        for chunk in t.chunks:
            if chunk.pos == 'NP':
                p.append((chunk.string, 2))
        for w in cleaned.split():
            p.append((w, 1))
        return p

    def getGrams(self, results):
        grams = {}
        for all_text, weight in results:
            for text in all_text.replace("·", " ").split(","):
                uni = set(ngrams(text, n=1))
                bi = set(ngrams(text, n=2))
                tri = set(ngrams(text, n=3))
                for gram in uni:
                    grams[gram] = grams.get(gram, 0) + weight
                for gram in bi:
                    grams[gram] = grams.get(gram, 0) + weight
                for gram in tri:
                    grams[gram] = grams.get(gram, 0) + weight
        return grams

    def removeStopWords(self, grams, queries):
        pop_gram = []
        for gram in grams.keys():
            inter = set([g.lower() for g in gram]) & set(wordlist.STOPWORDS)
            if len(inter) > 1 or inter and len(gram) == 1:
                pop_gram.append(gram)
        for gram in pop_gram:
            grams.pop(gram)
        return grams

    def searchQueries(self, queries):
        results = []
        for q, w1, d in queries:
            for r in self._engine.search(q, count=100):
                results.append((re.sub(r'[!,.?]', '', plaintext(r.txt)), w1))
        return results

    def searchQueriesWithPatterns(self, queries):
        # Faster, but still need to refine extraction patterns
        results = []
        for q, w1, d in queries:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(q)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            for r in self._engine.search(q, count=50):
                # Each result is given a preliminary score based on the weight of the query
                # that retrieved it and the pattern that was matched to it
                for p, w2 in self.getPatterns(q):
                    if d == 'L':
                        m = re.search('(.*?)' + p + '.*\.', plaintext(r.txt), re.IGNORECASE)
                    else:
                        m = re.search(p + '(.*)', plaintext(r.txt), re.IGNORECASE)
                    if m:
                        print(plaintext(r.txt))
                        print("-------------------------------------------------")
                        print(p, "generated", m.group(1))
                        print("=================================================")
                        results.append((m.group(1), w1 + w2))
                        break
        return results

    def searchAndGram(self, queries):
        results = self.searchQueries(queries)
        grams = self.getGrams(results)
        grams = self.removeStopWords(grams, queries)
        return grams
