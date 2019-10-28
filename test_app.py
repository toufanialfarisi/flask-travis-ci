import app as my_app
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client()

    def test_index(self):
        response = self.app.get("/")
        not_found = self.app.get("/test")
        assert response.status_code == 200
        assert b"Welcome to index !" in response.data
        assert not_found.status_code == 404

    def test_about(self):
        response = self.app.get("/about")
        assert response.status_code == 200
        assert b"Ini adalah halaman about" in response.data

    def test_contact(self):
        response = self.app.get("/contact")
        assert response.status_code == 200
        assert b"Ini adalah halaman contact" in response.data


if __name__ == "__main__":
    unittest.main()
