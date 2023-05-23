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
> **Time stamp:** 4:20:55
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

## Building A Word Counter In Django
> **Time stamp:** 4:28:12
1. Go to **templates > index.html** and insert the next HTML code:
    ```HTML
    <h1>Input your text below: </h1>

    <!--method is for POST or GET-->
    <!--action is for indicating where do we want to send the data-->
    <!--It will send it something like: [localhost]/counter/'words=hey+whats+up-->
    <form method="" action="counter">
     <textarea name="text" rows="25" cols="100"></textarea><br>
     <input type="submit" />
    </form>
    ```
2. Go to **myapp > urls.py** and add another URL:
    ```python
    path('counter', views.counter, name='counter')
    ```
3. Go to **myapp > views.py** and create the `counter` function:
    ```python
    def counter(request):
      return render(request, 'counter.html')
    ```

4. Get rid of the `context` variable in `index` leaving it like this:
    ```python
    def index(request):
      return render(request, 'index.html')
    ```

5. Create a new file in **templates** called **counter.html**

6. For getting the data inserted into the textfield, we need to modify `counter` function:
    ```python
    def counter(request):
      #It gets the data from the element called "text"
      #In this case: <form> element
      text = request.GET['text']
      amount_of_words = len(text.split())
      return render(request, 'counter.html', {'amount': amount_of_words})
    ```

7. Go to **counter.html** and add the next code:
    ```HTML
    <h1>
      The amount of words is {{amount}}.
    </h1>
    ```

## Get vs Post In Django
> **Time stamp:** 4:43:13
When we specified the method in `index.html`, remember that left it empty. So `method` is for indicating what type of request you are using. Usually is either a GET method or a POST method.
- **GET:** It's mostly used whenever we are not passing any safe information (It's shown in the URL).
- **POST:** The information we send isn't going to be shown in the URL.  

Because you left the `method` property empty, by default it uses GET.

1. Go to **templates > index.html** and modify the form method, adding the value `"POST"` to the method property.

2. Anytime we are using a POST method, Django expects us to use CSRF token, helping for preventing attacks: add the next piece of code to **index.html**:
    ```HTML
    <form method="POST" action="counter">
      {% csrf_token %}
     <textarea name="text" rows="25" cols="100"></textarea><br>
     <input type="submit" />
    </form>
    ```

3. Go to **myapp > views.py** and modify the `counter` function, modifying the request for the variable `text`:
    ```python
    text = requests.POST['text']
    ```

## Static Files in Django
> **Time stamp:** 4:49:21
> **Static Files:** An external file that you use in your template file (Ex: External CSS files,  images, videos). All static files are saved in a folder called *"static"*.

1. Go to **templates > index.html** and remove the `<form>` tag. We don't need it anymore, and add the next code:
    ```HTML
    <h1>Hey, Welcome to my project</h1>
    ```

2. Create a new folder called **static**.

3. Go to **myproject > settings.py** and add the next piece of code for importing `os`:
    ```python
    import os
    ```

4. In **settings.py** create a new variable called `STATICFILES_DIRS` below `STATIC_URL` in the next way:
    ```python
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    ```
    And that's it! Now you can save static files in your *static* folder. Continuing you are going to see how it works.

5. Go to **static** and create a new file called **style.css**. Add the next code:
    ```CSS
    h1 {
      color: blue;
    }
    ```

6. Go again to **index.html** and add at the beggining:
    ```HTML
    <!--static is a tag that Django can see.-->
    {% load static %}

    <!--How we are importing our css file is because that's how it works in Django.-->
    <link rel ="stylesheet" href="{% static 'style.css' %}">
    ```

> If you need to move an entire HTML template, I recommend you to go to video!  
Basically, all the changes you did here, you have to do it for every file in your HTML template (Incluiding CSS, Javascript, etc.)

## Introduction to Django Models
> **Time stamp:** 5:04:29

*Models* are used for configuring our database. Usually you don't need to write a single line of SQL code to get your database up and running and that's called *model view template*.

- **Model:** What we use for our database. From here it's passed all the data into the template.
- **View:** What the user sees.

### Configuring a model
1. Go to **myapp > models.py** and create a new model:
    ```python
    #Create your models here.
    class Feature:
      id: int
      name: str
      details: str
    ```

