# USTC_QA_System

## Task
retrieve short answers to questions based on the Webs with redundant data.

## Query Reformulation: 
### rewrite the sentence:  
1) split the words  
2) choose keywords and ANDing them  
### assign weight to the strings  
 “associated weights manually” in paper
 Better way?
## N-Gram Mining
put the reformulated parse into search engine and get the summary of web page  
**extract(In Watson's implementation, the passage returned is evaluated within an 20-word window, shifting 6 words at a time)** unigrams, bigrams and trigrams and then score them respectively based on the weight specified aforehand.（say, “eat an apple” wins 5 points）  
sum the n-grams across all the summaries individually  
（say, “eat an apple” appears 3 times in 3 unique summaries, then the final score is 5 * 3 = 15）

<!-- Besides, we can use Sentence offset, Sentence length, Number of named entities as features to estimate the relevence of a passage for a given search query. -->

First, find the known named entity in the database from the relation argument string using a step called entity disambiguation and matching. 

## N-Gram Filtering
assign question types to the query  
decide the collection of filters (How?)  
rescore the n-gram according to their feature relevant to the filter  
## N-Gram Tiling
greedily merges similar answers and assembles longer answers from overlapping smaller answer fragments  
（say, the best answer for now is A*, if n-gram B can merge into A*, then A*U B = B* is optimal; if not, keep the one with a larger score）.  

return the answer 
## Others:
Train a decision tree to judge whether to answer or not.  
Train another decision tree to judge whether a correct answer appears in the top 5 answers

建议先用论文原数据集 https://trec.nist.gov/data/qa/t9_qadata.html 完成以上算法后，再做USTC Web的语料库进行实验，并对比。(会不会来不及

rewrite (using parser tree with nltk) (< 10.20)  
return page summary (google searching engine) and collect the n-grams (<10.30)  
filtering and reweighting (handwritten filters) (<11.10)  
tiling (answer tiling algorithm)  (<11.20)  
(optional) decision tree (<11.30)  

# File Description

| File Name(.py) | Usage |
| :-- | :-- |
|search | main function, including the input and output to the system |
|query | define class Qeury |
|engine | define class Search Engine, so that it will return summaries after inputting a query |
|filter | reweight each n-gram with the certain query and n-gram set |
|tile | greedily tile all the n-grams until exit |

# Question Discription
All_pairs: Full context of all our collected pairs  
good_pairs are the pairs we used for evaluation  
bad_pairs are the pairs that our QA system didn't perform quite well on.
