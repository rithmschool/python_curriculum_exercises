import unittest
from flask_testing import TestCase
from project import app, db
from project.users.models import User
from project.messages.models import Message

class TestMessage(TestCase):

    def _login_user(self,username='eschoppik',password='secret',follow_redirects=False):
        return self.client.post('/users/login',
            data=dict(username=username,
            password=password), follow_redirects=follow_redirects)

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
        return app

    def setUp(self):
        db.create_all()
        user1 = User("Elie", "Schoppik", "eschoppik", "secret")
        user2 = User("Tim", "Garcia", "tigarcia", "secret")
        user3 = User("Matt", "Lane", "mmmaaatttttt", "secret")
        db.session.add_all([user1, user2, user3])
        message1 = Message("Hello Elie!!", 1)
        message2 = Message("Goodbye Elie!!", 1)
        message3 = Message("Hello Tim!!", 2)
        message4 = Message("Goodbye Tim!!", 2)
        db.session.add_all([message1, message2, message3,message4])
        db.session.commit()
        self._login_user()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_messages_index(self):
        response = self.client.get('/users/1/messages', content_type='html/text', follow_redirects=True)
        self.assertLess(response.status_code, 400)
        self.assertIn(b'Hello Elie!!', response.data)
        self.assertIn(b'Goodbye Elie!!', response.data)

    def test_messages_show(self):
        response = self.client.get('/users/1/messages/1')
        self.assertEqual(response.status_code, 200)

    def test_do_not_messages_show_for_other_users(self):
        response = self.client.get('/users/2/messages/1',follow_redirects=True)
        self.assertIn(b'Not Authorized', response.data)

    def test_messages_create(self):
        response = self.client.post(
            '/users/1/messages/',
            data=dict(text="Hi Matt!!", user_id=1),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hi Matt!!', response.data)

    def test_messages_edit(self):
        response = self.client.get(
            '/users/1/messages/1/edit'
        )
        self.assertIn(b'Hello Elie!!', response.data)

    def test_messages_edit_unauthorized(self):
        response = self.client.get(
            '/users/2/messages/4/edit', follow_redirects=True
        )
        self.assertIn(b'Not Authorized', response.data)

    def test_messages_update(self):
        response = self.client.patch(
            '/users/1/messages/1?_method=PATCH',
            data=dict(text="Welcome Back Elie!"),
            follow_redirects=True
        )
        self.assertIn(b'Welcome Back Elie!', response.data)

    def test_messages_delete(self):
        response = self.client.delete(
            '/users/1/messages/1?_method=DELETE',
            follow_redirects=True
        )
        self.assertNotIn(b'Hello Elie!!', response.data)

if __name__ == '__main__':
    unittest.main()
