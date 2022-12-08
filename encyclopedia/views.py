from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def css(request):
    return render(request, "encyclopedia/css.html", {
        "info": util.get_entry("CSS")
    })

def entry(request, entry):
    return render(request, "encyclopedia/entries.html",{
        "entryname": entry,
        "entry": util.get_entry(f"{entry}")
    })
