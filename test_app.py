import app as my_app
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client()

    def test_home(self):
        result = self.app.get("/")
        not_found = self.app.get("/test")
        assert result.status_code == 200
        assert b"Hallo Travis CI" in result.data
        assert not_found.status_code == 404
        # Make your assertions


if __name__ == "__main__":
    unittest.main()
