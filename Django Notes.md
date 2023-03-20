# Django notes

## Url Routing And Django App
> *Time stamp:*4:00:00

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
2. Import path writing: `from django.urls import path`.  
This line allows us to have multiple URLs in our list.
3. Create a new list called `urlpatterns`, and this list will take all the the URLs we have in our project. The structure is the next one:
```python
urlpatterns = [
  path('', views.index, name='index')
]
```
- The empty `\` \``