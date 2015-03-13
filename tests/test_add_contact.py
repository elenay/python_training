__author__ = 'eya'

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.fill_in_new_contact_form(Contact("one", "two", "three", "four", "one.threetwo@ww.com"))
    app.session.logout()
