from pattern.search import search
from pattern.en import parsetree, tenses, verbs
from pattern.vector import count
import operator

class Query(object):
    def __init__(self, query):
        self._q = query

    def makeSameTense(self, w1, w2):
        tense = count([i[0] for i in tenses(w2)], stopwords=True)
        tense = sorted(tense, key=operator.itemgetter(2))
        return verbs.conjugate(w1, tense[0])

    def joinGroups(self, match, order):
        words = []
        for i in order:
            if isinstance(i, tuple):
                words.append(self.makeSameTense(match.group(i[1]).string, match.group(i[0]).string))
            else:
                words.append(match.group(i).string)
        return ' '.join(words)

    def getKeyWords(self, t):
        return ' AND '.join([match.string for match in search('NN*|VB*|CD', t)])

    def getQueries(self):
        queries = []
        WP = 'who|what|when|where|why|how|which'
        patterns = [
                # Some verbs are mislabeled as nouns
                # When *+ is used next to NP, it swallows parts of the NP
                # Becuase of this, using {JJ|NN*+} to capture NPs in some cases
                # [NUMS] -> rearrange captured groups in order of NUMS
                # [(x, y)] -> conjugates x into the tense of y
                # ex: [1, (2, 3)] -> "(First Group) (Second Group conjugated to tense of Third Group)"
                (WP + ' {be} {NP}',
                    "queries.append((self.joinGroups(match[0], [2, 1]), 1, 'R'))"),
                (WP + ' {be} {NP} {VB*|NN}',
                    "queries.append((self.joinGroups(match[0], [2, 1, 3]), 3, 'R'))"),
                (WP + ' {be} {NP} {VB*|NN} {*+}',
                    "queries.append((self.joinGroups(match[0], [4, 2, 1, 3]), 4, 'R'))"),
                (WP + ' {do} {NP} {VB*|NN}',
                    "queries.append((self.joinGroups(match[0], [2, (1, 3)]), 5, 'R'))"),
                (WP + ' {do} {NP} {VB*|NN} {*+}',
                    "queries.append((self.joinGroups(match[0], [4, 2, (1, 3)]), 5, 'R'))"),
                (WP + ' {NP} {VB*|NN} {*+}',
                    "queries.append((self.joinGroups(match[0], [1, 3, 2]), 3, 'R'))"),
                (WP + ' {VB*|NN} {JJ|NN*+} {*+}',
                    "queries.append((self.joinGroups(match[0], [3, 2, 1]), 2, 'R'))"),
                (WP + ' {NP} {VB*|NN} {*+}',
                    "queries.append((self.joinGroups(match[0], [2, 1, 3]), 4, 'L'))"),
                (WP + ' {VB*|NN} {JJ|NN*+} {*+}',
                    "queries.append((self.joinGroups(match[0], [1, 2, 3]), 4, 'L'))")
                ]
        i = 0
        while(i < 10):
            try:
                t = parsetree(self._q.strip('?'), lemmata=True)  # lemmata=True
                break
            except:
                i += 1
        for p, c in patterns:
            match = search(p, t)
            if match:
                exec(c)
        return queries + [(self.getKeyWords(t), 1, 'A')] + [(self._q, 2, 'A')]
