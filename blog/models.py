from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=200) # заголовок блога
	author = models.ForeignKey(         # юзер написавший блог
		'auth.User' ,
		on_delete=models.CASCADE,
	)
	body = models.TextField()   # тело блога (т.е. основной текст)

	def __str__(self):
		return self.title
 
 