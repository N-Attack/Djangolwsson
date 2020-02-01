from django.http import HttpResponse
from django.template import loader


path = r"D:\Users\teacher\PycharmProjects\test_django\django_lesson\polls\templates\polls\index.html"


def index(request):
    template = loader.get_template("polls/index.html")
    context = {
        'comments': [
            "самый худший фильм",
            "автор прекрати!!!!"
        ],
    }
    return HttpResponse(template.render(context, request))


def work(request):
    text = request.GET.get("data")
    return HttpResponse(f"text is {text}")

