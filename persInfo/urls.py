from django.contrib import admin
from django.urls import path
from home.views import home,about ,contact,add_contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addcontact',add_contact, name ='AddContact'),

]
