from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('display1', views.display_all, name = 'display1'),
	path('display2', views.display_done, name = 'display2'),
]