import unittest
from flask_testing import TestCase
from project import app, db, bcrypt
from project.models import User, Message
from flask import request, g, session

class TestUser(TestCase):

    def _login_user(self,username,password,follow_redirects=False):
        return self.client.post('/users/login',
            data=dict(username=username,
            password=password), follow_redirects=follow_redirects)

    def create_app(self):
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["SQLALCHEMY_ECHO"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///usersmessages.db'
        return app

    def setUp(self):
        """Disable CSRF, initialize a sqlite DB and seed a user"""
        db.create_all()
        user = User("Elie", "Schoppik","eschoppik", "secret")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """drop the db after each test"""
        db.drop_all()

    def test_user_registeration(self):
        """Ensure user can register"""
        with self.client:
            response = self.client.post('/users/signup', data=dict(
                username='tigarcia',password='secret',first_name="Tim",last_name="Garcia"
            ), follow_redirects=True)
            self.assertIn(b'User Created!', response.data)
            self.assertEqual(g.current_user.username, "tigarcia")
            # make sure we hash the password!
            self.assertNotEqual(g.current_user.password, "secret")

    def test_incorrect_user_registeration_duplicate_username(self):
        """ Errors are thrown during an incorrect user registration"""
        with self.client:
            response = self.client.post('/users/signup', data=dict(
                username='eschoppik',password='doesnotmatter',first_name="anything",last_name="anything@gmail.com"))
            self.assertIn(b'Username already taken', response.data)
            self.assertIn('/users/signup', request.url)

    def test_get_by_id(self):
        """Ensure id is correct for the current/logged in user"""
        with self.client:
            self.client.post('/users/login', data=dict(
                username="eschoppik", password='secret'
            ), follow_redirects=True)
            self.assertTrue(g.current_user.id == 1)
            self.assertFalse(g.current_user.id == 20)

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


    def test_current_user(self):
        """A current_user variable is created on g when a user is logged in"""
        with self.client:
            self._login_user('eschoppik','secret', True)
            self.assertEqual(g.current_user.username, "eschoppik")

    def test_incorrect_login(self):
        """The correct flash message is sent when incorrect info is posted"""
        response = self.client.post(
            '/users/login',
            data=dict(username="dsadsa", password="dsadsadsa"),
            follow_redirects=True
        )
        self.assertIn(b"Invalid Credentials", response.data)

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

    def testEditPassword(self):
        """Logged In User Editing Password"""
        self._login_user('eschoppik','secret')
        response = self.client.post('/users/1?_method=PATCH',
            data=dict(first_name='a', last_name='b',
            username='bob', password='secret'), follow_redirects=True)
        user = User.query.filter_by(username='bob').first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bcrypt.check_password_hash(user.password, 'secret'),True)

    def test_add_messages(self):
        """Ensure user can add a message"""
        with self.client:
            self._login_user('eschoppik','secret', follow_redirects=True)
            response = self.client.post('/users/1/messages/', data=dict(content='Hello World',user_id=session.get('user_id')), follow_redirects=True)
            self.assertIn(b'Message Created!', response.data)
            message = Message.query.filter_by(content="Hello World").first()
            self.assertEqual(message.user.first_name, "Elie")
            self.assertEqual(message.content,"Hello World")

    def test_edit_messages(self):
        """Ensure user can edit a message"""
        with self.client:
            self._login_user('eschoppik','secret')
            self.client.post('/users/1/messages/', data=dict(content='Hello World',user_id=session.get('user_id'), follow_redirects=True))
            response = self.client.post('/users/1/messages/1?_method=PATCH' , data= dict(
                content="Hello Everyone", user_id=session.get('user_id')
            ), follow_redirects=True)
            self.assertIn(b'Message Updated!', response.data)
            message = Message.query.filter_by(content="Hello Everyone").first()
            self.assertTrue(message.content == "Hello Everyone")
            self.assertTrue(message.user_id == session.get('user_id'))

    def test_delete_message(self):
        """Ensure user can delete a message"""
        with self.client:
            self._login_user('eschoppik','secret')
            self.client.post('/users/1/messages/', data=dict(content='Hello World',user_id=session.get('user_id'), follow_redirects=True))
            response = self.client.post('/users/1/messages/1?_method=DELETE', follow_redirects=True)
            self.assertIn(b'Message Deleted!', response.data)
            message = Message.query.filter_by(content="Hello World").first()
            self.assertFalse(message)

    def test_cannot_modify_another_users_message(self):
        """Ensure user can't edit another user's messages"""
        with self.client:
            self._login_user('eschoppik','secret')
            self.client.post('/users/1/messages', data=dict(content='Hello World',user_id=session.get('user_id'), follow_redirects=True))
            user2 = User("Another", "User", "secret", "secret")
            db.session.add(user2)
            db.session.commit()
            self.client.get('/users/logout', follow_redirects=True)
            self._login_user('secret','secret')
            response = self.client.post('/users/1/messages/1?_method=PATCH' , data= dict(
                text="Here are updated comments.", user_id=session.get('user_id')
            ), follow_redirects=True)
            self.assertIn(b'Not Authorized', response.data)

    def test_cannot_delete_another_users_message(self):
        """Ensure user can't delete another user's messages"""
        with self.client:
            self._login_user('eschoppik','secret')
            self.client.post('/users/1/messages', data=dict(content='Hello World',user_id=session.get('user_id'), follow_redirects=True))
            user2 = User("Another", "User", "secret", "secret")
            db.session.add(user2)
            db.session.commit()
            self.client.get('/users/logout', follow_redirects=True)
            self._login_user('secret','secret')
            response = self.client.post('/users/1/messages/1?_method=DELETE', follow_redirects=True)
            self.assertIn(b'Not Authorized', response.data)

if __name__ == '__main__':
    unittest.main()
