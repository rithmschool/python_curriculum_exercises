import unittest
from flask_testing import TestCase
from project import app, db, bcrypt
from project.users.models import User
from flask import request

class TestAuth(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['HASH_ROUNDS'] = 1
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
        return app

    def setUp(self):
        """Initialize a sqlite DB and seed a user"""
        db.create_all()
        user = User('Elie', 'Schoppik', 'eschoppik', 'secret')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """drop the db after each test"""
        db.session.remove()
        db.drop_all()

    def _login_user(self,username,password,follow_redirects=False):
        return self.client.post('/users/login',
            data=dict(username=username,
            password=password), follow_redirects=follow_redirects)

    def test_user_registeration(self):
        """Ensure user can register"""
        with self.client:
            response = self.client.post('/users/signup', data=dict(
                username='eschoppik2',password='secret2',first_name="Elie2",last_name="Schoppik2"
            ), follow_redirects=True)
            self.assertIn(b'User Created!', response.data)

    def test_incorrect_user_registeration_duplicate_username(self):
        """# Errors are thrown during an incorrect user registration"""
        with self.client:
            response = self.client.post('/users/signup', data=dict(
                username='eschoppik',password='doesnotmatter',first_name="anything",last_name="anything"))
            self.assertIn(b'Username already taken', response.data)
            self.assertIn('/users/signup', request.url)

    def test_check_password(self):
        """ Ensure given password is correct after unhashing """
        user = User.query.filter_by(username='eschoppik').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'secret'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'notsecret'))

    def test_login_page_loads(self):
        """Ensure that the login page loads correctly"""
        response = self.client.get('/users/login')
        self.assertIn(b'Login', response.data)

    def test_correct_login(self):
        """User should be authenticated upon successful login and stored in current user"""
        with self.client:
            response = self.client.post(
                '/users/login',
                data=dict(username="eschoppik", password="secret"),
                follow_redirects=True
            )
            self.assertIn(b'You are now logged in!', response.data)

    def test_incorrect_login(self):
        """The correct flash message is sent when incorrect info is posted"""
        response = self.client.post(
            '/users/login',
            data=dict(username="dsadsa", password="dsadsadsa"),
            follow_redirects=True
        )
        self.assertIn(b"Invalid Credentials", response.data)

    def test_already_logged_in(self):
        """Ensure that logged in user can't log in again"""
        self._login_user('eschoppik','secret')
        response = self.client.get('/users/login',follow_redirects=True)
        self.assertIn(b'You are logged in already', response.data)

    def test_logout(self):
        """Make sure log out actually logs out a user"""
        with self.client:
            self.client.post(
                '/users/login',
                data=dict(username="eschoppik", password="secret"),
                follow_redirects=True
            )
            response = self.client.get('/users/logout', follow_redirects=True)
            self.assertIn(b'Logged Out!', response.data)

    def test_logout_route_requires_login(self):
        """Make sure that you can not log out without being logged in"""
        response = self.client.get('/users/logout', follow_redirects=True)
        self.assertIn(b'Please log in first', response.data)

    def test_edit_password(self):
        """Logged In User Editing Password"""
        self._login_user('eschoppik','secret', follow_redirects=True)
        response = self.client.post('/users/1?_method=PATCH',
            data=dict(username='eschoppik', password='newpass', first_name='ElieAgain', last_name='SchoppikAgain'), follow_redirects=True)
        user = User.query.filter_by(username='eschoppik').first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bcrypt.check_password_hash(user.password, 'newpass'),True)

if __name__ == '__main__':
    unittest.main()
