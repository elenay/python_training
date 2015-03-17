__author__ = 'eya'

def test_delete_contact(app):
    app.contact.open_contacts_page()
    app.contact.delete_first_contact()