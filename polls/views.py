from django.http import HttpResponse
from django.template import loader
from .models import Question

path = r"D:\Users\teacher\PycharmProjects\test_django\django_lesson\polls\templates\polls\index.html"


def index(request):
    template = loader.get_template("polls/index.html")
    context = {
            'items': Question.objects.order_by
    }
    return HttpResponse(template.render(context, request))


def work(request):
    text = request.GET.get("data")
    return HttpResponse(f"text is {text}")

