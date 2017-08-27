from rest_framework import generics

from pages.models import AbstractPage, SiteNavigation
from pages.serializers import PageMetaAPISerializer, SiteNavigationAPISerializer

class PageMetaAPIView(generics.RetrieveAPIView):
    queryset = AbstractPage.objects.all()
    serializer_class = PageMetaAPISerializer

class SiteNavigationAPIView(generics.ListAPIView):
    queryset = SiteNavigation.objects.all()
    serializer_class = SiteNavigationAPISerializer