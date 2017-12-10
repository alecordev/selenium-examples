"""
PhantomJS: http://phantomjs.org/
"""

from selenium import webdriver


class PhantomBrowser():
    def __init__(self):
        self.phantom_browser = webdriver.PhantomJS()

    def __enter__(self):
        return self.phantom_browser

    def __exit__(self, *args, **kwargs):
        self.phantom_browser.quit()


def do():
    with PhantomBrowser() as browser:
        browser.get('https://www.google.com')


def main():
    do()


if __name__ == '__main__':
    main()
