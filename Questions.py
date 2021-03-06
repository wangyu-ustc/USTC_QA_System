## discription
# All_pairs: Full context of all our collected pairs
# good_pairs are the pairs we used for evaluation
# bad_pairs are the pairs that our QA system didn't perform quite well on.

All_pairs = """When was USTC established? -- 1958
When was USTC relocated to Hefei City? -- 1970
When did the first Gifted-Young Class of USTC graduate? -- 1978
When did USTC launch the NSRL?  -- 1983
When was USTC selected into project 211? -- 1995
When was USTC selected into project 985? -- 1999
When did USTC launch Micius? -- 2016
When was the 60th anniversary of USTC? -- 2018
When was USTC selected as National Double First-class initiative? -- 2017
When did USTC set up the first graduate school in China? -- 1978
When did President Xi Jinping visited USTC? -- 2016, April 26
When did former President Jiang Zemin visited USTC? -- None
When did former President Jiang Zemin inscribed for USTC? -- 1998
When was statue of Guo Moruo constructed? -- 1988
When was School of Chemistry and Materials Science -- 1996
When was School of Physics Science of USTC founded? -- 2009
When was School of Mathematics Science of USTC founded? -- 2011
When was School of Computer Science of USTC founded? -- 1958
When was School of Chemistry of USTC founded? -- 1996
When was School of Earth and Space Sciences of USTC founded? -- 1978
When was School of Engineering Science of USTC founded? --1998
When was School of Gifted Young of USTC founded? -- 1978
When was School of Humanities and Social Science of USTC founded? --2000
When was School of Lift Sciences of USTC founded? -- 1958
When was School of Public Affairs of USTC founded? -- 2010
When was School of Software Engineering of USTC founded? -- 2001
What is the educational principle of USTC? -- fundamental theories,high-level training
What is the ratio of student to faculty in USTC? -- 8 students per 1 faculty
What is the educational aim of USTC? -- creative atmosphere, higher education, educating top talent
what is the most beautiful scenery in USTC? -- summer,east compus,night
what is the name of the human-like robot developed by USTC? -- Jiajia
What is the the major breakthrough of USTC? -- quantum information,high-temperature superconductivity,nanotechnology
What is the telephone number for the University of Science and Technology of China? -- +86 (551) 360 31 44, 360 31 44, 551-3603144
What is the telephone number for the President's Office of USTC? -- +86-551-63602184, 551-63602184
What is the rank of USTC in QS news? -- 93
What is the rank of USTC in Nature Index 2020? -- eighth, 8, top 10
What is the rank of USTC in U.S. News Rankings 2020? -- 124
What is the rank of USTC in QS World University Rankings 2020? -- 93
Who is the Dean of the School of Computer Science of USTC? -- Xiang-Yang Li, Enhong Chen, 
Who is the Dean of the School of Information Science and Technology of USTC? -- Professor Li Weiping
Who is the Dean of the School of Chemistry of USTC? -- Dou Xiankang,Yujie Xiong
Who is the Dean of the School of Earth and Space Sciences of USTC? --  Chen Xiaofei, Xiaofei Chen Chen Yong, Zheng Yongfei, Huang Jianhua
Who is the Dean of the School of Gifted Young of USTC? -- Chen Yang, Yang Chen
Who is the Dean of the School of Humanities and Social Science of USTC? -- Prof. LIU Dun, Liu Dun
Who is the Dean of the School of Life Sciences of USTC? -- Zhang Guangping
Who is the Dean of the School of Management of USTC? -- Yugang Yu
Who is the Dean of the School of Mathematical Sciences of USTC? -- Li Jiayu, Zuoqin Wang
Who is the Dean of the School of Physical Sciences of USTC? -- Chen Ning Yang
Who is the leader of quantum physics in USTC? -- Jian-wei Pan, Pan Jian-wei
How was USTC established? -- sponsorship，private charity, iahs, 1989
How many students are in USTC? -- 15500, 13794
How many professors are in USTC? -- 528
How is the learning atmosphere in USTC? -- quiet, study, science, technology
How long is the Business Hours of the University Hospital in USTC? -- 24
How old is Bao Xinhe? -- 62, 61, 1959
How old is Pan Jianwei? -- 50
Where is the third teaching building of USTC? -- west campus
Where is the second teaching building of USTC? -- east campus
Where is the first teaching building of USTC? -- east campus
Where is the fifth teaching building of USTC? -- east campus
Where is the north gate of the west campus of USTC? -- west campus
Where is the mechanics teaching building of USTC? -- west campus
Where is the electronic teaching building of USTC? -- west campus
Where is the school of life science of USTC? -- west campus
Where is the history museum of USTC? -- east campus
Where is the east library of USTC? -- east campus
Where is the west library of USTC? -- west campus
Where is the West Campus Clinic of USTC? -- west campus
Where is the institude of advanced technology of USTC? -- hefei, anhui
Where is the middle campus of USTC? -- baohe, baohe district
Where is the west campus of USTC? -- huang shan, huang shan road, hefei
Where is the east campus of USTC? -- jinzhai road, jinzhai, baohe district, baohe
Where is USTC established? -- beijing
Where is Lab for Data Science in USTC? -- huangshan, huangshan road
Where is the National Synchrotron Radiation Laboratory of China? -- ustc, anhui, hefei
Where is the office of USTC president? -- jinzhai road, jinzhai, baohe district, baohe
Where is the office buiding of USTC? -- jinzhai road, jinzhai, baohe district, baohe
Where is Pan Jianwei graduated? -- vienna,  university of vienna, ustc,  university of science and technology of china
Where is the software school of USTC located? --Su Zhou
Who is the first president of USTC? -- Guo Moruo
Which city was USTC founded in? -- Beijing
Which city was USTC relocated to? -- Hefei
Which institution leads USTC? -- CAS
Which prize is the biggest scholarship of USTC? -- Guo Moruo"""

