import markdown2
from django.shortcuts import render
from django import forms
from . import util

class SearchEntryForm(forms.Form):
    entry_searched = forms.CharField(label = "")

class CreatePageForm(forms.Form):
    title = forms.CharField(label = "Title")
    content = forms.CharField(widget=forms.Textarea(), label = "Markdown content for the page")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : SearchEntryForm()
    })

def entry(request, entry):
    if entry in util.list_entries():
        return render(request, "encyclopedia/entries.html",{
            "entry": markdown2.markdown(util.get_entry(f"{entry}")),
            "form" : SearchEntryForm()
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "form" : SearchEntryForm(),
            "exists": False
            })

def searchentry(request):
    if request.method == "POST":
        entry = SearchEntryForm(request.POST)
        if entry.is_valid():
            searched = entry.cleaned_data['entry_searched']
            if searched in util.list_entries():
                return render(request, "encyclopedia/entries.html",{
                    "entry": markdown2.markdown(util.get_entry(f"{searched}")),
                    "form" : SearchEntryForm()
                    })
            else:
                results = []
                for i in range(len(util.list_entries())):
                    if searched in util.list_entries()[i]:
                        results.append(util.list_entries()[i])
                return render(request, "encyclopedia/searchresults.html", {
                    "results": results,
                    "form" : SearchEntryForm()
                })

    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "form" : SearchEntryForm()
        })

def createnew(request):
    return render(request, "encyclopedia/createnew.html", {
        "form" : SearchEntryForm(),
        "title": CreatePageForm()
        })

def createdpage(request):
    if request.method == "POST":
        page = CreatePageForm(request.POST)
        if page.is_valid():
            title = page.cleaned_data['title']
            if title in util.list_entries():
                return render(request, "encyclopedia/error.html", {
                    "form" : SearchEntryForm(),
                    "exists": True
                    })
            content = page.cleaned_data['content']
            util.save_entry(title, content)

        return render(request, "encyclopedia/entries.html",{
            "entry": markdown2.markdown(util.get_entry(f"{title}")),
            "form" : SearchEntryForm()
            })
