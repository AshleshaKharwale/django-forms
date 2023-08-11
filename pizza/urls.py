from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('pizzas/', views.pizzas, name='pizzas'),
]