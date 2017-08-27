from django.conf.urls import url

from pages.api_views import PageMetaAPIView, SiteNavigationAPIView

urlpatterns = [
    url(r'^page-meta/(?P<pk>\d+)', PageMetaAPIView.as_view()),
    url(r'^navigation', SiteNavigationAPIView.as_view()),
]