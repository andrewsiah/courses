from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse



class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    #Check if there's already a list of tasks inside session. 
    #If not, make one.
    if "tasks" not in request.session:
        #a new list of tasks that is stored in request.session. 
        #Referrable as request.session["tasks"] as var.
        request.session["tasks"]=[]
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    #Server side validation of data.
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        #
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html",{
                "form":form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })