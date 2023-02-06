from django.shortcuts import render

tasks = ["read", "cook", "workout"]

# Create your views here.


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
