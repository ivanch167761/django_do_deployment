from django.test import TestCase
from django.conf import settings
import os
class mainTest(TestCase):

    def test_envTestFail(self):

        ENV_SECRET_KEY = str(os.environ.get("DJANGO_SECRET_KEY"))

        print(ENV_SECRET_KEY)
        self.assertEqual(settings.SECRET_KEY, 'abcdefg!!A')
    def test_envTestPass(self):

        ENV_SECRET_KEY = str(os.environ.get("DJANGO_SECRET_KEY"))

        print(ENV_SECRET_KEY)
        self.assertEqual(settings.SECRET_KEY, ENV_SECRET_KEY)
