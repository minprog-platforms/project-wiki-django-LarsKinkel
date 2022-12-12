import markdown2
from django.shortcuts import render
from django import forms
from . import util

class NewTaskForm(forms.Form):
    task = forms.CharField(label = 'Search Encyclopedia')

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : NewTaskForm()
    })

def entry(request, entry):
    if request.method == "POST":
        searched = 

    if entry in util.list_entries():
        return render(request, "encyclopedia/entries.html",{
            "entryname": entry,
            "entry": markdown2.markdown(util.get_entry(f"{entry}"))
            })
    else:
        return render(request, "encyclopedia/error.html")