Appended_pairs = """Which person is the first president of USTC? -- Guo Moruo
Which person is the second president of USTC? -- Yan Jici
Which person is the party secretary of USTC? -- Shu Gequn
Which person is the president of USTC? --Bao Xinhe
Which city was the first graduate school in china established in? -- Beijing
Which province is USTC located? -- Anhui
Which province is the software school of USTC located? -- Jiangsu
Which country is USTC located? --China
Which year was USTC established in? -- 1958
Which year was USTC relocated to Hefei City in? -- 1970
Which year did the first Gifted-Young Class of USTC graduate in? -- 1978
Which year did USTC launch the NSRL in?  -- 1983
Which year was USTC selected into project 211 in? -- 1995
Which year was USTC selected into project 985 in? -- 1999
Which year did USTC launch Micius in? -- 2016
Which year was USTC selected as National Double First-class initiative in? -- 2017
Which year did USTC set up the first graduate school in China in? -- 1978
Which campus is the school of life science of USTC in? -- west campus
Which campus is the history museum of USTC in? -- east campus
Which campus is the third teaching building of USTC in? -- west campus
Which campus is the second teaching building of USTC in? -- east campus
Which campus is the first teaching building of USTC in? -- east campus
Which campus is the fifth teaching building of USTC in? -- east campus
Which campus is the north gate of the west campus of USTC in? -- west campus
Which campus is the mechanics teaching building of USTC in? -- west campus
Which campus is the electronic teaching building of USTC in? -- west campus"""

good_pairs = """What is the educational principle of USTC? -- fundamental theories,high-level training
What is the educational aim of USTC? -- creative atmosphere, higher education, educating top talent
What is the telephone number for the University of Science and Technology of China? -- +86 (551) 360 31 44, 360 31 44, 551-3603144
What is the rank of USTC in QS news? -- 93
What is the rank of USTC in Nature Index 2020? -- eighth, 8, top 10
What is the rank of USTC in QS World University Rankings 2020? -- 93
what is the name of the human-like robot developed by USTC? -- Jiajia
Who is the first president of USTC? -- Guo Moruo
Who is the Dean of the School of Computer Science of USTC? -- Xiang-Yang Li, Enhong Chen, 
Who is the Dean of the School of Earth and Space Sciences of USTC? --  Chen Xiaofei, Xiaofei Chen Chen Yong, Zheng Yongfei, Huang Jianhua
Who is the Dean of the School of Gifted Young of USTC? -- Chen Yang, Yang Chen
Who is the Dean of the School of Physical Sciences of USTC? -- Chen Ning Yang
Who is the leader of quantum physics in USTC? -- Jian-wei Pan, Pan Jian-wei
Who is the president of USTC? --Bao Xinhe
How many students are in USTC? -- 15500, 13794
How many campuses do USTC have? -- 5
How old is Bao Xinhe? -- 62, 61, 1959
Where is the third teaching building of USTC? -- west campus
Where is the second teaching building of USTC? -- east campus
Where is the first teaching building of USTC? -- east campus
Where is the mechanics teaching building of USTC? -- west campus
Where is the electronic teaching building of USTC? -- west campus
Where was the first graduate school in china established? -- Beijing
Where is the history museum of USTC? -- east campus
Where is the east library of USTC? -- east campus
Where is the west library of USTC? -- west campus
Where is USTC established? -- beijing
Where is the National Synchrotron Radiation Laboratory of China? -- ustc, anhui, hefei
Where is the National Synchrotron Radiation Laboratory of China? -- ustc, anhui, hefei
Where is the office of USTC president? -- jinzhai road, jinzhai, baohe district, baohe
Where is the software school of USTC located? --Su Zhou
When was USTC established? -- 1958
When was USTC relocated to Hefei City? -- 1970
When did USTC launch Micius? -- 2016
When did USTC set up the first graduate school in China? -- 1978
When did President Xi Jinping visited USTC? -- 2016, April 26
When was School of Mathematics Science of USTC founded? -- 2011
When was School of Chemistry of USTC founded? -- 1996
When was School of Engineering Science of USTC founded? --1998
When was School of Gifted Young of USTC founded? -- 1978
Which city was USTC relocated to? -- Hefei
Which institution leads USTC? -- CAS
"""

