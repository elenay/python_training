from sys import maxsize

__author__ = 'eya'

class Contact:

    def __init__(self, firstname=None, lastname=None, email=None, email2=None, email3=None, id=None,
                 homephone=None, workphone=None, mobilephone=None, secondaryphone=None, address=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.id = id
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.lastname, self.firstname, self.email, self.email2, self.email3, self.homephone, self.workphone, self.mobilephone, self.secondaryphone, self.address)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id)
                and ((self.firstname == other.firstname) and (self.lastname == other.lastname)))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize