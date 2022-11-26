from django.urls import path
from . import views

app_name='report'
urlpatterns = [
    path('',views.IndexView.as_view(),name='home')
]