bad_pairs = '''what is the ratio of student to faculty in USTC? -- 8 students per 1 faculty
what is the most beautiful scenery in USTC? -- summer,east compus,night
What is the the major breakthrough of USTC? -- quantum information,high-temperature superconductivity,nanotechnology, quantum
What is the telephone number for the President's Office of USTC? -- +86-551-63602184, 551-63602184
What is the rank of USTC in U.S. News Rankings 2020? -- 124
What is the motto of USTC? -- Studying diligently, making progress both in study and development of moral character
What is the founding mission of USTC --to develop a high-level science and technology workforce
What was the campus for graduate study in Beijing renamed? -- the Graduate School of the CAS,  University of Chinese Academy of Sciences
What is the full name of USTC? -- University of Science and Technology of China?
What is the abbreviation of University of Science and Technology of China? -- USTC
What is the abbreviation of School of Gifted Young -- SGY
What is the abbreviation of School of Information Science and Technology -- SIST
Who is the second president of USTC? -- Yan Jici
Who is the party secretary of USTC? -- Shu Gequn
Who is the Dean of the School of Information Science and Technology of USTC? -- Professor Li Weiping
Who is the Dean of the School of Chemistry of USTC? -- Dou Xiankang,Yujie Xiong
Who is the Dean of the School of Humanities and Social Science of USTC? -- Prof. LIU Dun, Liu Dun
Who is the Dean of the School of Life Sciences of USTC? -- Zhang Guangping
Who is the Dean of the School of Management of USTC? -- Yugang Yu
Who is the Dean of the School of Mathematical Sciences of USTC? -- Li Jiayu, Zuoqin Wang
How was USTC established? -- sponsorship，private charity, iahs, 1989
How many professors are in USTC? -- 528
How is the learning atmosphere in USTC? -- quiet, study, science, technology
How long is the Business Hours of the University Hospital in USTC? -- 24
How many schools are in USTC now?  -- 23
How many departments are in USTC now? -- 33
How many books are in USTC’s library?  -- 1.73 million
How old is Pan Jianwei? -- 50
Where is the fifth teaching building of USTC? -- east campus
Where is the north gate of the west campus of USTC? -- west campus
Where is the school of life science of USTC? -- west campus
Where is the West Campus Clinic of USTC? -- west campus
Where is the institude of advanced technology of USTC? -- hefei, anhui
Where is the middle campus of USTC? -- baohe, baohe district
Where is the west campus of USTC? -- huang shan, huang shan road, hefei
Where is the east campus of USTC? -- jinzhai road, jinzhai, baohe district, baohe
Where is Lab for Data Science in USTC? -- huangshan, huangshan road
Where is the office buiding of USTC? -- jinzhai road, jinzhai, baohe district, baohe
Where is Pan Jianwei graduated? -- vienna,  university of vienna, ustc,  university of science and technology of china
When did the first Gifted-Young Class of USTC graduate? -- 1978
When did USTC launch the NSRL?  -- 1983
When was USTC selected into project 211? -- 1995
When was USTC selected into project 985? -- 1999
When was the 60th anniversary of USTC? -- 2018
When was USTC selected as National Double First-class initiative? -- 2017
When did former President Jiang Zemin inscribed for USTC? -- 1998
When was statue of Guo Moruo constructed? -- 1988
When was School of Physics Science of USTC founded? -- 2009
When was School of Computer Science of USTC founded? -- 1958
When was School of Earth and Space Sciences of USTC founded? -- 1978
When was School of Humanities and Social Science of USTC founded? --2000
When was School of Lift Sciences of USTC founded? -- 1958
When was School of Public Affairs of USTC founded? -- 2010
When was School of Software Engineering of USTC founded? -- 2001
When was the campus for graduate study in Hefei established? --1978
When was the Experimental Class of Innovation of USTC was established? --2008
Which city was USTC founded in? -- Beijing
Which prize is the biggest scholarship of USTC? -- Guo Moruo'''

def get_pairs():
    return All_pairs

def get_appended_pairs():
    return Appended_pairs

def get_good_pairs():
    return good_pairs
