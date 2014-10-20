from django.test import SimpleTestCase
from contact.forms import ContactView

# Create your tests here.

class ContactViewTests(SimpleTestCase):

    def test_displayed_fields(self):
        expected_fields = ['name', 'email', 'topic', 'message']
        self.assertEquals(ContactView.Meta.fields, expected_fields)