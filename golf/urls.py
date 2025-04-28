from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('shot_predictor/', views.shot_predictor, name='shot_predictor'),
    path('scorecard/', views.scorecard_view, name='scorecard'),
    path('reset_scorecard/', views.reset_scorecard, name='reset_scorecard'),

]
