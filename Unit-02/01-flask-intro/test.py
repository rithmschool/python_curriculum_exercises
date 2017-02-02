from app import app
import unittest

class TestSimpleRoutes(unittest.TestCase):

    def test_welcome(self):
        tester = app.test_client(self)
        response = tester.get('/welcome', content_type='html/text')
        self.assertIn(b'welcome', response.data)
        self.assertEqual(response.status_code, 200)

    def test_welcome_home(self):
        tester = app.test_client(self)
        response = tester.get('/welcome/home', content_type='html/text')
        self.assertIn(b'welcome home', response.data)
        self.assertEqual(response.status_code, 200)

    def test_welcome_back(self):
        tester = app.test_client(self)
        response = tester.get('/welcome/back', content_type='html/text')
        self.assertIn(b'welcome back', response.data)
        self.assertEqual(response.status_code, 200)

    def test_sum(self):
        tester = app.test_client(self)
        response = tester.get('/sum', content_type='html/text')
        self.assertIn(b'10', response.data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()