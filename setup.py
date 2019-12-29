from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='InstaScraper',
    url='https://github.com/supmayu/',
    author='Sahitya Upmanyu ',
    author_email='contact.sahitya@gmail.com',
    # Needed to actually package something
    packages=['release'],
    # Needed for dependencies
    install_requires=['beautifulsoup4'],
    install_requires=['requests'],
    install_requires=['soupsieve'],
    install_requires=['BeautifulSoup'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='GNU GPL V3',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)