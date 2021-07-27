import unittest
from selenium import webdriver
from django.test import TestCase
from gunicorn.config import User


class TestSuite(TestCase):
    def setUp(self):  # вызывается ПЕРЕД каждым тестом.
        self.user = User.objects.create_user(
            username='fatima', password='nikitinoleg24335')

    def test_user_can_login(self):
        response = self.client.post("/login", {"username": "fatima", "password": "nikitinoleg24335"})

    def tearDown(self):  # вызывается ПОСЛЕ каждого теста
        pass
