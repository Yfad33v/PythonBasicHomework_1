from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=244,  unique=True, blank=False)

    def __str__(self):
        return f'{self.group_name} '


class Article(models.Model):
    art_name = models.CharField(max_length=64, unique=True, blank=True)
    price = models.FloatField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.art_name}, цена:{self.price} руб'
    #return self.art_name, f'{self.group}'


class ArticleDetail(models.Model):
    art_detail_name = models.CharField(max_length=64, unique=True, blank=True)
    article = models.ManyToManyField(Article)

    def __str__(self):
        return f'{self.art_detail_name}'