2. For using the `Feature` class in the view, go to **myapp > views.py**, import `Feature` in this way:
    ```python
    from .models import Feature
    ```

    and modify the `index` function like this:
    ```python
    def index(request):
      feature1 = Feature()
      feature1.id = 0
      feature1.name = 'Fast'
      feature1.details = 'Our service is very quick'

      return render(request, 'index.html', {'feature': feature1})
    ```

3. Modify **index.html** adding this piece of code!
    ```HTML
    <p>Feature id: {{feature1.id}}</p>
    <p>Feature name: {{feature1.name}}</p>
    <p>Feature details: {{feature1.details}}</p>
    <hr>
    <p>Feature id: {{feature2.id}}</p>
    <p>Feature name: {{feature2.name}}</p>
    <p>Feature details: {{feature2.details}}</p>
    <hr>
    <p>Feature id: {{feature3.id}}</p>
    <p>Feature name: {{feature3.name}}</p>
    <p>Feature details: {{feature3.details}}</p>
    <hr>
    <p>Feature id: {{feature4.id}}</p>
    <p>Feature name: {{feature4.name}}</p>
    <p>Feature details: {{feature4.details}}</p>
    ```

4. Let's add some more features in **views.py**!
    ```python
    #[Insert below feature1.details]
      feature2 = Feature()
      feature2.id = 1
      feature2.name = 'Reliable'
      feature2.details = 'Our service is reliable'

      feature3 = Feature()
      feature3.id = 2
      feature3.name = 'Easy to use'
      feature3.details = 'Our service is easy to use'

      feature4 = Feature()
      feature4.id = 3
      feature4.name = 'Affordable'
      feature4.details = 'Our service is very affordable'
    
    return render(request, 'index.html', {'feature': feature1, 'feature2': feature2, 'feature3': feature3, 'feature4':feature4})
    ```

5. Don't you see this is a little bit... repetitive? Let's do this more dynamic. Open **views.py** again and add this piece of code:
    ```python
    #[Insert below feature4.details]
    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})
    ```
6. And, modify again the **index.html**, deleting the `<p>` tags and adding this piece of code:
    ```HTML
    {% for feature in features %}
    <div>
      <p>Feature id: {{features.id}}</p>
      <p>Feature name: {{features.name}}</p>
      <p>Feature details: {{features.details}}</p>
    <hr>
    </div>
    {% endfor %}
    ```

7. Now, playing with more stuff with Django, add a new property to `Feature` class in **models.py**:
    ```python
      is_true: bool
    ```

8. Add `true` to every feature except in `feature3` (Add `false`).

9. Modify **index.html** in this way:
    ```HTML
    <div>
      <p>Feature id: {{feature.id}}</p>
      <p>Feature name: {{feature.name}}</p>
      <p>Feature details: {{feature.details}}</p>
      {% if feature.is_true == True %}
      <p>This feature is true</p>
      {% else %}
      <p>This feature is false. So bad >:c</p>
      {% endif %}
    <hr>
    </div>
    ```

## Django Admin Panel & Manipulation Of Database
> **Time stamp:** 5:29:02

- **db.sqlite3:** *Found in myapp* This file is in charge of storing all the database in Django. By default is SQL Lite.

This is how you make a model using a database:

1. Go to **myapp > models.py** and modify the `Feature` class:
    ```python
    class Feature(models.Model):
      id: int
      name: str
      details: str
      is_true: bool
    ```
    And now, `Feature` is a model, each attribute object has an ID when it's created.

2. Because now our objects have an ID automatically, we don't need id anymore. And for converting `Feature` to model, modify it like this:
    ```python
    class Feature(models.Model):
      #CharField means a string
      name = models.CharField(max_length=100)
      details = models.CharField(max_length=500)
    ```

3. We need to configure some settings in order to set up a database. Go to **myproject > settings.py**. Look for `INSTALLED_APPS` and add:
    ```python
    'myapp'
    ```
    And now it will add *myapp* into the main project.

4. In order to migrate data into the database, open a new terminal and insert the next commands inside `myproject` root file:
    ```
    python manage.py makemigrations
    ```
    Any changes in which we made in the models file, it's going to save those changes

