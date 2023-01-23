from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import generics, status
from rest_framework.response import Response

from .models import News, Country
from .serializers import NewsSerializer, CountrySerializer
from rest_framework import viewsets


class NewsViewSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsViewSetPagination

    def get_queryset(self):
        country = self.request.query_params.get('country')
        if country:
            return News.objects.filter(country__id=country).order_by('-published_at')

        return super().get_queryset()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    permission_classes = [IsAdminUser]
