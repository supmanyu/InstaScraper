# WARNING: THIS SCRAPER IS NOT COMPATIBLE WITH PYTHON3 YET. ANY ISSUES REGARDING VERSIONING WILL NOT BE REPLIED TO AND CLOSED IMMEDIATELY. 
# InstaScraper
A Simple Scraper for Instagram public accounts' e-mail addresses. Built using Python2.7 and BeautifulSoup4.
# Requirements
* beautifulsoup4 ``` v4.8.2 ```
* requests ``` v2.22.0 ```
* soupsieve ``` v1.9.5 ```
* cfscrape ``` v2.0.3 ``` ``` NEW ```
# Instructions
1. Create a new file in the root directory of the project called "input.csv"
2. Run ``` Python Scraper.py ``` in a Terminal (**Linux or Mac**) or Command Prompt window (**Windows**). This may take a while to complete depending on the total number of usernames.
3. the Email Addresses will scraped and stored in a file named "output.csv" in the root directory.

# Latest Changelog
``` 
- Updated scraping algorithm to bypass cloudflare Javascript based bot protection
- Updated tests (Removed linting with flake8)
- Updated Setup.py (Added cfscrape to dependencies)
```
> This software is not affiliated with the official Instagram API in any way whatsoever. The user is reliable for any damages caused by the use of this software. This software was developed for educational purposes only.
