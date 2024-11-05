from django.contrib.auth.urls import urlpatterns
from django.urls import  path
from . import view
# from . import testdb
urlpatterns = [
    path('index1/', view.index1),
    path('recommend/', view.recommend, name='recommend'),
]