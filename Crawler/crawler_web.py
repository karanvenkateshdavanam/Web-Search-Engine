from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
from crawl_allowed import crawl_legal
from canonicalization import clean_url
import re
from request_parser import parse_write_page
import pickle
import os
import time
from build_adj_graph import create_adj_graph
from pageRank import page_rank
from space_vector_model import vector_calculation_call

url = "https://www.cs.uic.edu/"
# a queue of urls to be crawled
new_urls = deque([url])

# a set of urls that we have already been processed
processed_urls = set()
# a set of domains inside the target website
local_urls = set()
# a set of domains outside the target website
foreign_urls = set()
# a set of broken urls
broken_urls = set()
visited_urls = []
count = 0
file_link = {}
adj_link = {}
# process urls one by one until we exhaust the queue
parent_dir = os.path.dirname(os.path.realpath(__file__))
directory = "htmlcontent"
dir_path = os.path.join(parent_dir, directory)
os.mkdir(dir_path)
while len(new_urls) > 0 and count<=4000:
    #pg_count = pg_count + 1
    url = new_urls.popleft()
    if crawl_legal(url):                  #and check_url_type(url)
        url_clean = clean_url(url)
        if url_clean.startswith("http://"):
            add_url = url_clean.replace("http://","",1)
            add_url = add_url.strip()
        if url_clean.startswith("https://"):
            add_url = url_clean.replace("https://","",1)
            add_url = add_url.strip()

        if add_url not in visited_urls:
            try:
                response = requests.get(url_clean)
                if response.status_code != 200:
                    continue
                #r = requests.get(url)
                content_type = response.headers.get('content-type')
                if 'text/html' not in content_type:
                    continue
            except: #(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
                broken_urls.add(url_clean)
                continue
            #print(url_clean)
            parts = urlsplit(url_clean)
            base = "{0.netloc}".format(parts)
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = url_clean[:url_clean.rfind('/')+1] if '/' in parts.path else url_clean

            soup = BeautifulSoup(response.text, "lxml")
            file_name = parse_write_page(dir_path,soup)
            file_link[file_name] = url_clean

            adj_link.setdefault(url_clean, [])

            for link in soup.find_all('a'):
                # extract link url from the anchor
                anchor = link.attrs["href"] if "href" in link.attrs else ''

                if anchor.startswith('tel:') or anchor.startswith('mailto:') or anchor.startswith('#'):
                    continue

                if anchor.startswith('/'):
                    local_link = base_url + anchor
                    #print(local_link)
                    new_urls.append(local_link)
                    adj_link.setdefault(url_clean, []).append(clean_url(local_link))
                #elif anchor.startswith('#'):
                #    local_link = base_url +"/"+anchor
                    #print(local_link)
                    #new_urls.append(local_link)
                elif anchor.startswith('../'):
                    local_link = path + anchor.replace("../","",1)
                    #print(local_link)
                    new_urls.append(local_link)
                    adj_link.setdefault(url_clean, []).append(clean_url(local_link))
                elif base in anchor:
                    #print(anchor)
                    new_urls.append(anchor)
                    adj_link.setdefault(url_clean, []).append(clean_url(anchor))
                elif anchor.startswith('http') or anchor.startswith('https'):
                    #print(anchor)
                    new_urls.append(anchor)
                    adj_link.setdefault(url_clean, []).append(clean_url(anchor))
                else:
                    local_link = base_url +"/"+anchor
                    #print(local_link)
                    new_urls.append(local_link)
                    adj_link.setdefault(url_clean, []).append(clean_url(local_link))
            count = count + 1
        visited_urls.append(add_url)

pickle_out = open("file_link.pickle","wb")
pickle.dump(file_link, pickle_out)
pickle_out.close()

pickle_adj_list = open("adj_link_list.pickle","wb")
pickle.dump(adj_link, pickle_adj_list)
pickle_adj_list.close()

time.sleep(30)
create_adj_graph()

time.sleep(10)
page_rank()

time.sleep(10)
vector_calculation_call()
