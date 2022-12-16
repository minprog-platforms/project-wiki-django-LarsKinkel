# Wiki Encyclopedia

Application made as an exercise for Minor Programmeren at UvA.
Users are able to add pages, just like at wikipedia.
Users are able to search for existing pages.


## Getting Started

Pull the repository from github to your computer, then get the app running by typing "python3 manage.py runserver". Copy the given url and paste it into your webbrowser to go to the actual webpage. At the left hand side of the page will always be a searchbar. Precisely typing in an existing page will take you to that page. If you type in a substring of existing pages, you will be taken to a results page that includes all the entries that you are possibly looking for.


## Rough sketch of the pages

![image](https://github.com/minprog-platforms/project-wiki-django-LarsKinkel/blob/main/Sketch/sketchwiki.jpg?raw=true)

## Guidelines producing designdocument

In order to create a new page, I first have to create an url path in the urls.py, then i would create a function in views.py to decide what the page should do and what special variables should be handed to the website. At last, I need to create an html file to decide how the actual page is going to look like.

Html pages that i will certainly need are: homepage, entrypage, an errorpage and a page to create a new entry.
