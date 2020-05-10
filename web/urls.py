from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('international',views.international,name="international"),
    path('domestic',views.domestic,name="domestic"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('how',views.how,name="how"),
    path('moreideas',views.moreideas,name="moreideas"),
    path('destmap/<str:pk>',views.destmap,name="destmap")
]
