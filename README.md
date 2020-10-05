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
extract unigrams, bigrams and trigrams and then score them respectively based on the weight specified aforehand.（say, “eat an apple” wins 5 points）  
sum the n-grams across all the summaries individually  
（say, “eat an apple” appears 3 times in 3 unique summaries, then the final score is 5 * 3 = 15）
## N-Gram Filtering
assign question types to the query  
decide the collection of filters How?  
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