5. For sending the last changes to the databse, we need to migrate it with the next command in the terminal:
    ```
    python manage.py migrate
    ```
    All the changes made before are reflected in the `db.sqlite3`

### Exploring Django admin.py
You can open your web broser and go to `127.0.0.1:8000/admin`. The site you are looking is an admin site, this is where you can mantain and control the site at any hour. Only the developers can get credentials to that particular site.

1. In order to obtain the credentials, open a new terminal and insert the next command inside `myproject` root file:
    ```
    python manage.py createsuperuser
    ```
    This specific command creates a **Super User**. 

2. Insert a username, an email address (optional) and a password for you Super User account.

Now you can enter to the admin site.

> **Inside Users:** Here you'll find all the users you have in your project

---
We aren't still watching our `Feature` model inside the admin site, and what we have to do is:
1. Go to **myapp > admin.py** and add the next piece of code: 
    ```python
    from .models import Feature

    #Register your models here
    admin.site.register(Feature)
    ```
    This is for registering our modules. In this case we registered the `Feature` module. When I refresh the admin site you could see now the `Features` database.

2. Create a new register inside `Features` so you can see that it's working. **Select the `Feature` database > Click *Add Feature* button > Insert a name (Quick) and details (Our product is very fast) > Click *SAVE***.  

    Now that you saved it, you should see a new object inside the database
    
3. Since you have an object in the database, you don't need the ones created before. Go to **myapp > views.py** and delete all the objects created (`feature1`, `feature2`, `feature3` `feature4`, `feature5` and `features`).

4. Add another object to the database with the name *"Reliable"* and Details *"We are very very very reliable"*.

5. In order to get all the data created in the project you need to import the `Feature` inside **views.py** model like this:
    ```python
    from .models import Feature #This has been alredy done before
    ```

    So you are importing the `Feature` model, whcich is linked to the database. That means that if your assesing an object from `Feature` in your code, your assesing all the values inside the database.

6. Modify the **views.py** adding the next code inside the `index` function:
    ```python
    features = Feature.objects.all()
    ```
    In this case, `features` is importing all the objects from the `Feature` database.

7. Modify the **index.html** leaving only the content related with `name` and `details`.

Now, it's not necessary to add features with code anymore! You just need to go to `127.0.0.1:8000/admin/myapp/feature/add/` and add features. You can even manipulate them as any data. Add this to your **index.html** and you'll watch it:
```HTML
{% if feature.name == 'Quick' %}
<p>This feature says our site is quick</p>
{% endif %}
```

## User Registration in Django
> **Time stamp:** 5:46:38

User authentication means signing in and signing out to a platform. In order to add that feature into your project you'll have to:

1. Let's create a new URL called *register*. Go to **myapp > urls.py** and add the next url:
    ```python
    path('register', views.register, name='register')
    ```

2. Go to **myapp > views.py** and create a new function:
    ```python
    def register(request):
        return render (request, 'register.html')
    ```

3. You don't have `register.html` yet. Create a new filed called like that inside *templates* and add the next HTML code:
    ```HTML
    <h1>Sign Up Below</h1>

    <form method="POST" action="register">
      {% csrf_token %} <!--Remember Django needs CSRF token-->
      <p>Username:</p>
      <input type="text" name="username" />
      <p>Email:</p>
      <input type="email" name="email" />
      <p>Password:</p>
      <input type="password" name="password" />
      <p>Repeat Password:</p>
      <input type="password" name="password2" />
      <br>
      <input type="submit" />
    </form>
    ```

4. We need to colect all the data entered in the respective form, so we need to modify **views.py** in the next way:
    ```python
    def register(request):
        if request.method == 'POST': #Content is being sent
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          password2 = request.POST['password2']

        return render (request, 'register.html')
    ```
    The `if` condition is there to indicate whether the user is visiting the website (So the content is only going to be rendered) or if the page is being rendered with a **POST** method, meaning that something is being sent to this view.

5. Before we continue, we need to import some libraries, which are:
    ```python
    from django.shortcuts import render, redirect
    from django.contrib.auth.models import User, auth
    from django.contrib import messages
    ```
    - `redirect`: It's for redirecting the user to another page.
    - `User`: It's the user model from Django.
    - `auth`: It's functions of the methods that allow us to authenticate.
    - `messages`: It's for sending a response back if there is an error or anything.

