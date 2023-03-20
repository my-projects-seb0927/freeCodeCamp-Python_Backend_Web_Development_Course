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
1. Create new file called `urls.py` inside myapp.
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

## Django Template Language
> **Time stamp:** 4:14:21

We returned our HtttpResponse with an `<h1>` tag, but what if we have an external HTML file which we want to render in our index page? We need to configure Django to be able to see our HTML files or templates.

1. Create a new folder called **templates** inside **myproject (root)**. Inside this folder we store all our template file (HTML files).
2. Go to **myproject > settings.py**
3. Change the ``TEMPLATES`` variable putting inside `DIRS` the next value:
    ```python
    'DIRS': [BASE_DIR, 'templates']
    ```
    > TEMPLATES is a short form of directory (*"which directory should Django go into to look for the template file"*).   
    **BASE_DIR:** Indicates the base directory and look for a folder called **templates**.

4. If you alredy have an HTML file ready to work on, That's it. If not: go into your **templates** folder and create a new file named **index.html** and insert the next code so you can see how Django loads the page:
    ```HTML
    <h1>
      How are you doing today?
    </h1>
    ```
5. Go to **myapp > views.py** and modify the `index` function in the next way:
    ```python
    def index(request):
      return render(request, 'index.html')
    ```
    > The render function is in charge of rendering our html file. Inside render you add `request` and the respective file in order to render.

## Sending Data To Template File
In order to send dynamic data (Data that is difrerent deppending of the input):

1. Go to **myapp > views.py** anc change the `index` function to:
    ```python
    def index(request):
      name = 'Patrick'
      return render(request, 'index.html', {'name': name})
    ```
    > Here we are sending the variable `name` in a dictionary being `'name'` the key and `name` the variable in order to be sent.

2. Go to **templates > index.html** and modify it:
    ```HTML
    <h1>
      Welcome, ({name})!
    </h1>
    ```
    > The varibale `name` is coming from our backend.

3. Now: What we did in the first point it's not a good practice. This is how you should do it in **views.py**:
    ```python
    def index(request):
      context = {
        'name':name,
        'age':23,
        'nationality': 'British',
      }
      return render(request, 'index.html', context)
    ```
    and inside **index.html**:
    ```HTML
    <h1>
      Welcome{{name}}<br> You are {{age}} years old<br>You are {{nationality}}
    </h1>
    ```
