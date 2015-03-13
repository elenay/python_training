__author__ = 'eya'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture. session import SessionHelper
from fixture.group import GroupHelper

class Application():

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self. session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_in_new_contact_form(self, contact):
        wd = self.app.wd
        #filling in necessary fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        #submit filled in form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def destroy(self):
        self.app.wd.quit()