6. We would like to know: If `password` and `password2` are the same, if the inserted `email` alredy exists and if the inserted `username` alredy exists too in our database. For this modify the `register` function in the next way:

    ```python
    def register(request):
        if request.method == 'POST': #Content is being sent
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          password2 = request.POST['password2']
          
          if password == password2: #If passwords are equal
            if User.objects.filter(email=email).exists(): #If an email alredy exists
              messages.info(request, 'Email Alredy Used')
              return redirect('register')
            elif User.objects.filter(username=username).exists(): #If an user alredy exists
              messages.info(request, 'Username Alredy Used')
              return redirect('register')
            else: #Create a new user
              user = User.objects.create_user(username=username, email=email, password=password)
              user.save();
              return redirect('login')
          else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
        else:
          return render (request, 'register.html')
    ```

7. We need to show the messages if there is any error. Go to your **register.html** file and add the next piece of code below the first `<h1>` tag:
    ```HTML
    {% for message in messages %}
    <h5>{{message}}</h5>
    {% endfor %}
    ```

8. Add some style to your message inside **register.html**
    ```HTML
    <style>
      h5{
        color: red;
      }
    </style>
    ```
    
And that's it!


# User Login and Logout in Django
> **Time stamp:** 6:08:46

Now we want to make a login and logout for the registered users, and for this, you need to:

## Logging in
1. Go to **myapp > urls.py** and create a new URL named `path`:
    ```python
    path('login', views.login, name='login')
    ```

2. Go to **myapp > views.py** and create a new function named `login`:
    ```python
    def login(request):
      return render (request, 'login.html')
    ```

3. Create a new file inside *templates* called *login.html* and add the next code:
    ```HTML
    <h1>Login Now</h1>

    <form action="login" method="POST">
      {% csrf_token %}
      <p>Username:</p>
      <input type="text" name="username" />
      <p>Password:</p>
      <input type="password" name="password" />
      <br>
      <input type="submit"/>
    </form>
    ```

4. Go back to **views.py** and modify the `login` function:
    ```python
    def login(request):
      if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: #User is registered
          auth.login(request, user)
          return redirect('/')
        else:
          messages.info(request, 'Credentials Invalid')
          return redirect ('login')
      else:
        return render (request, 'login.html')

    ```
    - If the `user` is `None` means that the user is not known in our platform

5. Go back to **login.html** and add the next piece of code for the message in case that the user doesn't exists:
    ```HTML
    <style>
      h3{
        color: red;
      }
    </style>

      {% for message in messages %}
      <h3>{{message}}</h3>
      {% endfor %}
    ```

6. We want our user to feel welcomed. Go to **index.html** and add this welcome text for the user:
    ```HTML
    {% if user.is_authenticated %}
    <div>
      <h1 align="center">Welcome, {{user.username}}</h1>
    </div>
    {% else %}
    <div>
      <h1 align="center">Welcome to the website!</h1>
    </div>
    {% endif %}
    ```
    - The `user.is_authenticated` method checks if the user had login into the website or not.

## Logging out
What if the user wants to logout? Follow the next steps:

1. Add a button inside your **index.html** for logging in/out:
    ```HTML
    {% if user.is_authenticated %}
    <a href="logout" class="button">Logout</a>
    {% else %}
    <a href="login" class="login">Login or Signup</a>
    {% endif %}
    ```

2. Create a new URL inside **urls.py** called *logout*:
    ```python
    path('logout', views.logout, name='logout')
    ```

3. Go to **views.py** and create the `logout` function:
    ```python
    def logout(request):
      auth.logout(request)
      return redirect('/')
    ```
    - `auth.logout` is for logging out the user from his account.

# Dynamic Url Routing in Django
> **Time stamp:** 6:26:43

Dynamic URL it's for when we have the same URL but different ID passed in it, having different outputs. 

> An example for this is if we'd like to have a different profile page for every user.

For setting up this characteristic, follow the next steps:

1. Go to **myapp > urls.py** and add the next URL:
    ```python
    path('post/<str:pk>', views.post, name='post')
    ```
    In this path we are having */posts* and then a string called `pk`. `pk` is our variable.

