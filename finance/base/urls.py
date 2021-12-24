from django.urls import include, path
from . import views

urlpatterns = [
	path('login/', views.login_page, name = "login"),
	path('logout/', views.logout_user, name = "logout"),
	path('', views.index, name='index'),
	path('display1', views.display_all, name = 'display1'),
	path('display2', views.display_important, name = 'display2'),
	path('add', views.add_expense, name='add'),
	path('edit/<int:pk>/', views.edit_expense, name='edit'),
	path('delete/<int:pk>/', views.delete_expense, name='delete'),
	path('calculator', views.display_calculator, name='calculator'),
	path('statistics' ,views.display_statistics, name='stats'),
]