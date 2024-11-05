
from django.contrib.auth.urls import urlpatterns
from django.urls import  path
from . import view
# from . import testdb
urlpatterns = [
    path('index1/', view.index1),
    path('index1/recommend.html/', view.recommend, name='recommend'),
    path('search/', view.search, name='search'),
    path('search_form/', view.search_form, name='search_form'),
]