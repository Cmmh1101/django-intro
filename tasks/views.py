from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    # check for post method to access entered form data
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # if form is valid save data in task variable
            task = form.cleaned_data["task"]
            # add taks to the list of tasks in the user session
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # not valid? return to the form, with the entered data giving error feedback
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })
