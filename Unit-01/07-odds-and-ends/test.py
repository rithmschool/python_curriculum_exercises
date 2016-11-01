import odds_ends
import unittest

class OddsEndsTest(unittest.TestCase):

    def test_get_next_multiple(self):
        g = odds_ends.get_next_multiple(10)
        self.assertEqual(next(g)[0], 20)
        self.assertEqual(next(g)[0], 30)
        self.assertEqual(next(g)[0], 40)

    def test_is_prime(self):
        self.assertEqual(odds_ends.is_prime(11), True)
        self.assertEqual(odds_ends.is_prime(50), False)
        self.assertEqual(odds_ends.is_prime(110), False)

    def test_get_next_prime(self):
        g = odds_ends.get_next_prime(3)
        self.assertEqual(next(g), 5)
        self.assertEqual(next(g), 7)
        self.assertEqual(next(g), 11)

    def test_double_result(self):

        @odds_ends.double_result
        def add(a,b):
            return a+b

        self.assertEqual(add(2,2),8)
        self.assertEqual(add(2,20),44)

    def test_only_even_parameters(self):

        @odds_ends.only_even_parameters
        def add(a,b):
            return a+b

        self.assertEqual(add(2,2),4)
        self.assertEqual(add(2,21),"Please add even numbers")

    def test_sum_index(self):
        self.assertEqual(odds_ends.sum_index([1,2,3,4]),6)
        self.assertEqual(odds_ends.sum_index([1,2,3,4,5,6,7,8,9,10]),45)

    def test_remove_vowels(self):
        self.assertEqual(odds_ends.remove_vowels("awesome"),"wsm")

    def test_collect_email(self):
        self.assertEqual(odds_ends.collect_email("awesome@gmail.com"),"awesome")
        self.assertEqual(odds_ends.collect_email("person@webmail.co.il"),"person")

    def test_collect_domain_name(self):
        self.assertEqual(odds_ends.collect_domain_name("www.example.com"),"example.com")
        self.assertEqual(odds_ends.collect_domain_name("http://www.example.com"),"example.com")

    def test_valid_phone_number(self):
        self.assertEqual(odds_ends.valid_phone_number("123"),False)
        self.assertEqual(odds_ends.valid_phone_number("1-123-333-33"),False)
        self.assertEqual(odds_ends.valid_phone_number("5-223-333-3333"),False)
        self.assertEqual(odds_ends.valid_phone_number("1-123-456-212z"),False)
        self.assertEqual(odds_ends.valid_phone_number("1-123-333-2321"),True)

        self.assertEqual(odds_ends.valid_phone_number("123-333-2321"),True)


if __name__ == '__main__':
    unittest.main()


