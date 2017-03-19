import os
import sys
import time
import random

from selenium import webdriver


def log(*args):
    print('{} - {}'.format(time.ctime(), args))


def main(url, drivers_path=None):
    if drivers_path is not None:
        current_path = drivers_path
    else:
        current_path = os.path.dirname(os.path.abspath(__name__))

    log('Looking for drivers in ', current_path)

    os.environ['PATH'] = '{}{}{}'.format(os.environ['PATH'], ':',
                                         current_path)

    while 1:
        driver = None
        try:
            driver = webdriver.Firefox()
            driver.get(url)
            driver.quit()
            interval = random.randint(300, 500)
            log('Waiting for next iteration: ', interval)
            time.sleep(interval)
        except Exception as e:
            log(e)
            if driver is not None:
                driver.quit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        log('Second parameter should be URL to visit.')
        sys.exit(1)

    # Path to drivers
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        main(sys.argv[1])
