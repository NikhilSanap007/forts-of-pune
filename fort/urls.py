from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact_form', views.contact_form,name="contact_form"),
    path('forts/',views.forts,name='forts'),
    path('forts/fort_detail/<int:pk>', views.fort_detail, name='fort_detail'),

]