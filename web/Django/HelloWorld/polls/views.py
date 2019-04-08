from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question
from .models import Student


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    # 页面不存在则返回404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def test(request):
    # 增
    # Student.objects.create(name='Sam', sex=0)
    #
    # obj = Student(name='Tom', sex=0)
    # obj.save()
    #
    # dic = {'name': "Jack", 'sex': 1}
    # Student.objects.create(**dic)

    # 查
    # 返回object
    # context1 = Student.objects.all()
    # # 查询某一列,返回dict
    # context2 = Student.objects.all().values('name')
    # # 查询某几列,返回dict
    # context3 = Student.objects.all().values_list('id', 'name')
    # # 返回object
    # context4 = Student.objects.get(id=1)
    # # 返回object
    # context5 = Student.objects.get(name='Sam')
    # return HttpResponse(context4)

    # 改
    Student.objects.filter(name='Sam').update(sex=1)

    obj = Student.objects.get(name='Tom')
    obj.sex = 1
    obj.save()

    # 删
    Student.objects.filter(name='Sam').delete()
