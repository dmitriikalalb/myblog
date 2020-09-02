from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField('Название категории', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField('Название тега', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Author(models.Model):
    image = models.CharField('Фото автора', max_length=255, default='blog-avatar-1.png')
    name = models.CharField('Имя автора', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Article(models.Model):
    image = models.CharField('Фото статьи', max_length=255, default='blog-img-1.jpg')
    title = models.CharField('Название статьи', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    tag1 = models.ForeignKey(Tag, on_delete=models.CASCADE, default=1)
    # tag2 = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # tag3 = models.ForeignKey(Tag, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Дата публикации')
    text = models.TextField('Текс статьи')
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    views = models.IntegerField('Просмотры', default=0)
    is_draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=200)
    pub_date = models.DateTimeField('Дата публикации комментария', default=datetime.now())
    email = models.CharField('Почта', max_length=255, default='unknow@mail.ru')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
