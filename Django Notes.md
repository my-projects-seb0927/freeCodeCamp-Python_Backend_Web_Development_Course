# Django notes

## Url Routing And Django App
> **Time stamp:** 4:00:00

### Django apps
Django apps are subsets of the main project. An example can be Instagram: Instagram is our main project but every section of it can be apps (Direct messages, marketplace, Reels, etc.) and each app has individual features and functions.

Having many apps is not necessary, you can have a project with one app, but in big projects you'll probably create apps for dividing taks.

#### How to create a Django app
1. Make sure you are inside the virtual environment.
2. Make sure you are inside the root directory of Django project.
3. Insert the next command line:
`python manage.py startapp myapp`
4. We have now a new folder called `myapp` with the next files:
  - **__init_.py:** For libraries and modules.
  - **admin.py:** Admin interface which allows you to control your size or maintain your size, your view of the database, etc.
  - **apps.py** 
  - **models.py:** Here we create all our database.
  - **tests.py** 
  - **views.py:** Where all the main things happen.

### URL Routing
Each particular link in your website is a URL. For making that every URL in our website works correctly, we need to configure them first.

#### How to configure URLs
1. Create new file called `urls.py`.
2. Import `path` writing: `from django.urls import path`. This line allows us to have multiple URLs in our list.
3. Import `views` writing: `from . import views`
3. Create a new list called `urlpatterns`, and this list will take all the the URLs we have in our project. The structure is the next one:
```python
urlpatterns = [
  path('', views.index, name='index')
]
```
- `` '' `` means that's the root url (Main site).
- `views.index` indicates that is going to render an HTML file. In this section we can indicate what is going to happen when the user access this URL, so we can send a restful HTTP response, a JSON response, etc.
- ``name='index'`` means a function imported from the file `views.py`. What we do in the `index` function, is what is going to be assigned to the URL.
4. Go to `views.py` file and add the next piece of code:
```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse('<h1>Hey, Welcome</h1>')
```

#### Setting an app inside the main project
1. Go to **myproject > urls.py**.
2. Add the next piece of code:
```python
from django.urls import path, include
```
3. Add the next path inside `urlpatterns`
```python
path('', include('myapp.urls'))
```
