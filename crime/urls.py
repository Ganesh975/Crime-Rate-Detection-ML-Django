from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as ad
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('ulogin',views.ulogin,name="ulogin"),
    path('uregister',views.uregister,name='uregister'),
    path('ulogout',views.ulogout,name="ulogout"),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)