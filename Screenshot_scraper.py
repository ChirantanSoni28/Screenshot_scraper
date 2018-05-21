from selenium import webdriver
import datetime
import sys





def screenshot_scraper():

    query = sys.argv[1]
    path = sys.argv[2]
    today = datetime.date.today()
    name = sys.argv[3]

    location = path + "/" + name + "/" + name + "_" + str(today)
    print(location)

    browser = webdriver.Safari()
    browser.get(query)
    browser.refresh()

    screenshot = browser.save_screenshot(location)
    browser.quit()

screenshot_scraper()