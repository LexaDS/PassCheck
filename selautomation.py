from selenium import webdriver
import time


class selautomation(object):
    # ROBOT_LIBRARY_SCOPE='TEST SUITE'

    def __init__(self):
        self.driver=webdriver.Firefox()
        self.url='#insert chosen url on which the tests will be performed'

    def openbrowser(self):
        return self.driver.get(self.url)

    def login(self,password,user):
        self.driver.find_element_by_xpath('#insert chosen xpath locator').click()
        self.driver.find_element_by_xpath('#insert chosen xpath locator').send_keys(user)
        self.driver.find_element_by_xpath('#insert chosen xpath locator').send_keys(password)
        self.driver.find_element_by_xpath('#insert chosen xpath locator').click()

    def searchitem(self,book_name):
        self.driver.find_element_by_xpath('#insert chosen xpath locator').send_keys(book_name)
        self.driver.find_element_by_xpath('#insert chosen xpath locator').click()

    def checkelement(self,elementpath):
        return self.driver.find_element_by_xpath(elementpath).is_displayed()


    def scrolldown(self):
        return self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scrollup(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)
        self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def clickelem(self, path):
        self.driver.find_element_by_xpath(path).click()

    def closebrowser(self):
        return self.driver.quit()