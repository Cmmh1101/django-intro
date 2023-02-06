from django import forms
from django.shortcuts import render

tasks = ["read", "cook", "workout"]


class NewTaskForm(forms.Form):
    taks = forms.CharField(label="New Task")
    priority = forms.IntegerField(
        label="priority", min_value=1, max_value="10")

# Create your views here.


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    # check for post method to access entered form data
    if request.method == "POST":
        form = NewTaskForm(request.POST)
    if form.is_valid():
        # if form is valid save data in task variable
        task = form.cleaned_data["task"]
        # add taks to the list of tasks
        tasks.append(task)
    else:
        # not valid? return to the form, with the entered data giving error feedback
        return render(request, "tasks/add.html", {
            "form": form
        })

    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })
