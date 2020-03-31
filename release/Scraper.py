from bs4 import BeautifulSoup
from requests import get
import csv
from time import sleep
from array import *
from socket import error as SocketError
import errno
import pytest
import os
import cfscrape
from optparse import *
try :
    from proxylist import ProxyList
except:
    print("pip2 install proxylist ")
try :
    from mechanize import Browser
except:
    print("pip2 install mechanize")
import sys
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import logging
try:
    import mechanize
except:
    print("pip2  install mechanize ")
import random
fileDir = os.path.dirname(os.path.abspath(__file__))   # Directory of the Module

R = '\033[31m'  # red
G = '\033[32m'  # green
# tells the user to use proxy (-X or -- proxy )
use = OptionParser("{} python2 Scraper.py -X yourproxyfile.txt".format(G,R))

use.add_option("-X","--proxy",dest="proxy",help="Proxy list ")
(options,args) = use.parse_args()

#Testing function
#def test_scraper():
#    assert init_scraper() == True
#    print("===========================CODE BUILD SUCCESSFUL===========================")

#Convert list to string
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    # return string
    return str1

#proxy grabber
brows = Browser()
brows.set_handle_robots(False)
brows._factory.is_html = True
brows.set_cookiejar(cookielib.LWPCookieJar())
useragents = [
           'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6']
brows.addheaders = [('User-agent',random.choice(useragents))]
brows.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
proxyList = options.proxy
def proxy():
    logging.basicConfig()
    pl = ProxyList()
    try:
        pl.load_file(proxyList)
    except:
        sys.exit("[!] Proxy file wasn't found, please use -X and specify a proxy file.")
    pl.random()
    getProxy = pl.random().address()
    brows.set_proxies(proxies={"https": getProxy})
    # skips bad proxies (10 seconds is the limit for the proxy)
    try:
        checkProxyIP = brows.open("https://api.ipify.org/?format=raw", timeout=10)
    except:
        return proxy()

proxies = proxy()
#Decode Cloudflare Email Obfuscation


def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)
    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16) ^ k)
    #print de
    return de

def init_scraper():
    emails = []
    proxy = proxies
    user = 0
    found_emails = 0
    email_not_exist = 0
    f = open(fileDir + '/input.csv')
    csv_f = csv.reader(f)
    for row in csv_f:
        user += 1
        sleep(1)
        listToString(row)
        try:
            #Get Cloudflare tokens with proxy
            scraper = cfscrape.create_scraper()
            response = scraper.get(
                "https://www.theinstaprofile.com/email/" + listToString(row), proxies={"https": proxy})
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise
            pass
            print('The host has reset the connection due to rate limits.')
        soup = BeautifulSoup(response.content, 'html.parser')
        h = soup.findAll('h1')
        #print h
        #print h
        try:
            a = h[1].find('a', href='/cdn-cgi/l/email-protection')
            decode = a['data-cfemail']
            print('Found! for: ' + listToString(row))
            print listToString(row), decodeEmail(decode)
            emails.append([listToString(row), decodeEmail(decode)])
            found_emails += 1
            #print emails
        except:
            print('Not found for influencer: ' + listToString(row))
            emails.append([listToString(row), 'null'])
            email_not_exist += 1
            #print emails
    with open("Output.csv", "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        for i in range(len(emails)):
            if (emails[i][1] != 'null'):
                csvWriter.writerow(emails[i])
            else:
                pass
    print('Total Emails Found: ' + str(found_emails))
    print('Total Emails NOT Found: ' + str(email_not_exist))
    return True
init_scraper()
