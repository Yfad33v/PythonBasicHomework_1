from django.core.management.base import BaseCommand

from article.models import Group, Article, ArticleDetail

class Command(BaseCommand):

    def handle(self, *args, **options):
        # создаем товарные группы
        groups = ['Одежда', 'Электроника', 'Товары для дома']
        for group in groups:
            Group.objects.get_or_create(group_name=group)
        # создаем товары внутри групп
        Closes = Group.objects.get(group_name='Одежда')
        Closes.article_set.create(art_name='Джинсы', price = 1500.5)
        Closes.article_set.create(art_name='Рубашка', price = 2500.78)

        Elec = Group.objects.get(group_name='Электроника')
        Elec.article_set.create(art_name='Смартфон Huawei', price = 21500.5)
        Elec.article_set.create(art_name='Laptop HP', price = 4500.78)

        Housholds = Group.objects.get(group_name='Товары для дома')
        Housholds.article_set.create(art_name='Утюг', price = 3500.5)
        Housholds.article_set.create(art_name='Увлажнитель', price = 6500.78)

        # создаем справочник доп свойств товара
        art_details = ['Вес', 'Цвет']
        for art_detail in art_details:
            ArticleDetail.objects.get_or_create(art_detail_name=art_detail)

        # добавляем по каждому товару связь с его свойством (вес, цвет)
        articles = Article.objects.all()
        art_details = ArticleDetail.objects.all()
        for article in articles:
             for art_detail in art_details:
                 article.articledetail_set.add(art_detail)
