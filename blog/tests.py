from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user( # создаем пользователя для теста
			username='testuser',
			email='test@email.com',
			password='secret',
		)

		self.post = Post.objects.create(  # создаем сам тестовый пост
			title='Just a test title',
			author=self.user,
			body='Just a good description',
		)


	def test_string_representation(self):
		post = Post(title='Just a test title')
		self.assertEqual(str(post), post.title)

	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'Just a test title')
		self.assertEqual(f'{self.post.author}', 'testuser')
		self.assertEqual(f'{self.post.body}', 'Just a good description')

	def test_post_list_view(self):  # тестим домашнюю страницу (код состояния http 200, содержит наш основное описание и содержит наш шаблон home.html)
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Just a good description')
		self.assertTemplateUsed(response, 'home.html')

	def test_post_detail_view(self): # проверяем работает ли нужный пост или выдает ошибку 404
		response = self.client.get('/post/1/')
		no_response = self.client.get('/post/100000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'Just a test title')
		self.assertTemplateUsed(response, 'post_detail.html')

