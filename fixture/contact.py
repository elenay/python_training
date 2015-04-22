__author__ = 'eya'
from model.contact import Contact
import re


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
        self.open_add_contact_page()
        self.fill_in_new_contact_form(contact)
        #submit filled in form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/")):
            wd.find_element_by_link_text("home").click()

    def select_and_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(".//*[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def select_and_edit_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href$='edit.php?id=%s']" % id).click()

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_and_edit_contact_by_index(index)
        #modify first name of contact
        self.fill_in_new_contact_form(new_contact_data)
        #submit changes
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[1]").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_and_edit_contact_by_id(id)
        #modify first name of contact
        self.fill_in_new_contact_form(new_contact_data)
        #submit changes
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/input[1]").click()
        self.contact_cache = None

    def add_contact_by_id_to_group(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        #choose random contact to add
        self.select_contact_by_id(id)
        #select random group to add to
        self.select_random_group_from_list()
        #confirm adding
        wd.find_element_by_xpath("html/body/div/div[4]/form[2]/div[4]/input").click()

    def select_random_group_from_list(self):
        wd = self.app.wd
        index = len(wd.find_elements_by_xpath(".//*[@id='content']/form[2]/div[4]/select/option[]"))
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[4]/select/option[%s]" % index).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        #delete this contact
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        #delete this contact
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                name = cells[2].text
                surname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                email = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(firstname=name, lastname=surname, id=id, email=email,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones,
                                                  address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_tag_name("textarea").text
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        all_text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", all_text).group(1)
        workphone = re.search("W: (.*)", all_text).group(1)
        mobilephone = re.search("M: (.*)", all_text).group(1)
        secondaryphone = re.search("F: (.*)", all_text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)