2. Go to **myapp > views.py** and create a new function called `post` like this:
    ```python
    def post(request, pk):
      return render (request, 'post.html', {'pk': pk})
    ```
    - `pk` is a variable that is receiving from the last step. We are also sending it to **post.html**

3. Go to *templates* and create a new file called **post.html** and show the value inside `pk`:
    ```HTML
    <h1>The value in the url is {{pk}}</h1>
    ```
    You can test the result going to `127.0.0.1:8000/post/12`!
    By this far, you have set up Dynamic URL in your website.

4. Did you remember your `counter` function? Me neither. Go to **views.py** and modify it like this:
    ```python
    def counter(request):
      posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john']
      return render(request, 'counter.html', {'posts': posts})
    ```

5. We'd like to setup a different page for every element inisde `posts`. Delete everything inside **counter.html** and add the next code:
    ```HTML
    {% for post in posts %}
    <h1><a href="{% url 'post' post %}">Post</h1>
    {% endfor %}
    ```
    - `{% url 'post' post %}`: It means:
      - `url`: The initial URL of our website, this means `127.0.0.1:8000`
      - `'post'`: Go to `/post`
      - `post`: The respective element of the `posts` variable from the `counter` function in **views.py**


# Postgresql Setup
> **Time stamp:** 6:37:24

For this section you need to have installed Postgresql and pgAdmin
> **Note from the author**  
Yeah, unfortunately I have Arch. For Postgresql you need to install it as usual but maybe you'll get an error when you try to start the service. For that scenerio, follow [these steps](https://bbs.archlinux.org/viewtopic.php?id=149446).  
And for pgAdmin, well... If you try to install it as usual you'll never be able to open it because it has a critical bug, so your alternative option is to run it inside a virtual environment :D. [This is a good tutorial](https://linuxhint.com/install-pgadmin4-manjaro-linux/) orientated for Manjaro. That's it, thank you for reading me c:  
*4 Hours after I wrote the last paragraph:* Well, I didn't know how to create a server... [Here it is how you can do it (ES)](https://youtu.be/WzV4ncw9-ng?t=1326)

