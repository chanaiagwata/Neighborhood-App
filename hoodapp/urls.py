from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name = 'indexpage'),
    path(r'search/', views.search_business, name='search_business'),
    path('accounts/profile/',views.profile,name = 'profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)