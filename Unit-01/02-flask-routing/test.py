from app import app
import unittest

class TestCalculator(unittest.TestCase):

    def test_add(self):
        tester = app.test_client(self)
        response = tester.get('/add/2/2', content_type='html/text')
        self.assertIn(b'4', response.data)
        self.assertEqual(response.status_code, 200)

    def test_subtract(self):
        tester = app.test_client(self)
        response = tester.get('/subtract/2/2', content_type='html/text')
        self.assertIn(b'0', response.data)
        self.assertEqual(response.status_code, 200)

    def test_multiply(self):
        tester = app.test_client(self)
        response = tester.get('/multiply/20/2', content_type='html/text')
        self.assertIn(b'40', response.data)
        self.assertEqual(response.status_code, 200)

    def test_division(self):
        tester = app.test_client(self)
        response = tester.get('/divide/2/2', content_type='html/text')
        self.assertIn(b'1', response.data)
        self.assertEqual(response.status_code, 200)

    def test_all_in_one(self):
        tester = app.test_client(self)
        response = tester.get('/math/add/2/2', content_type='html/text')
        self.assertIn(b'4', response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/math/subtract/2/2', content_type='html/text')
        self.assertIn(b'0', response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/math/multiply/2/20', content_type='html/text')
        self.assertIn(b'40', response.data)
        self.assertEqual(response.status_code, 200)

        response = tester.get('/math/divide/2/2', content_type='html/text')
        self.assertIn(b'1', response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()