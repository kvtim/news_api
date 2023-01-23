from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'countries', views.CountriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
