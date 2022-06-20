from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name = 'indexpage'),
    path(r'search/', views.search_business, name='search_business'),
    path('accounts/profile/',views.profile,name = 'profile'),
    path(r'update_profile', views.update_profile, name='update'),
    path('hoods/', views.hoods, name='hoodpage'),
    path('hoods/join/', views.join_hood, name='joinpage')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)