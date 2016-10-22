from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login page loads correctly
    def test_login_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure that login functions with correct data
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"),follow_redirects = True)
        self.assertIn(b"logged in",response.data)

    # Ensure that login functions with incorrect data
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="username", password="admin"), follow_redirects=True)
        self.assertIn(b"try again", response.data)

    # Ensure that logout page functions correctly
    def test_logout_loads(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        response = tester.get('/logout', follow_redirects = True)
        self.assertTrue(b'logged out' in response.data)

    # Ensure main page requires login
    def test_main_page_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', follow_redirects = True)
        self.assertTrue(b'login' in response.data)

        # Ensure that logout page requires user login

    def test_logout_route_requires_login(self):
        tester = app.test_client()
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to login first.', response.data)

        # Ensure that posts show up on the main page

    def test_posts_show_up_on_main_page(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'Hello to you', response.data)

if __name__ == '__main__':
    unittest.main()