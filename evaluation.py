import math

def test_all_questions(Candidates, Answers, topN, Questions):
    """
    :param Candidates: list of list of strings: e.g. [["a", "b"], ["c", "d"]]
    :param Answers: list of strings: e.g. ["a", "b"]
    :param topN: e.g. [2, 5]
    :return: recall and ndcg
    """
    recall = []
    NDCG = []
    for index in range(len(topN)):
        sumForRecall = 0
        sumForNdcg = 0
        for i in range(len(Candidates)):
            if len(Answers[i]) != 0:
                userHit = 0
                dcg = 0
                idcg = 0
                idcgCount = len(Answers[i])
                ndcg = 0
                for j in range(topN[index]):
                    if j >= len(Candidates[i]): continue
                    break_flag = 0
                    for answer in Answers[i]:
                        if answer.lower() in Candidates[i][j].lower():
                            # if Hit!
                            dcg += 1.0 / math.log2(j + 2)
                            if break_flag == 0:
                                userHit += 1
                                break_flag = 1
                            break
                    if idcgCount > 0:
                        idcg += 1.0 / math.log2(j + 2)
                        idcgCount = idcgCount - 1
                    if break_flag == 1:
                        break

                if (idcg != 0):
                    ndcg += (dcg / idcg)

                if dcg == 0:
                    print("question index:", i)

                sumForRecall += userHit
                sumForNdcg += ndcg

        recall.append(sumForRecall / len(Candidates))
        NDCG.append(sumForNdcg / len(Candidates))
    return recall, NDCG