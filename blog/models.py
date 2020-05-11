from django.db import models
from django.urls import reverse 


class Post(models.Model):
	title = models.CharField(max_length=200) # заголовок блога
	author = models.ForeignKey(         # юзер написавший блог
		'auth.User' ,
		on_delete=models.CASCADE,
	)
	body = models.TextField()   # тело блога (т.е. основной текст)

	def __str__(self):
		return self.title

	def get_absolute_url(self): # перенаправляем пользователя на страницу его поста
		return reverse('post_detail', args=[str(self.id)])

 
 