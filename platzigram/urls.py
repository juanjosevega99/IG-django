from django.urls import path

from platzigram import views

urlpatterns = [
    path('hello_world/', views.hello_world),
    path('hi/', views.hi)
]
