from django.db import models


# class名字为表名
# CharField 表示char类型的字段
# question_text为字段名及数据库中的列名
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # 当前时间
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Student(models.Model):
    name = models.CharField(max_length=50)
    # 0男1女
    sex = models.IntegerField(default=0)
