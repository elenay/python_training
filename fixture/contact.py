import time
from model import contact

__author__ = 'eya'
from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php")):
            wd.find_element_by_link_text("add new").click()

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_in_new_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("email", contact.email)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_in_new_contact_form(contact)
        #submit filled in form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/")):
            wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        #edit first contact
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #modify first name of contact
        time.sleep(2)
        self.fill_in_new_contact_form(new_contact_data)
        #submit changes
        time.sleep(2)
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[1]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #delete this contact
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            text = element.find_elements_by_css_selector("td")[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text, id=id))
        return contacts



