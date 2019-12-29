
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import BeautifulSoup
import keyboard
import time
import random
import csv
from array import *
import json

def login(driver):
    username = "_.supmanyu._"  # <username here>
    password = "runbarryrun3097"  # <password here>
    # Load page
    driver.get("https://www.instagram.com/accounts/login/")
    # Login
    time.sleep(3)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_css_selector("button[type=submit]").click()
    time.sleep(3)

def scrape_followers(driver, account):
    # Load account info page
    driver.get("view-source:https://www.instagram.com/" + str(account[0]) + "/?__a=1")
    content = driver.find_element_by_tag_name('pre').text
    #Save info to JSON
    parsed_json = json.loads(content)
    #Extract No. of users being followed
    maxFollowerCount = parsed_json['graphql']['user']['edge_follow']['count']
    driver.get("https://www.instagram.com/" + str(account[0]))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "following")))
    print ("Accounts following: " + str(maxFollowerCount))
    # Click the 'Follower(s)' link
    driver.find_element_by_partial_link_text("following").click()
    return scroll_follow_list(driver,maxFollowerCount)

def scroll_follow_list(driver,maxFollowerCount): 
    # Wait for the followers modal to load
    time.sleep(2)
    actions = ActionChains(driver)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role=\'dialog\'] ul')))
    FList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
    numberOfFollowersInList = len(FList.find_elements_by_css_selector('li'))
    numberOfFollower_temp = 0
    FList.click()
    actionChain = webdriver.ActionChains(driver)
    time.sleep(random.randint(2,4))
    #Scroll the following list until the end to load all followers
    while (numberOfFollowersInList < maxFollowerCount):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()        
            numberOfFollowersInList = len(FList.find_elements_by_css_selector('li'))
            time.sleep(0.5)
            print(numberOfFollowersInList)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()            
            time.sleep(1)
            if numberOfFollower_temp < numberOfFollowersInList:
                numberOfFollower_temp = numberOfFollowersInList
            else:
                break
    # Finally, scrape the followers
    followers_elems = driver.find_elements_by_class_name("_0imsa")
    return [e.text for e in followers_elems]


if __name__ == "__main__":
    Flist = []
    driver = webdriver.Firefox(executable_path='/home/redrum/Desktop/geckodriver')
    try:
        login(driver)
        f = open('inf_scrapped_null.csv')
        csv_f = csv.reader(f)
        for row in csv_f:
            followers = scrape_followers(driver, row)
            for i in followers:
                Flist.append(i)
            print('Total No. of followers found for user '+ str(row) + ' : ' + str(len(followers)))
        print('Total usernames found: ' + Flist)
        with open("instaScraper_output.csv","w+") as my_csv:
            csvWriter = csv.writer(my_csv,delimiter=',')
            for row in Flist:
                csvWriter.writerow(i)
    finally: 
        driver.quit()