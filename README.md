**I haven't had the time to work on this project, the website that was used for scraping has been shut down due to some unknown reason, please do not open issues asking for further updates, stay tuned and check this space for any updates, Thanks.**
# InstaScraper
A Simple Scraper for Instagram public accounts' e-mail addresses. Built using Python2.7 and BeautifulSoup4.
# Requirements
* beautifulsoup4 ``` v4.8.2 ```
* requests ``` v2.22.0 ```
* soupsieve ``` v1.9.5 ```
* cfscrape ``` v2.0.3 ```
* optparse ``` NEW ```
# Instructions
1. Create a new file in the root directory of the project called "input.csv"
2. Run ``` Python Scraper.py ``` in a Terminal (**Linux or Mac**) or Command Prompt window (**Windows**). This may take a while to complete depending on the total number of usernames and your internet speed.
3. the Email Addresses will scraped and stored in a file named "output.csv" in the root directory.

# Latest Changelog
``` 
- Bypassed IP Banning by sending requests through proxy servers.
- Users can now import proxies from a file using -X or --proxy flag
```
Thanks to [Axelu2020](https://www.github.com/axelu2020) for implementing the proxy.
> This software is not affiliated with the official Instagram API in any way whatsoever. The user is liable for any damages caused by the use of this software. This software was developed for educational purposes only.
