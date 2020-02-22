from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='InstaScraper',
    url='https://supmanyu.github.io',
    author='Sahitya Upmanyu ',
    author_email='contact.sahitya@gmail.com',
    # Needed to actually package something
    packages=['release'],
    # Needed for dependencies
    install_requires=['beautifulsoup4','requests','soupsieve','BeautifulSoup','cfscrape'],
    # *strongly* suggested for sharing
    version='0.1.1',
    # The license can be anything you like
    license='GNU GPL V3',
    description='A Instagram email scraper written in python using beautifulSoup.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
