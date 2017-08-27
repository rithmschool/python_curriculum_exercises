import unittest
from flask_testing import TestCase
from project import app, db
from project.users.models import User

class TestUser(TestCase):

    def _login_user(self,username='eschoppik',password='secret',follow_redirects=False):
        with self.client:
            return self.client.post('/users/login',
                data=dict(username=username,
                password=password), follow_redirects=follow_redirects)

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///testing.db'
        return app

    def setUp(self):
        user1 = User("Elie", "Schoppik", "eschoppik", "secret")
        user2 = User("Tim", "Garcia", "tigarcia", "secret")
        user3 = User("Matt", "Lane", "mmmaaatttttt", "secret")
        db.create_all()
        db.session.add_all([user1,user2,user3])
        db.session.commit()
        self._login_user()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_users_index(self):
        response = self.client.get('/users', content_type='html/text', follow_redirects=True)
        self.assertLess(response.status_code, 400)
        self.assertIn(b'Elie Schoppik', response.data)
        self.assertIn(b'Tim Garcia', response.data)
        self.assertIn(b'Matt Lane', response.data)

    def test_users_show(self):
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_users_show_unauthorized(self):
        response = self.client.get('/users/2', follow_redirects=True)
        self.assertIn(b'Not Authorized', response.data)

    def test_users_edit(self):
        response = self.client.get(
            '/users/1/edit'
        )
        self.assertIn(b'Elie', response.data)
        self.assertIn(b'Schoppik', response.data)

    def test_users_edit_unauthorized(self):
        response = self.client.get('/users/2/edit', follow_redirects=True)
        self.assertIn(b'Not Authorized', response.data)

    def test_users_delete(self):
        response = self.client.delete(
            '/users/1?_method=DELETE',
            follow_redirects=True
        )
        self.assertNotIn(b'Elie Schoppik', response.data)

    def test_users_delete_unauthorized(self):
        response = self.client.get('/users/2/edit', follow_redirects=True)
        self.assertIn(b'Not Authorized', response.data)

if __name__ == '__main__':
    unittest.main()
