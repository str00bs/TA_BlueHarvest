"""
File contains tests for 'users' features
"""
from unittest import TestCase

from fastapi.testclient import TestClient

from src.main import app


class TestUsers(TestCase):
    """
    Testcases for 'users' features
    """

    app: TestClient

    def setUp(self):
        """
        Sets up ASGI Test App and global variables
        """
        # ASGI Test App
        self.app = TestClient(app)

        # TestCase Global Variables
