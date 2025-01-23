"""
File contains tests for the `main.py` application file
"""
from unittest import TestCase

from fastapi.testclient import TestClient

from src.main import app


class TestMain(TestCase):
    """
    Testcase for the `main.py` application file
    """

    app: TestClient

    def setUp(self):
        """
        Sets up ASGI Test App and global variables
        """
        # ASGI Test App
        self.app = TestClient(app)

        # TestCase Global Variables

    def test_has_landing(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("DOCTYPE", response.text)

    def test_has_docs(self):
        response_docs = self.app.get("/docs")
        response_redoc = self.app.get("/redoc")

        self.assertEqual(response_docs.status_code, 200)
        self.assertEqual(response_redoc.status_code, 200)

    def test_has_openapi(self):
        response_openapi = self.app.get("/openapi.json")

        self.assertEqual(response_openapi.status_code, 200)
        self.assertIsInstance(response_openapi.json(), dict)
