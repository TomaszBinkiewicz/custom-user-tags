from django.test import TestCase, Client
from datetime import date

from django.urls import reverse_lazy

from .models import User
from custom_user_tags_app.templatetags.custom_tags import pg_13, bizz_fuzz


class Pg13TestCase(TestCase):

    def setUp(self):
        User.objects.create(username='test_user1', first_name='Young', last_name='User',
                            email='test@example.com', birthday=date(2010, 3, 14))
        User.objects.create(username='test_user2', first_name='Old', last_name='User',
                            email='test_2@example.com', birthday=date(1995, 3, 14))

    def test_pg_13_young(self):
        young_user = User.objects.get(username='test_user1')
        self.assertEqual(pg_13(young_user), 'blocked')

    def test_pg_13_old(self):
        old_user = User.objects.get(username='test_user2')
        self.assertEqual(pg_13(old_user), 'allowed')


class BizzFuzzTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='test_user1', first_name='Some', last_name='User',
                            email='test@example.com', birthday=date(1995, 3, 14), random_number=3)
        User.objects.create(username='test_user2', first_name='Some', last_name='User',
                            email='test_2@example.com', birthday=date(1995, 3, 14), random_number=5)
        User.objects.create(username='test_user3', first_name='Some', last_name='User',
                            email='test_3@example.com', birthday=date(1995, 3, 14), random_number=15)
        User.objects.create(username='test_user4', first_name='Some', last_name='User',
                            email='test_4@example.com', birthday=date(1995, 3, 14), random_number=7)

    def test_bizz_fuzz_3(self):
        user = User.objects.get(username='test_user1')
        self.assertEqual(bizz_fuzz(user), 'Bizz')

    def test_bizz_fuzz_5(self):
        user = User.objects.get(username='test_user2')
        self.assertEqual(bizz_fuzz(user), 'Fuzz')

    def test_bizz_fuzz_15(self):
        user = User.objects.get(username='test_user3')
        self.assertEqual(bizz_fuzz(user), 'BizzFuzz')

    def test_bizz_fuzz_7(self):
        user = User.objects.get(username='test_user4')
        self.assertEqual(bizz_fuzz(user), 7)


class EmptyUserListViewTestCase(TestCase):

    def test_user_list_view_empty(self):
        c = Client()
        response = c.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No users yet.')


class UserListViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='test_user1', first_name='Some', last_name='User',
                            email='test@example.com', birthday=date(1995, 3, 14), random_number=3)
        User.objects.create(username='test_user2', first_name='Some', last_name='User',
                            email='test_2@example.com', birthday=date(1995, 3, 14), random_number=5)

    def test_user_list_view(self):
        c = Client()
        response = c.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], ['<User: test_user1>', '<User: test_user2>'])


class UserCreateViewTestCase(TestCase):

    def test_create_user_view_get(self):
        c = Client()
        response = c.get('/users/add')
        self.assertEqual(response.status_code, 200)

    def test_create_user_view_post(self):
        c = Client()
        response = c.post('/users/add', {'username': 'new_nick', 'first_name': 'Some', 'last_name': 'User',
                                         'email': 'test_2@example.com', 'birthday': date(1995, 3, 14), })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(User.objects.all()), 1)
        self.assertQuerysetEqual(User.objects.all(), ['<User: new_nick>'])


class UserUpdateViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='test_user1', first_name='Some', last_name='User',
                            email='test@example.com', birthday=date(1995, 3, 14), random_number=3)

    def test_update_user_view_get(self):
        c = Client()
        response = c.get('/users/edit/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], User.objects.get(id=1))

    def test_update_user_view_post(self):
        c = Client()
        response = c.post('/users/edit/1', {'username': 'new_nick', 'first_name': 'Some', 'last_name': 'User',
                                            'email': 'test@example.com', 'birthday': date(1995, 3, 14)})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.get(id=1).username, 'new_nick')


class UserDetailViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='test_user1', first_name='Some', last_name='User',
                            email='test@example.com', birthday=date(1995, 3, 14), random_number=3)

    def test_detail_user_view(self):
        c = Client()
        response = c.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], User.objects.get(id=1))


class UserDeleteViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='test_user1', first_name='Some', last_name='User',
                            email='test@example.com', birthday=date(1995, 3, 14))
        User.objects.create(username='test_user2', first_name='Some', last_name='User',
                            email='test@example.com', birthday=date(1995, 3, 14))

    def test_delete_user_view_get(self):
        c = Client()
        response = c.get('/users/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Are you sure you want to delete')
        self.assertEqual(response.context['object'], User.objects.get(id=1))

    def test_delete_user_view_post(self):
        c = Client()
        response = c.post('/users/delete/1')
        self.assertEqual(response.status_code, 302)
        self.assertQuerysetEqual(User.objects.all(), ['<User: test_user2>'])
        self.assertRedirects(response, reverse_lazy('users-list'))
