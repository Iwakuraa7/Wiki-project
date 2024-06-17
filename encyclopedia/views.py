import os
from django.shortcuts import render
from wiki import settings
from . import util
from markdown2 import markdown
from django.http import HttpResponseRedirect
import random

entries = util.list_entries()

def index(request):
    matches = []
    if request.method == "GET":
        value = request.GET.get("q", "")

        if value == "":
            return render(request, "encyclopedia/index.html", {
                "entries": entries
            })

        elif value:
            for entry in entries:
                if value == entry:
                    return HttpResponseRedirect(f"{value}")
                elif value.lower() in entry.lower():
                    matches.append(entry)

            if len(matches) == 0:
                return HttpResponseRedirect(f"{value}")
            else:
                return render(request, "encyclopedia/mathces.html", {
                "matches": matches,
                "query": value
            })

def CSS_entry(request):
    content = markdown(util.get_entry("CSS"))
    title = "CSS"
    return render(request, "encyclopedia/CSS.html", {
        "content": content,
        "title": title
    })


def Django_entry(request):
    content = markdown(util.get_entry("Django"))
    title = "Django"
    return render(request, "encyclopedia/Djangp.html", {
        "content": content,
        "title": title
    })


def Git_entry(request):
    content = markdown(util.get_entry("Git"))
    title = "Git"
    return render(request, "encyclopedia/Git.html", {
        "content": content,
        "title": title
    })


def HTML_entry(request):
    content = markdown(util.get_entry("HTML"))
    title = "HTML"
    return render(request, "encyclopedia/HTML.html", {
        "content": content,
        "title": title
    })

def Python_entry(request):
    content = markdown(util.get_entry("Python"))
    title = "Python"
    return render(request, "encyclopedia/Python.html", {
        "content": content,
        "title": title
    })

def dynamic_entry(request, title):
    md_filepath = os.path.join(settings.BASE_DIR, "entries", f"{title}.md")
    with open(md_filepath, "r") as md_file:
        md_string = md_file.read()

    html_string = markdown(md_string)
    return render(request, "encyclopedia/new_page_layout.html", {
        "content": html_string,
        "title": title
    })

def create_new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        for entry in entries:
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/Page_not_found.html", {
                    "title_error_msg": "The page with this title already exists"
                })
        content = request.POST.get("content")

        md_string = f"{content}"
        md_filepath = os.path.join(settings.BASE_DIR, "entries", f"{title}.md")
        with open(md_filepath, "w") as md_file:
            md_file.write(md_string)

        entries.append(title)
        return HttpResponseRedirect(f"/wiki/{title}")
    else:
        return render(request, "encyclopedia/create_entry_page.html")

def edit_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        md_string = (util.get_entry(request.POST.get("title")))
        return render(request, "encyclopedia/edit_page.html", {
            "content": md_string,
            "title": title
        })

def save_edit_page(request):
    if request.method == "POST":
        edit_md_string = request.POST.get("edit_content")
        title = request.POST.get("title")

        util.save_entry(title, edit_md_string)
        return HttpResponseRedirect(f"/wiki/{title}")

def random_page(request):
    rand_index = random.randint(0, len(entries) - 1)
    return HttpResponseRedirect(f"/wiki/{entries[rand_index]}")

def page_not_found(request):
    return render(request, "encyclopedia/Page_not_found.html", {
        "not_found_error_msg": "Page not found"
    }, status=500)