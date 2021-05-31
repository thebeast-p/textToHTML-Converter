from django.urls import path


from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('Contact.html',views.contact, name='Contact.html'),
    path('Home.html',views.home, name='Home.html'),
    path('About.html',views.about, name='About.html'),
    path('ConvertPage.html',views.convert, name='ConvertPage'),
    path('Converted.html',views.converted, name='Display'),
]