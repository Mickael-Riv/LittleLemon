from django.test import TestCase
from restaurant.models import Menu

class MenuViewTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for the tests
        self.menu = Menu.objects.create(
            name='Ice Cream',
            price=5,
            description='Delicious vanilla ice cream'
        )
        self.url = 'restaurant/menu/'
        self.client = self.client_class()
        self.client.login(username='testuser', password='testpassword')
        # Create a test user and log in
        self.client.post('/auth/users/', {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.client.post('/auth/token/login/', {
            'username': 'testuser',
            'password': 'testpassword'
        })
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

    def test_get_menu_items(self):
        # Test the GET request to retrieve menu items
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ice Cream')