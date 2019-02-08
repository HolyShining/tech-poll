from django.test import TestCase
from .PasswordGenerator import decode


class PasswordGenerator_test_cases(TestCase):
    def test_decoding(self):
        """The decoder works properly"""
        self.assertEqual(decode('password'), "b'¥«,Â\x8aÝ'")
