import sys
import os
import io
import urllib
import socket
import time
import gzip

import re
import random
import types
from filecmp import cmp

from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup

# reload(sys)
# sys.setdefaultencoding('utf-8')

# Load config from .env file
# TODO: Error handling
# try:
#     load_dotenv(find_dotenv(usecwd=True))
#     base_url = os.environ.get('BASE_URL')
#     results_per_page = int(os.environ.get('RESULTS_PER_PAGE'))
# except:
#     print("ERROR: Make sure you have .env file with proper config")
#     sys.exit(1)
base_url = 'https://www.google.com.hk'
results_per_page = 5
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
         (KHTML, like Gecko) Element Browser 5.0',
         'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
         'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
         'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
         Version/6.0 Mobile/10A5355d Safari/8536.25',
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/28.0.1468.0 Safari/537.36',
         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']


# results from the search engine
# basically include url, title,content


class SearchResult:
    def __init__(self):
        self.url = ''
        self.title = ''
        self.content = ''

    def getURL(self):
        return self.url

    def setURL(self, url):
        self.url = url

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content

    def printIt(self, prefix=''):
        print('url\t->', self.url)
        print('title\t->', self.title)
        print('content\t->', self.content)
        print()

    def writeFile(self, filename):
        file = open(filename, 'a')
        try:
            file.write('url:' + self.url + '\n')
            file.write('title:' + self.title + '\n')
            file.write('content:' + self.content + '\n\n')
        except IOError as e:
            print('file error:', e)
        finally:
            file.close()


class GoogleAPI:
    def __init__(self):
        timeout = 40
        socket.setdefaulttimeout(timeout)

    def randomSleep(self):
        sleeptime = random.randint(60, 120)
        time.sleep(sleeptime)

    def extractDomain(self, url):
        """Return string
        extract the domain of a url
        """
        domain = ''
        pattern = re.compile(r'http[s]?://([^/]+)/', re.U | re.M)
        url_match = pattern.search(url)
        if (url_match and url_match.lastindex > 0):
            domain = url_match.group(1)

        return domain

    def extractUrl(self, href):
        """ Return a string
        extract a url from a link
        """
        if href is not None:
            url = ''
            pattern = re.compile(r'(http[s]?://[^&]+)&', re.U | re.M)
            try:
                url_match = pattern.search(href)
            except:
                print(url_match)
            if (url_match and url_match.lastindex > 0):
                url = url_match.group(1)

            return url
        else:
            return ''

    def extractSearchResults(self, html):
        """Return a list
        extract serach results list from downloaded html file
        """
        results = list()
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            if not 'h3' in str(link):
                continue
            # if not link.get('h3 class'):
            #     continue
            result = SearchResult()
            url = link.get('href')
            url = self.extractUrl(url)
            if url == '': continue
            title = link.renderContents()
            title = re.sub(r'<.+?>', '', title.decode())
            result.setURL(url)
            result.setTitle(title)
            # span = li.find('span', {'class': 'st'})
            span = soup.find('span', {'class': 'fYyStc'})
            if span is not None:
                content = span.renderContents()
                content = re.sub(r'<.+?>', '', content.decode())
                result.setContent(content)
            # result.printIt()
            results.append(result.title)

        return results

    def search(self, query, lang='en', num=results_per_page):
        """Return a list of lists
        search web
        @param query -> query key words
        @param lang -> language of search results
        @param num -> number of search results to return
        """
        search_results = list()
        query = urllib.request.quote(query)
        if (num % results_per_page == 0):
            pages = num // results_per_page
        else:
            pages = num // results_per_page + 1

        for p in range(0, pages):
            start = p * results_per_page
            url = '%s/search?hl=%s&num=%d&start=%s&q=%s' % (
                base_url, lang, results_per_page, start, query)
            retry = 3
            while (retry > 0):
                try:
                    request = urllib.request.Request(url)
                    length = len(user_agents)
                    index = random.randint(0, length - 1)
                    user_agent = user_agents[index]
                    request.add_header('User-agent', user_agent)
                    request.add_header('connection', 'keep-alive')
                    # request.add_header('Accept-Encoding', 'gzip')
                    request.add_header('referer', base_url)
                    response = urllib.request.urlopen(request)
                    html = response.read()
                    if (response.headers.get('content-encoding', None) == 'gzip'):
                        html = gzip.GzipFile(
                            fileobj=io.StringIO(html)).read()

                    # url = 'https://www.google.com.hk/search?hl=en&q=%s' % query
                    # request = urllib.request.Request(url)
                    # index = random.randint(0, 9)
                    # user_agent = user_agents[index]
                    # request.add_header('User-agent', user_agent)
                    # response = urllib.request.urlopen(request)
                    # html = response.read()
                    results = self.extractSearchResults(html)
                    assert len(results) > 0, "results is empty"
                    search_results.extend(results)
                    break
                except urllib.request.URLError as e:
                    print('url error:', e)
                    self.randomSleep()
                    retry = retry - 1
                    continue

                except Exception as e:
                    print('error:', e)
                    retry = retry - 1
                    # self.randomSleep()
                    continue
        return search_results


# def load_user_agent():
#     fp = open('./user_agents', 'r')
#
#     line = fp.readline().strip('\n')
#     while (line):
#         user_agents.append(line)
#         line = fp.readline().strip('\n')
#     fp.close()


def crawler():
    # Load use agent string from file
    # load_user_agent()

    # Create a GoogleAPI instance
    api = GoogleAPI()

    # set expect search results to be crawled
    expect_num = 10
    # if no parameters, read query keywords from file
    if (len(sys.argv) < 2):
        # keywords = open('./keywords', 'r')
        keywords = ['USTC president']
        # keyword = keywords.readline()
        for keyword in keywords:
            results = api.search(keyword, num=expect_num)
            print(results)
            # keyword = keywords.readline()
        # keywords.close()
    else:
        keyword = sys.argv[1]
        results = api.search(keyword, num=expect_num)
        print(results)


if __name__ == '__main__':
    crawler()