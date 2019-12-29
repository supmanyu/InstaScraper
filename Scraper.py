from bs4 import BeautifulSoup
from requests import get
import csv
from time import sleep
from array import *
from socket import error as SocketError
import errno
import pytest

@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("Code Build Successful")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass

#Testing function
def test_scraper():
    assert init_scraper() == True
    return test_ok()

#Initialize global variables


#Function to convert list objects to str objects
def listToString(s):   
    str1 = ""   
    for ele in s:  
        str1 += ele      
    return str1

#Decode Cloudflare Email Obfuscation
def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)
    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16)^k)
    return de

def init_scraper():
    emails = []
    user = 0
    found_emails = 0
    email_not_exist = 0
    f = open('input.csv')
    csv_f = csv.reader(f)
    for row in csv_f:
        user +=1
        print('Username #' + str(user))
        sleep(1)
        listToString(row)
        try:
            url = 'https://www.theinstaprofile.com/email/' + listToString(row)
            response = get(url)
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                print('The host has reset the connection due to rate limits.')
        soup = BeautifulSoup(response.text, 'html.parser')
        h = soup.findAll('h1')
        #print h
        try:
            a = h[1].find('a', href='/cdn-cgi/l/email-protection')
            decode = a['data-cfemail']
            print('Found! for: ' + listToString(row))
            emails.append([listToString(row),decodeEmail(decode)])
            found_emails += 1
            #print emails
        except:
            print('Not found for influencer: ' + listToString(row))
            emails.append([listToString(row),'null'])
            email_not_exist += 1
            #print emails
    with open("output.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        for i in range(len(emails)):
            if (emails[i][1] != 'null'):
                csvWriter.writerow(emails[i])
            else:
                pass
    print ('Total Emails Found: ' + str(found_emails))
    print ('Total Emails NOT Found: ' + str(email_not_exist))
    return True

test_scraper()