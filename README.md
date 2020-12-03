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


# Questions

### What Question
What is the educational principle of USTC?  
what is the faculty-to-student ratio in USTC?  
What is the educational aim of USTC?  
what is the most beautiful scenery in USTC?  
what is the name of the human-like robot developed by USTC?  
What is the the major breakthrough of USTC?  
What is the telephone number for the University of Science and Technology of China?  
What is the telephone nunber for the President's Office of USTC?  
What is USTC's rank in QS news?  

### Who Question
Who is the Dean of the School of Computer Science, University of Science and Technology of China?  
Who is the Dean of the School of Information Science and Technology of the USTC?  
Who is the Dean of the School of Chemistry of the USTC?  
Who is the Dean of the School of Earth and Space Sciences of the USTC?  
Who is the Dean of the School of Engineering Science of the USTC?  
Who is the Dean of the School of Gifted Young of the USTC?  
Who is the Dean of the School of Humanities and Social Science of the USTC?  
Who is the Dean of the School of Lift Sciences of the USTC?  
Who is the Dean of the School of Management of the USTC?  
Who is the Dean of the School of Mathematical Sciences of the USTC?  
Who is the Dean of the School of Physical Sciences of the USTC?  
Who is the Dean of the School of Public Affairs of the USTC?  
Who is the Dean of the School of Software Engineering of the USTC?  
Who is the leader of quantum physics in USTC?  