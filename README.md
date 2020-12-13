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


# Current Situation
1. 对时间, 地点和数字加强判断.
2. what问题几乎无法处理.


<!-- 1. Filter 按照summary的reweight有问题 -->
2. isNumber有待更新
3. how (old|many|much|long) 分开 (!how old)
4. r.summary: high weight; r.url.cut100: low weight.

# Questions

### What Question
What is the educational principle of USTC?  
what is the faculty-to-student ratio in USTC?  
What is the educational aim of USTC?  
what is the most beautiful scenery in USTC?  
what is the name of the human-like robot developed by USTC?  
What is the the major breakthrough of USTC?  
What is the telephone number for the University of Science and Technology of China?  
What is the telephone number for the President's Office of USTC?  
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

### When Question
When was USTC established? <br>
When was USTC relocated to Hefei City? <br>
When did the first Gifted-Young Class of USTC  graduate? <br>
When did USTC launch the NSRL?  <br>
When was USTC selected into project 211? <br>
When was USTC selected into project 985? <br>
When did USTC launch Micius? <br>
When was the 60th anniversary of USTC? <br>
When was USTC selected as National Double First-class initiative? <br>
When did USTC set up the first graduate school in China?<br>
When did President Xi Jinping visited USTC?<br>
When did former President Jiang visited USTC?<br>
When didi former President Jiang Zemin inscribed for USTC?<br>
When was statue of Guo Moruo constructed?<br>
When was School of Physics Science of USTC founded?<br>
When was School of Mathematics Science of USTC founded?<br>
When was School of Computer Science of USTC founded?<br>
When was School of Information Science and Technology of USTC founded?<br>
When was School of Chemistry of USTC founded?<br>
When was School of Earth and Space Sciences of USTC founded?<br>
When was School of Engineering Science of USTC founded?<br>
When was School of Gifted Young of USTC founded?<br>
When was School of Humanities and Social Science of USTC founded?<br>
When was School of Lift Sciences of USTC founded?<br>
When was School of Management of USTC founded?<br>
When was School of Public Affairs of USTC founded?<br>
When was School of Software Engineering of USTC founded?<br>

### Which Question
Which city was USTC founded in? <br>
Which city was USTC relocated to?<br>
Which institution leads USTC?<br>
Which prize is the biggest scholarship of USTC?<br>

### How Question
How was USTC established <br>
How many students in USTC <br>
How many professors in USTC<br>
How is the learning atmosphere in USTC<br>
How is USTC ranked in Nature Index 2020<br>
How is USTC ranked in U.S. News Rankings 2020 <br>
How is USTC ranked in QS World University Rankings 2020 <br>
How long is the Business Hours of the University Hospital in USTC? <br>
How old is Bao Xinhe <br>
How old is Pan Jianwei<br>


### Where Question
Where is the third teaching building of USTC <br>
Where is the second teaching building of USTC <br>
Where is the first teaching building of USTC <br>
Where is the fifth teaching building of USTC <br>
Where is the north gate of the west campus of USTC <br>
Where is the mechanics teaching building of USTC <br>
Where is the electronic teaching building of USTC <br>
Where is the school of life science of USTC <br>
Where is the mini west lake of USTC <br>
Where is the history museum of USTC <br>
Where is the east library of USTC <br>
Where is the west library of USTC <br>
Where is the West Campus Clinic of USTC <br>
Where is the institude of advanced technology of USTC <br>
Where is the middle campus of USTC<br>
Where is the west campus of USTC<br>
Where is the east campus of USTC<br>
Where is USTC established <br>
Where is Lab for Data Science in USTC <br>
Where is the National Synchrotron Radiation Laboratory of China <br>
Where is the office of USTC president<br>
Where is the office buiding of USTC<br>
Where is Pan Jianwei graduated <br>


