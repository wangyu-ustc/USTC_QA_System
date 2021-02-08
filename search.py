import argparse, os, sys
sys.path.append(os.path.join(os.path.realpath('..'), 'lib'))

import engine, query, filter, tile
import NER
import pandas as pd
import evaluation
import operator
def search(queryinput, key, provider, cutoff, n, with_NER=True):
    e = engine.Engine(provider, key)

    q = query.Query(queryinput)
    qs = q.getQueries()
    # qs = [(queryinput, 2, 'A')]

    g = e.searchAndGram(qs)
    f = filter.Filter(qs, g)
    f.reweightGrams()

    # A = dict(sorted(g.items(), key=operator.itemgetter(1), reverse=True)[:int(cutoff)])
    t = tile.Tile(g, qs)
    A = t.getAnswers(cutoff)

    if with_NER:
        nf = NER.Filter(qs, A)
        return nf.get_results()
    else:
        return A

def main():
    desc = "QA system using Google/Bing as an information backend"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-k', '--key', default=None,
            help='API key for chosen backend provider')
    parser.add_argument('-p', '--provider', default='Google',
            help='choose Bing or Google as a backend, defaults to Bing')
    parser.add_argument('-c', '--cutoff',  default=50, type=int,
            help='cut off for top ranked ngrams to be tiled for the final answer, defaults to 10')
    parser.add_argument('-n', '--nanswers', default=2, type=int,
            help='returns the top n answers (must be less than the cutoff value), defaults to 1')
    args = parser.parse_args()

    #############################
    # single sample testing
    query = input("Question:")
    q, k, p, c, n = query, args.key, args.provider, args.cutoff, args.nanswers
    result = search(q, k, p, c, n)
    for idx, (i, score) in enumerate(result.items()):
        print(i, score)
        if idx > 5:
            break

    ###############################
    ###### Evaluation of QA system
    # import Questions
    # All_pairs = Questions.get_good_pairs().strip().split("\n")
    # All_questions = [x.split("--")[0] for x in All_pairs]
    # All_questions = [[i.strip() for i in x.split(",")][0] for x in All_questions]
    #
    # Ground_truth = [x.split("--")[1] for x in All_pairs]
    # Ground_truth = [[i.strip() for i in x.split(",")] for x in Ground_truth]
    #
    # All_results = []
    # All_answers = []
    # for query in All_questions:
    #     All_results.append([query])
    #     All_answers.append([])
    #     try:
    #         q, k, p, c, n = query, args.key, args.provider, args.cutoff, args.nanswers
    #         result = search(q, k, p, c, n)
    #         for i, score in result.items():
    #             print(i, score)
    #             All_answers[-1].append(' '.join(i))
    #             All_results[-1].append(' '.join(i))
    #             if i == 5:
    #                 break
    #     except:
    #         print("something went wrong with Question:", query)
    # pd.DataFrame(All_results).to_csv("C:/Users/ls/Desktop/Answers.csv", header=False, index=False)
    # recall, ndcg = evaluation.test_all_questions(All_answers, Ground_truth, [1, 2, 3, 4, 5], All_questions)
    # print("recall:", recall)
    # print("ndcg:", ndcg)

if __name__ == "__main__": main()
