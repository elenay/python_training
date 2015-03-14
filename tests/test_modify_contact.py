__author__ = 'eya'

from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contacts_page()
    app.contact.edit_first_contact(Contact("edited-one", "", "", "", ""))
    app.session.logout()
