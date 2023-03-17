from django.contrib import admin
from django.urls import path
from YouGotSpam import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('user-data/', views.user_data, name='user_data'),
]
