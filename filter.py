from pattern.en import wordlist
import sys, os, re
import os
os.environ["JAVA_HOME"] = "C:\\Program Files\\Java\\jre1.8.0_271"
from nltk.tag.stanford import StanfordNERTagger
jar = "C:/Users/ls/Desktop/NLP/QA/stanford-ner-4.0.0/stanford-ner-4.0.0.jar"
model="C:/Users/ls/Desktop/NLP/QA/stanford-ner-4.0.0/classifiers/english.conll.4class.distsim.crf.ser.gz"

class Filter(object):

    def __init__(self, queries, grams):
        self._queries = queries
        self._grams = grams
        try:
            data_p = os.path.join('data')
            self._cities = [w for w in open(os.path.join(data_p, 'city.lst')).read().upper().split('\n')]
            self._countries = [w for w in open(os.path.join(data_p, 'country.lst')).read().upper().split('\n')]
            self._males = [w for w in open(os.path.join(data_p, 'person_male.lst')).read().split('\n')]
            self._females = [w for w in open(os.path.join(data_p, 'person_female.lst')).read().split('\n')]
        except:
            print("Error reading list files")
        self.ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

    def isCity(self, w):
        return w.upper() in self._cities

    def isCountry(self, w):
        return w.upper() in self._countries

    def isLocation(self, w):
        return self.isCity(w) or self.isCountry(w)

    def isTime(self, w):
        return w.lower() in wordlist.TIME

    def isnotTime(self, w):
        return w.lower() not in wordlist.TIME

    def isNumber(self, w):

        if w.isdigit():
            return True

        if self.isTime(w):
            return False

        for i in w:
            try:
                import unicodedata
                unicodedata.numeric(i)
                return True
            except (TypeError, ValueError):
                pass

        return False

    def isNotNumber(self, w):
        return not self.isNumber(w)

    def isUpper(self, w):
        return w[0].isupper()

    def isName(self, w):
        return w in self._males or w in self._females

    def isNovel(self, w):
        return w.lower() not in self._queries[-1][0].lower().strip('?').split()

    def isNotNovel(self, w):
        return not self.isNovel(w)

    def reweightGrams(self):
        orig_q = self._queries[-1][0]
        # checks = [self.isNovel] # improve the score of any grams that meet these conditions
        strips = [self.isNotNovel, self.isNotNovel] # decrease the scores of any grams that meet these conditions
        checks = []
        # strips = []
        if re.search('when', orig_q, re.IGNORECASE):
            checks += [self.isTime, self.isTime]
            strips += [self.isName, self.isLocation]
        elif re.search('who', orig_q, re.IGNORECASE):
            checks += [self.isName, self.isUpper]
            strips += [self.isLocation]
        elif re.search('where', orig_q, re.IGNORECASE):
            checks += [self.isUpper, self.isLocation]
            strips += [self.isName, self.isTime, self.isNumber, self.isCountry]
        elif re.search("how (many|much|long)", orig_q, re.IGNORECASE):
            checks += [self.isNumber, self.isTime, self.isNumber]
            strips += [self.isName, self.isLocation]
        elif re.search("how (old)", orig_q, re.IGNORECASE):
            checks += [self.isTime, self.isNumber]
            strips += [self.isLocation, self.isCountry]
        elif re.search("(which|what).*?(country|countries)", orig_q, re.IGNORECASE):
            checks += [self.isUpper, self.isCountry]
            strips += [self.isName]
        elif re.search("(which|what).*?(city|cities)", orig_q, re.IGNORECASE):
            checks += [self.isUpper, self.isCity]
            strips += [self.isName]
        elif re.search("(which|what).*?(rank|number|ratio)", orig_q, re.IGNORECASE):
            checks += [self.isNumber, self.isNumber]
            strips += [self.isName, self.isCity, self.isNotNumber]
        elif re.search("(which|what).*?(name)", orig_q, re.IGNORECASE):
            checks += [self.isName]
            strips += [self.isNumber]
        elif re.search("(which|what)", orig_q, re.IGNORECASE):
            strips += [self.isName, self.isCity, self.isCountry]
        pop_grams = []
        for g in self._grams:
            if len("".join(list(g))) < 3: # 太短的字符串直接舍弃
                pop_grams.append(g)
                continue
            for f in checks:
                passed = 0
                for w in g:
                    if f(w):
                        passed += 1
                self._grams[g] *= (1 + passed)
            for f in strips:
                failed = 0
                for w in g:
                    if f(w):
                        failed += 1
                self._grams[g] /= (1 + failed)
        for gram in pop_grams:
            self._grams.pop(gram)
        return self._grams
