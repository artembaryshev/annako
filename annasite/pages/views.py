# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.http import Http404

from pages.models import AbstractPage


class BasePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        slug = kwargs['slug']
        if slug == '':
            slug = 'home'
        try:
            return {'page_data': AbstractPage.objects.get(slug=slug)}
        except AbstractPage.DoesNotExist:
            raise Http404