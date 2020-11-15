import argparse, os, sys
sys.path.append(os.path.join(os.path.realpath('..'), 'lib'))

import engine, query, filter, tile

def search(queryinput, key, provider, cutoff, n):
    e = engine.Engine(provider, key)

    q = query.Query(queryinput)
    qs = q.getQueries()

    g = e.searchAndGram(qs)
    f = filter.Filter(qs, g)
    f.reweightGrams()

    t = tile.Tile(g, qs)
    return t.getAnswers(cutoff, n)

def main():
    desc = "QA system using Google/Bing as an information backend"
    parser = argparse.ArgumentParser(description=desc)
    # parser.add_argument('query', help='Question to be answered.')
    parser.add_argument('-k', '--key', default=None,
            help='API key for chosen backend provider')
    parser.add_argument('-p', '--provider', default='google',
            help='choose Bing or Google as a backend, defaults to Bing')
    parser.add_argument('-c', '--cutoff',  default=10, type=int,
            help='cut off for top ranked ngrams to be tiled for the final answer, defaults to 10')
    parser.add_argument('-n', '--nanswers', default=2, type=int,
            help='returns the top n answers (must be less than the cutoff value), defaults to 1')
    args = parser.parse_args()

    # query = input("Question: ")
    query = "Who is the president of China?"
    q, k, p, c, n = query, args.key, args.provider, args.cutoff, args.nanswers
    print(search(q, k, p, c, n))

if __name__ == "__main__": main()
