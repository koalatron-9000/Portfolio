from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