> **Note from the author: How to create the server that you can see inside the video**
> 1. Right-click on *Servers*
> 2. Register > Server
> 3. Insert the name (PostgreSQL 12)
> 4. Insert the Host name/address (127.0.0.1)
> 5. Remember to put a Username (By default, you can use *postgres*) and a password (By default, I'm using postgres)
> 6. Save it.

For creating a database inside pgAdmin, follow the next steps

1. Open pgAdmin4 and display *servers*.

2. Right-click *Databases* and select *Create > Database*.

3. Give it a name (*myproject*) and save it.

4. Click on *myproject > Schemas* and as you can see, *Tables* is empty

5. Go back to your project and go to **myapp > myproject > settings.py**

6. Search for the `DATABASES` variable and change the `ENGINE` and `NAME`, and add the `USER`, `PASSWORD` and `HOST` variables for your database. In this case we are changing like this:
    ```python
    DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
      }
    }
    ```

7. Open your command prompt inside *myproject* (root) and install the next modules:
    ```
    pip install psycopg2
    pip install Pillow
    ```
    These libraries are going to allow you to be able to connect Postgres to your Django project.

8. And finally, insert the next commands:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

For viewing your data inside pgAdmin, you can:
1. Go to *Servers > PostgreSQL 12 > Databases > myproject > Schemas > public > tables*.

2. Inside *tables* you'll find all the tables generated from Django. For viewing one of them follow the next steps (This exampl with *myapp_feature*). *Right-click myapp_feature > View/Edit Data > All Rows* and you can see it.

And this is everything from the Django Crash Course. Thank you for reading me and I hope this was helpful to you. 

From this section onwards you'll find little projects for practicing your new skills :)


# Building A Blog With Django - Part 1
> **Time stamp:** 6:47:23

In this section, we create a Blog using Django. Go and watch the video if you want to know how it was done!

>**Superuser account**
> *seb0927 - admin1234*


# Building A Blog With Django - Part 2
> **Time stamp:** 7:12:10

In this section, we create a Blog using Django. Go and watch the video if you want to know how it was done!

>**Superuser account**
> *seb0927 - admin1234*


# Building A Weather App With Django - Part 1
> **Time stamp:** 7:25:48


# Building A Weather App With Django - Part 2
> **Time stamp:** 7:45:17


# Building A Realtime Chat Application With Django - Part 1
> **Time stamp:** 8:03:06


# Building A Realtime Chat Application With Django - Part 2
> **Time stamp:** 8:50:11


# Django Rest Framework Crash Course
> **Time stamp:** 9:07:59

In this section, we'll be talking about the Django Rest Framework. The Django REST Framework is a library wchic allows you to built API's in your Django project.

In order to start using it, we'll follow the next steps in order to install, and using it

1. Inside our command prompt, you'll install django with the next command:
    ```
    pip install django
    ```

2. Now, start a new Django project with the next command:
    ```
    django-admin startproject drfproj
    ```
    So that command line is going to start a new application or a new Django Project.

3. In order to use the REST framework, we need to install it first with the net command:
    ```
    pip install djangorestframework
    ```

4. Now that we have the REST framework installed, you can use the library in other modules of your project. In order to do this, create a new file inside *drfproj* called: `views.py` and add the next piece of code:
    ```python
    from django.shortcuts import render
    from rest_framework.views import APIView
    from rest_framework.response import Response
    ```
    - `APIView`:  It let's us to access a lot of API's that are available in the Django REST Framework. So with this we cane make get or post requests.
    - `Response`: It's for showing results or giving a response to the user accessing the API.

5. Create a new class that inherits from `APIView` and implement a get request for the API:
    ```python
    class TesView(APIView):
    ```

6. You can implement a get request for the API in this way:
    ```python
    class TesView(APIView):
      def get(self, request, *args, **kwargs):
        data = {
          'username': 'admin',
          'years_active': 10
        }
        return Response(data)
    ```
    In this case, it'll only return a dictionary in a variable called `data`

7. Go to *urls.py* and import the `TestView` function created before, and add a new path to `urlpatterns`:
    ```python
    from django.contrib import admin
    from django.urls import path, include
    from .views import TesView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', TesView.as_view(), name='test')
    ]
    ```
    Since `TesView` is not a view *per se*, we neet to add it with the method `as_view` in order for not getting errors.

8. We aren't finished yet. Go to *settings.py* and inside `INSTALLED_APPS`, you'll add `'rest_framework` in order to Django recognize the REST framewor k.

9. Go back to *urls.py* and another path:
    ```python
    path('api-auth/', include('rest_framework.urls'))
    ```

10. Time for testing! Inside your command prompt run the server with the next command:
    ```
    python manage.py runserver
    ```
    And now it showcases your API!.
    > Note from the author: If you get any errors, just do a `python manage.py makemigrations` and `python manage.py migrate`.

## Serializers

Serializers are a structure of representation that represents data we want to return in a JSON format, so we can transform our Django models into a JSON. In order to start using our API like an API, follow the next steps:

1. Insert into your command prompt:
    ```
    python manage.py startapp drfapp
    ```

2. Go to *drfapp > models.py* and create a new model:
    ```python
    from django.db import models

    #Create your models here.
    class Student(models.Model):
      name = models.CharField(max_length=100)
      age = models.IntegerField()
      description = models.TextField()
      date_enrolled = models.DateTimeField(auto_now=True)

      def __str__(self):
        return self.name
    ```

3. Now go to *settings.py* and add to `INSTALLED_APPS`: `'drfapp'`

4. Migrate the model created inside your command prompt with the next commands:
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a new file called *serlializers.py* inside *drfapp* and add the next piece of code:
    ```python
    from rest_framework import serializers
    from .models import Student

    class StudentSerializer(serializers.ModelSerializer):
      class Meta:
        model = Student
        fields = (
          'name', 'age'
        )
    ```

6. Go back to *drfproj > views.py* and import the serializers we are going to use adding the next lines of code:
    ```python
    from drfapp.serializers import StudentSerializer
    from drfapp.models import Student
    ```

7. Now with those imports, we can create a POST method in our test view class so we can receive data like in a form. Add the next piece of code inside *views.py*:
    ```python
    def post(self, request, *args, **kwargs):
      serializer = StudentSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors)
    ```
    - `(data=request.data)`: It means that we are submiting data.
    - `serializer.is_valid()`: If the values or variables are correct (Ex: Cheking Integer fields, etc.).
    - `serializer.save()`: Save the data submitted.
    - `return Response(serializer.data)`: Return the data indicating that it has been sucesfully saved.
    - `return Response(serializer.errors)`: Return the data indicating that it has got an error

8. Run the server with `python manage.py runserver`!

9. For testing our POST methods, we'll use an application called `POSTMAN` you can get it [here](https://www.postman.com/). Copy your localhost server andpaste it into the field that says *Enter request URL*.

  After that, you'll select that you'll be testing with a POST method. Select the radio-button *form-data* and you'll get a table. If you remember correctly we are asking inside `StudentSerializer` the fields `name` and `age` so we'll add the next data:
  - **KEY:** name **VALUE:** admin
  - **KEY:** age **VALUE:** 25

  And finally, click on *Send* in order to test the API.

  You'll get a respone in a JSON Format of the data introduced, indicating that it has been correctly send.

10. How can I know if that particular data has been submitted into my model? You can check it inside your admin interface. So create a new Superuser inside your command prompt:
    ```
    python manage.py createsuperuser
    admin

    admin1234
    admin1234
    y
    ```

11. Go to *admin.py* and add the next piece of code in order to import the Student model:
    ```python
    from django.contrib import admin
    from .models import Student

    #Register your models here.
    admin.site.register(Student)
    ```

12. Now you can enter to the admin panel. Go there (*127.0.0.1:8000/admin*) and inside *Drfapp* we have the Student model, and we have a student called *admin*. which it was submitted via our API, indicating that is working correctly.

## Serializing with GET method
We already have created a model, so now we are going to create a GET method using serializing.

1. Modify the `get` function in this way:
    ```python
    def get(self, request, *args, **kwargs):
      qs = Student.objects.all()
      serializer = StudentSerializer(qs, many=True)
      return Response(serializer.data)
    ```
    - `qs`: It represents the query set from the Student model.
    - `StudentSerializer(qs, many=True)`: It indicates that I may obtain many data from the Students database.

2. In order to test it, go to Postman and change for a GET Method, select form-data, remove the key and values that are in the table and select none, and hit Send. And as you can see you are obtaining a query set of lists of the data you have inside the Student model.

3. If we only want one data, we need to modify the `get` function in the next way:
    ```python
    def get(self, request, *args, **kwargs):
      qs = Student.objects.all()
      student1 = qs.first()
      serializer = StudentSerializer(student1)
      return Response(serializer.data)
    ```
    - `qs.first()`: It's only selecting the first student in the query set.

## Authentication
Authentication helps to protect our API endpoint, so in order to implement it, follow the next steps:

1. Add the next imports inside *drfproj > views.py*:
    ```python
    from rest_framework.permissions import IsAuthenticated
    ```
2. Insert a new piece of code at the beggining of `TesView`:
    ```python
    permission_classes = (IsAuthenticated, )
    ```
    And now if we send a request, it is going to return an authentication error because we are not authenticated.

3. Go to *settings.py* and addd at the end of the code the next lines:
    ```python
    REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
      ]
    }
    ```
    And add to `INSTALLED_APPS`
    ```python
    'rest_framework.authtoken'
    ```

4. Make a new migration with `python manage.py makemigrations` and `python manage.py migrate`.

5. Flush the data you have inside your DB with `python manage.py flush`.

6. Because you deleted all the data, you need to create a new superuser again. Do it like you did it before:
    ```
    python manage.py createsuperuser
    admin

    admin1234
    admin1234
    y
    ```

7. In order to create a token for a user, go to your command prompt and insert the next command:
    ```
    python manage.py drf_create_token admin
    ```
    So in this command we are creating a token for the admin user.

8. In order to be authenticated so we can use that token for sending an API request, select the *Authorization* tab and select in type *API Key* and insert the next values:c
    - **KEY:** Authorization **VALUE:**Token [Insert the token created here (You can watch it in the admin panel)]
    And now you can ask for API requests

9. In order to create a token for every user registered in our platform, we need to make a change in *urls.py*:
    ```python
    from rest_framework.authtoken.views import obtain_auth_token
    ```
    and add a new path:
    ```python
    path('api/token', obtain_auth_token, name='obtain')
    ```