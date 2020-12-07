from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from . import util
import markdown2
from django import forms
import random

class NewSearchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia", required= False, widget=forms.TextInput(attrs={'placeholder':'Search','style': 'width:100%'}))

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", required= True, widget=forms.TextInput(attrs={'placeholder':'title..'}))
    content = forms.CharField(label="Content", required=True, widget=forms.TextInput(attrs={'placeholder':'content..'}))

class NewEditForm(forms.Form):
    content = forms.CharField(label="Content", required=True, widget=forms.TextInput())

form = NewSearchForm()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),"form":form
    })

def get_page(request, title):
    page = util.get_entry(title)
    
    if page == None:
        return render(request, 'encyclopedia/error.html', {"title":title,"form":form})
        # return HttpResponse(markdown2.markdown(page))
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title, "content": markdown2.markdown(page), "form": form})

def search(request):
    if request.method == "GET":
        entries_found = []  #List of entries that match query
        entries_all = util.list_entries()  #All entries
        form = NewSearchForm(request.GET)  #Gets info from form
        # Check if form fields are valid
        if form.is_valid():
            # Get the query to search entries/pages
            query = form.cleaned_data["query"]
            # Check if any entries/pages match query
            # If exists, redirect to entry/page
            for entry in entries_all:
                if query.lower() == entry.lower():
                    return get_page(request, entry)
                # Partial matches are displayed in a list
                elif query.lower() in entry.lower():
                    entries_found.append(entry)
            # Return list of partial matches
            
            if len(entries_found) != 0:
                return render(request, "encyclopedia/search_results.html", {
                    "results": entries_found,
                    "form": form
                })
    # Default values
    return render(request, "encyclopedia/error.html", {
        "title": query, "form": form})
    
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html", {"form": form, "new_form": NewEntryForm()})

    elif request.method == "POST":
        new_entry = NewEntryForm(request.POST)
        if new_entry.is_valid():
            new_title = new_entry.cleaned_data["title"].capitalize()
            new_content = new_entry.cleaned_data["content"]
            entries_all = util.list_entries()
            for entry in entries_all:
                if new_title.lower() == entry.lower():
                    return render(request, "encyclopedia/new_page.html", {"form": form, "new_form": NewEntryForm(), "error": "That title already exists."})
            util.save_entry(new_title,new_content)
            return get_page(request, new_title)


def edit_page(request,title):
    if request.method == "GET":
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {"edit_form": NewEditForm(initial={'content':content}),"title":title})
    elif request.method == "POST":
        edited = NewEditForm(request.POST)
        title = request.POST
        if edited.is_valid():
            edited_content = edited.cleaned_data["content"]
            util.save_entry(title, edited_content)
            return get_page(request, title)

def random_page(request):
    entries_all = util.list_entries()
    length = len(entries_all)
    page = random.randrange(0, length)
    return get_page(request, entries_all[page])