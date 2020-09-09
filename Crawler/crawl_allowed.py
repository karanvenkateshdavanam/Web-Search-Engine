from urllib.request import urlopen
from urllib.parse import urlparse
from urllib import robotparser
import requests

def crawl_legal(url):
    ##parse the URL to get six components scheme://netloc/path;parameters?query#fragment
    parsed_url = urlparse(url)

    #First step we check if the url belongs to .uic.edu the reason for .uic.edu is because there can be links with @uic.edu and bot should stay within .ui.edu domains
    if ".uic.edu" not in parsed_url.netloc:
        return False
    else:
        #here we check the robots.txt - scheme://netloc/robots.txt
        robot_url = parsed_url.scheme+"://"+parsed_url.netloc+"/"+"robots.txt"
        #print(robot_url)
        rp = robotparser.RobotFileParser()
        rp.set_url(robot_url)
        #Reads the robots.txt URL and feeds it to the parser
        try:
            rp.read()
        except:
            return False

        return rp.can_fetch("*", url)
        #return rp.can_fetch("*", url)

#to check if the url is pdf or not
'''def check_url_type(url):
    r = requests.get(url)
    content_type = r.headers.get('content-type')

    if 'text/html' in content_type:
        return True
    else:
        return False'''



'''def main():
    url = "https://uichicago.webex.com/webappng/sites/uichicago/dashboard?siteurl=uichicago"
    crawl_legal(url)   #should return true and
    check_url_type(url)  #should return true

if __name__ == "__main__":
    main()'''
