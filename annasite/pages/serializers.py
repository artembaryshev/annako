from pages.models import AbstractPage, SiteNavigation
from rest_framework import serializers


class PageMetaAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractPage
        fields = ('title', 'meta_description', 'meta_keywords',)


class SiteNavigationAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteNavigation
        fields = ('link', 'link_title',)
