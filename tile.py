from pattern.metrics import similarity
from filter_with_tag import Filter
import operator


class Tile(object):

    def __init__(self, grams, query):
        self._grams = grams
        self.query = query

    def joinSimilar(self, t1, t2):
        s1, w1 = t1
        s2, w2 = t2
        if w1 == 0 or w2 == 0: return #already previously merged
        sim = similarity(' '.join(s1), ' '.join(s2))
        if sim > .75 and sim != 1:
            if w1 > w2:
                self._grams[s2] = 0
                self._grams[s1] += w2
            else:
                self._grams[s1] = 0
                self._grams[s2] += w1

    def first(self, t, l):
        return [i[:l] for i in t]

    def last(self, t, l):
        return [i[-l:] for i in t]

    def tileRight(self, t, s, l):
        while s[-2:] in self.first(t, l):
            for i in t:
                if s[-l:] == i[:l]:
                    part = max(len(i) - l, 0)
                    if part:
                        s += i[-part:]
                    t.remove(i)
                    break
        return s

    def tileLeft(self, t, s, l):
        while s[:l] in self.last(t, l):
            for i in t:
                if s[:l] == i[-l:]:
                    part = max(len(i) - l, 0)
                    if part:
                        s = i[:part] + s
                    t.remove(i)
                    break
        return s

    def mergeIden(self, t1, t2):
        # t1 is a 1-gram
        if t1[0][0] in t2[0]:
            self._grams[t2[0]] += self._grams.pop([t1[0]])

    def getAnswers(self, cutoff, n):
        sl = sorted(self._grams.items(), key=operator.itemgetter(1))
        for t1 in sl[-cutoff*n:]:
            for t2 in sl:
                self.joinSimilar(t1, t2)
                if len(t2) == 1:
                    self.mergeIden(t2, t1)
        sl = sorted(self._grams.items(), key=operator.itemgetter(1))


        t = list(reversed([i for i in sl]))[:cutoff]

        # extra filtering
        extra_filter = Filter(self.query, dict(t))
        extra_filter.reweightGrams()
        sl = sorted(extra_filter._grams.items(), key=operator.itemgetter(1))
        t = list(reversed([i[0] for i in sl]))

        ans = []
        n = min(n, cutoff)
        for i in range(n):
            s = t.pop(0)
            if len(s) > 1:
                s = self.tileLeft(t, s, 2)
                s = self.tileRight(t, s, 2)
            else:
                s = self.tileLeft(t, s, 1)
                s = self.tileLeft(t, s, 1)
            ans.append(' '.join(s))
        return ans
