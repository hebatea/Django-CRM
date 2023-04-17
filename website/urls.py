from django.urls import path
from . import views

# create actual template file 
# create actual html page
# create a URL and view 
urlpatterns = [
    path('', views.home, name='home'),
]