from pattern.en import wordlist
import operator
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

    def isOrganization(self, w, w_tag):
        return (w_tag == 'ORGANIZATION')

    def isLocation(self, w, w_tag):
        return (w_tag == 'LOCATION')


    def isTime(self, w, w_tag):
        return w_tag == 'DATE' or w_tag=='TIME'

    def isName(self, w, w_tag):
        return w_tag == 'PERSON'

    def isMoney(self, w, w_tag):
        return w_tag == 'MONEY'

    def isNone(self, w, w_tag):
        return (w_tag == 'O')

    def reweightGrams(self):
        orig_q = self._queries[-1][0]
        checks = []
        strips = []
        # checks = [self.isNovel] # improve the score of any grams that meet these conditions
        # strips = [self.isNotNovel] # decrease the scores of any grams that meet these conditions
        if re.search('when', orig_q, re.IGNORECASE):
            checks += [self.isTime]
            strips += [self.isName, self.isLocation, self.isOrganization]
        elif re.search('who', orig_q, re.IGNORECASE):
            checks += [self.isName]
            strips += [self.isLocation, self.isOrganization, self.isNone]
        elif re.search('where', orig_q, re.IGNORECASE):
            checks += [self.isLocation]
            strips += [self.isName, self.isTime]
        elif re.search("how (old|many|much)", orig_q, re.IGNORECASE):
            checks += [self.isMoney]
            strips += [self.isName, self.isLocation]
        # elif re.search("(which|what).*?(country|countries)", orig_q, re.IGNORECASE):
        #     strips += [self.isName]
        # elif re.search("(which|what).*?(city|cities)", orig_q, re.IGNORECASE):
        #     strips += [self.isName]
        # elif re.search("(which|what)", orig_q, re.IGNORECASE):
        #     strips += [self.isName]
        for i, g in enumerate(self._grams):
            if (len(checks) + len(strips) == 0): continue
            g_tag = self.ner_tagger.tag(list(g))
            for f in checks:
                passed = 0
                for w, w_tag in g_tag:
                    if f(w, w_tag):
                        passed += 1
                self._grams[g] *= (1 + passed)
            for f in strips:
                failed = 0
                for w, w_tag in g_tag:
                    if f(w, w_tag):
                        failed += 1
                self._grams[g] /= (1 + failed)
            if i >= 10:
                break
        return self._grams

    def get_results(self):
        self.reweightGrams()
        sorted_lst = sorted(self._grams.items(), key=operator.itemgetter(1), reverse=True)
        return dict(sorted_lst)
