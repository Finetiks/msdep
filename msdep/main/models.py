from django.db import models
import datetime


# Create your models here.
class News(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.TextField()
    text = models.TextField()
    date = models.TextField()
    tags = models.TextField()
    author = models.TextField(default="Admin MSDEP 1")


class Images(models.Model):
    _id = models.AutoField(primary_key=True)
    path = models.ImageField()
    date = models.DateField(default=str(datetime.date.today()))
    related_news = models.ForeignKey(News, on_delete=models.CASCADE)


class DocumentsCategory(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.TextField()


class Document(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.TextField()
    file = models.FileField()
    category = models.ForeignKey(DocumentsCategory, on_delete=models.CASCADE)


class Employees(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.TextField()
    position = models.TextField()
    email = models.TextField()
    activity_description = models.TextField()
    image = models.ImageField(default='NoImage.png')


def MakeDictOfDocuments(category):
    docs_dict = dict()
    for i in category:
        if not i.docs_dict in docs_dict.keys():
            docs_list = list(Document.objects.filter(category=i))
            docs_dict.update({i.name: docs_list})
    return docs_dict


def get_all_employees():
    return Employees.objects.all()


def get_employee(id):
    return Employees.objects.filter(_id=id)


def get_news_by_id(id):
    return News.objects.filter(_id=id)


def get_last_news():
    last_ten = News.objects.all().order_by('-_id')[:10]
    last_ten_in_ascending_order = reversed(last_ten)
    return last_ten_in_ascending_order


def images_by_news(news):
    return Images.objects.filter(related_news=news)


def get_images():
    return Images.objects.all()
