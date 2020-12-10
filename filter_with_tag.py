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

    def isCity(self, w, w_tag):
        return (w.upper() in self._cities) + (w_tag == 'LOCATION')

    def isCountry(self, w, w_tag):
        return (w.upper() in self._countries) + (w_tag == 'LOCATION')

    def isLocation(self, w, w_tag):
        return (self.isCity(w, w_tag) or self.isCountry(w, w_tag))

    def isTime(self, w, w_tag):
        return (w.lower() in wordlist.TIME) + (w_tag == 'DATE' or w_tag=='TIME')

    def isNumber(self, w, w_tag=None):
        return w.isdigit()

    def isUpper(self, w, w_tag=None):
        return w[0].isupper()

    def isName(self, w, w_tag):
        return (w in self._males or w in self._females) + (w_tag == 'PERSON')

    def isNovel(self, w, w_tag=None):
        return w.lower() not in self._queries[-1][0].lower().strip('?').split()

    def isNotNovel(self, w, w_tag=None):
        return not self.isNovel(w)

    def isMoney(self, w, w_tag):
        return self.isNumber(w) + (w_tag == 'MONEY')

    def reweightGrams(self):
        orig_q = self._queries[-1][0]
        checks = [self.isNovel] # improve the score of any grams that meet these conditions
        strips = [self.isNotNovel] # decrease the scores of any grams that meet these conditions
        if re.search('when', orig_q, re.IGNORECASE):
            checks += [self.isTime, self.isNumber]
            strips += [self.isName, self.isLocation]
        elif re.search('who', orig_q, re.IGNORECASE):
            checks += [self.isName, self.isUpper]
            strips += [self.isLocation]
        elif re.search('where', orig_q, re.IGNORECASE):
            checks += [self.isUpper, self.isLocation]
            strips += [self.isName, self.isTime]
        elif re.search("how (old|many|much)", orig_q, re.IGNORECASE):
            checks += [self.isNumber, self.isMoney]
            strips += [self.isName, self.isLocation]
        elif re.search("(which|what).*?(country|countries)", orig_q, re.IGNORECASE):
            checks += [self.isUpper, self.isCountry]
            strips += [self.isName]
        elif re.search("(which|what).*?(city|cities)", orig_q, re.IGNORECASE):
            checks += [self.isUpper, self.isCity]
            strips += [self.isName]
        elif re.search("(which|what)", orig_q, re.IGNORECASE):
            strips += [self.isName]
        for g in self._grams:
            g_tag = self.ner_tagger.tag(list(g))
            for f in checks:
                passed = 0
                for w, w_tag in g_tag:
                    if f(w, w_tag):
                        passed += 1
                self._grams[g] *= (1 + passed)
            for f in strips:
                failed = 0
                for w in g:
                    if f(w, w_tag):
                        failed += 1
                self._grams[g] /= (1 + failed)
        return self._grams
