from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shot_predictor/', views.shot_predictor, name='shot_predictor'),

]