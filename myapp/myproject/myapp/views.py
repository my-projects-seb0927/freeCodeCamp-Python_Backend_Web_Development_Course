from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
  feature1 = Feature()
  feature1.id = 0
  feature1.name = 'Fast'
  feature1.details = 'Our service is very quick'
  feature1.is_true = True

  #[Insert below feature1.details]
  feature2 = Feature()
  feature2.id = 1
  feature2.name = 'Reliable'
  feature2.details = 'Our service is reliable'
  feature2.is_true = True

  feature3 = Feature()
  feature3.id = 2
  feature3.name = 'Easy to use'
  feature3.details = 'Our service is easy to use'
  feature3.is_true = False

  feature4 = Feature()
  feature4.id = 3
  feature4.name = 'Affordable'
  feature4.details = 'Our service is very affordable'
  feature4.is_true = False

  features = [feature1, feature2, feature3, feature4]
  return render(request, 'index.html', {'features': features})

def counter(request):
  #It gets the data from the element called "text"
  #In this case: <form> element
  text = request.POST['text']
  amount_of_words = len(text.split())
  return render(request, 'counter.html', {'amount': amount_of_words})
