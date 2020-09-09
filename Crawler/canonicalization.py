from urllib.parse import urlparse

def clean_url(url):
    url = url.strip()
    parsed_url = urlparse(url)
    if len(parsed_url.fragment) > 0:
        url = url.rsplit('#'+parsed_url.fragment)[0]

    if url.endswith('/'):
        url = url[:-1]
        url = url.strip()

    #remove www. from because most uic.edu url don't have www.
    if "www." in url:
        url = url.replace("www.","",1)
        url = url.strip()


    return url
