from bs4 import BeautifulSoup
from requests import get
import csv
from time import sleep
from array import *
from socket import error as SocketError
import errno

#Convert list to string
def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1

#Decode Cloudflare Email Obfuscation
def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)
    for i in range(2, len(e)-1, 2):
        de += chr(int(e[i:i+2], 16)^k)
    #print de
    return de

emails = []
user = 0
found_emails = 0
email_not_exist = 0
f = open('inf_scrapped_null.csv')
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
            raise
        pass print('The host has reset the connection due to rate limits.')
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
with open("new_file.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    for i in range(len(emails)):
        if (emails[i][1] != 'null'):
            csvWriter.writerow(emails[i])
        else:
            pass
print ('Total Emails Found: ' + str(found_emails))
print ('Total Emails NOT Found: ' + str(email_not_exist))
