from pattern.metrics import similarity
from filter_with_tag import Filter
import operator
import itertools


# This is the implementation of tiling algorithm
# It greedily tiles all the candidates which can be possibly tiled
class Tile(object):

    def __init__(self, grams, query):
        self._grams = grams
        self._query = query
        self._tile = dict()

    def getAnswers(self, cutoff=None):

        # cutoff can be an int or a float,default None which means we need no cutoff operation
        # when it is an int,it selects the top n candidates,else it selects the top n percentile of candidates
        if (type(cutoff) == int):
            sorted_lst = sorted(self._grams.items(), key=operator.itemgetter(1), reverse=True)[:int(cutoff)]
        elif (type(cutoff) == float):
            sorted_lst = sorted(self._grams.items(), key=operator.itemgetter(1), reverse=True)[
                         :int(cutoff * len(self._grams))]
        else:
            RaiseError('Invalid cutoff value')
            return
        self._grams = dict(sorted_lst)

        # if _grams only contains one candidate,there is no need to apply tiling
        if len(sorted_lst) > 1:
            # enum_lst is the list of pairs of candidate
            enum_lst = list(itertools.combinations(sorted_lst, 2))
        else:
            print(self._grams)
            return

        # flag is a condition varible which indicates whether we need further tiling
        flag = 1
        while (flag):
            flag = 0

            if len(enum_lst) > 1000:
                enum_lst = enum_lst[:1000]

            for conb in range(len(enum_lst)):
                length, direction = self.tilecheck(enum_lst[conb][0][0], enum_lst[conb][1][0])
                if (length):
                    if (direction == 'right'):
                        self.tileRight(enum_lst[conb][0], enum_lst[conb][1], length)
                    elif (direction == 'left'):
                        self.tileLeft(enum_lst[conb][0], enum_lst[conb][1], length)
                    flag = 1
            # update the _grams dict with the _tile dict and then reset the _tile dict
            self._grams.update(self._tile)
            self._tile = dict()

            # prepare to get the next round of tiling started
            sorted_lst = sorted(self._grams.items(), key=operator.itemgetter(1), reverse=True)
            self._grams = dict(sorted_lst)
            if len(sorted_lst) > 1:
                enum_lst = list(itertools.combinations(sorted_lst, 2))
            else:
                break

        print(self._grams)

        # reweight the tiled string,here just return the maximun of two candidate weights

    def reweight(self, tiler_val, tilee_val):
        return max(tiler_val, tilee_val)

    def tileLeft(self, tiler, tilee, length):
        if length == 0:
            return
        tiler_str, tiler_val = tiler[0], tiler[1]
        tilee_str, tilee_val = tilee[0], tilee[1]
        tiler_cat = tilee_str + tiler_str[length:]

        # reweight the tiled string
        self._tile[tiler_cat] = self.reweight(tiler_val, tilee_val)
        if (tilee_str in self._grams):
            self._grams.pop(tilee_str)
        if (tiler_str in self._grams):
            self._grams.pop(tiler_str)

    def tileRight(self, tiler, tilee, length):
        if length == 0:
            return
        tiler_str, tiler_val = tiler[0], tiler[1]
        tilee_str, tilee_val = tilee[0], tilee[1]
        tiler_cat = tiler_str + tilee_str[length:]

        self._tile[tiler_cat] = self.reweight(tiler_val, tilee_val)
        if (tilee_str in self._grams):
            self._grams.pop(tilee_str)
        if (tiler_str in self._grams):
            self._grams.pop(tiler_str)

    def tilecheck(self, tiler, tilee):
        minlen = min(len(tiler), len(tilee))
        length = 0
        direction = ''
        for i in range(1, minlen + 1):
            if tiler[:i] == tilee[-i:]:
                length = i
                direction = 'left'
            if tilee[:i] == tiler[-i:]:
                length = i
                direction = 'right'
        return length, direction



