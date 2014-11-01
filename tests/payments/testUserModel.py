from django.test import TestCase
from django.db import IntegrityError
from payments.models import User

# Create your tests here.

class UserModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_user = User(email="j@j.com", name='test user',
                             password="pass", last_4_digits="1234")
        cls.test_user.save()

    @classmethod
    def tearDownClass(cls):
        cls.test_user.delete()

    def test_user_to_string_print_email(self):
        self.assertEquals(str(self.test_user), "j@j.com")

    def test_create_user_function_stores_in_database(self):
        user = User.create("test", "test@t.com", "tt", "1234", "22")
        self.assertEquals(User.objects.get(email="test@t.com"), user)

    def test_create_user_already_exists_throws_IntegrityError(self):
        self.assertRaises(
            IntegrityError,
            User.create,
            "test user",
            "j@j.com",
            "jj",
            "1234",
            89
        )

    def test_get_by_id(self):
        self.assertEquals(User.get_by_id(self.test_user.id), self.test_user)
