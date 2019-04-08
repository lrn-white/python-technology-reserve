from django.contrib import admin
from django.urls import path, include

# from web.Django.HelloWorld.HelloWorld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.index),
    path('polls/', include('polls.urls')),
]
