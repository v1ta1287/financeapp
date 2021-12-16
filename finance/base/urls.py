from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('display1', views.display_all, name = 'display1'),
	path('display2', views.display_done, name = 'display2'),
	path('add', views.add_task, name='add'),
	path('edit/<int:pk>/', views.edit_task, name='edit'),
	path('delete/<int:pk>/', views.delete_task, name='delete'),
]