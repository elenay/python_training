from model import contact

__author__ = 'eya'

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
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
        self.fill_in_new_contact_form(contact)
        #submit filled in form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        #edit first contact
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        #modify first name of contact
        self.fill_in_new_contact_form(new_contact_data)
        #submit changes
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        #select first contact
        wd.find_element_by_name("selected[]")
        #delete this contact
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))



